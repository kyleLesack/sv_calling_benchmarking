import configparser
import argparse
import os
from os import path
from pathlib import Path
from glob import glob
from collections import defaultdict
from collections import namedtuple
import itertools
import pybedtools

config = configparser.ConfigParser()
parser = argparse.ArgumentParser()
parser.add_argument("config_file", help="Config file with the paths, filename formats, mock genome names, etc.")
parser.add_argument("caller", help="Caller to analyze")
parser.add_argument('--svim_qual', nargs='?', default=15)

args = parser.parse_args()

# Get overlap between caller predictions and truth
def get_overlap(caller_bedfile, truth_bedfile):
	caller_predicted_variant_count = caller_bedfile.count()
	truth_variant_count = truth_bedfile.count()
	caller_truth_reciprocal_overlap = caller_bedfile.intersect(truth_bedfile, u=True, r=True, f=0.5) # Get intersecting calls with at least 50% reciprocal overlap
	caller_truth_reciprocal_overlap_count = caller_truth_reciprocal_overlap.count()
	caller_truth_any_overlap = caller_bedfile.intersect(truth_bedfile, u=True)
	caller_truth_any_overlap_count = caller_truth_any_overlap.count()
	caller_no_reciprocal_overlap = caller_bedfile.intersect(truth_bedfile, v=True, r=True, f=0.5) # Get caller predictions not found in truth (v parameter returns missing)
	false_positive_count = caller_no_reciprocal_overlap.count()
	caller_missing = truth_bedfile.intersect(caller_bedfile, v=True, r=True, f=0.5) # Get calls missing in caller (v parameter returns missing)
	false_negative_count = caller_missing.count()
	return(caller_predicted_variant_count, truth_variant_count,	caller_truth_reciprocal_overlap_count,caller_truth_any_overlap_count, false_positive_count, false_negative_count)

# Write summary statistics to disk
def write_statistics(predicted_variants,simulated_variants,reciprocal_overlap,any_overlap, false_positives, false_negatives, variant_file, sv_type):
	path = Path(variant_file)
	parent_path = path.parent.absolute() # Get the path for the variant file parent directory
	outputdir = str(parent_path) + "/overlap_with_truth/"
	if not os.path.exists(outputdir): # Check if parent directory exists
		os.makedirs(outputdir)

	outfile = outputdir + sv_type + "_overlap.txt"
	with open(outfile, 'w', newline='\n') as f:
		f.write("Predicted variants: " + str(predicted_variants) + "\n")
		f.write("Simulated variants: " + str(simulated_variants) + "\n")
		f.write("Reciprocal overlap (50% overlap; true positives): " + str(reciprocal_overlap) + "\n")
		f.write("Any overlap: " + str(any_overlap) + "\n")
		f.write("False positives (no reciprocal overlap): " + str(false_positives) + "\n")
		f.write("False negatives (no reciprocal overlap): " + str(false_negatives) + "\n")

config.read(args.config_file) # Read config file to get directories

# Get names of mock genomes
def get_mock_genomes(truth_file):
	mock_name_list = []
	split_name = truth_file.split("MOCKGENOME")[0]
	split_name = split_name + "*/"
	mock_genome_names = glob(split_name)

	for name in mock_genome_names:
		name = name.rstrip("/")
		strip_name = name.rsplit("/",1)[1]
		mock_name_list.append(strip_name)
	return(mock_name_list)

if args.caller == "pbsv" or args.caller == "sniffles":
	for sv_type in ["DEL", "DUP", "INV"]: # SV types to analyze
		for i in [1]:
			truth_file_format = config[args.caller]["TRUTH_PATH"]
			mock_genome_names = get_mock_genomes(truth_file_format) # Get mock genomes
			for mock_genome in mock_genome_names: # Loop through mock genome names in order to find caller and truth vcf files
				truth_file = truth_file_format.replace("MOCKGENOME", mock_genome)
				truth_file = truth_file + mock_genome + "_S0_" + sv_type + ".sorted.bed"
				variant_file = config[args.caller]["VARIANT_PATH"]
				variant_file = variant_file.replace("MOCKGENOME", mock_genome)
				variant_file = variant_file + mock_genome + "_" + sv_type + ".declustered.bed"

				predicted_variant_count = 0
				simulated_variant_count = 0
				false_positive_count = 0

				if os.path.isfile(truth_file):
					with open(truth_file) as f:
						simulated_variants = f.readlines()
						simulated_variant_count = len(simulated_variants)
						truth_bedfile = pybedtools.BedTool(truth_file)

				if os.path.isfile(variant_file):
					with open(variant_file) as f:
						variants = f.readlines()
						predicted_variant_count = len(variants)
						caller_bedfile = pybedtools.BedTool(variant_file)

				if os.path.isfile(variant_file) and os.path.isfile(truth_file):
					caller_truth_overlap = get_overlap(caller_bedfile, truth_bedfile) # Get overlap statistics
					write_statistics(caller_truth_overlap[0],caller_truth_overlap[1],caller_truth_overlap[2],caller_truth_overlap[3], caller_truth_overlap[4], caller_truth_overlap[5],variant_file, sv_type)

				elif os.path.isfile(variant_file) and not os.path.isfile(truth_file):
					print("No truth file: " + truth_file)
					write_statistics(predicted_variant_count,simulated_variant_count, 0,0, predicted_variant_count, 0, variant_file, sv_type) # If no truth file, all predicted SVs are false positives

				elif not os.path.isfile(variant_file) and os.path.isfile(truth_file):
					print("No caller file: " + variant_file)
					write_statistics(predicted_variant_count,simulated_variant_count, 0, 0, 0, simulated_variant_count, variant_file, sv_type) # If no caller file, all simulated SVs are false negatives

				else:
					print("Truth and caller files missing for: " + truth_file + ", " + variant_file)

elif args.caller == "svim":
	for sv_type in ["DEL", "DUP", "INV"]: # SV types to analyze
		for i in [1]:
			truth_file_format = config[args.caller]["TRUTH_PATH"]
			mock_genome_names = get_mock_genomes(truth_file_format)
			for mock_genome in mock_genome_names:
				truth_file = truth_file_format.replace("MOCKGENOME", mock_genome)
				truth_file = truth_file + mock_genome + "_S0_" + sv_type + ".sorted.bed"
				variant_file = config[args.caller]["VARIANT_PATH"]
				variant_file = variant_file.replace("MOCKGENOME", mock_genome)
				variant_file = variant_file.replace("SVIMQUAL", str(args.svim_qual))

				if sv_type == "DUP": # SVIM has two duplication types. If DUP is in the sv_type, open the tandem duplication file
					variant_file = variant_file + mock_genome + "_DUP_TANDEM.declustered.bed"
				else:
					variant_file = variant_file + mock_genome + "_" + sv_type + ".declustered.bed"

				predicted_variant_count = 0
				simulated_variant_count = 0
				false_positive_count = 0

				if os.path.isfile(truth_file):
					with open(truth_file) as f:
						simulated_variants = f.readlines()
						simulated_variant_count = len(simulated_variants)
						truth_bedfile = pybedtools.BedTool(truth_file)

				if os.path.isfile(variant_file):
					with open(variant_file) as f:
						variants = f.readlines()
						predicted_variant_count = len(variants)
						caller_bedfile = pybedtools.BedTool(variant_file)
				else:
					print("Missing variant file: " + str(variant_file))

				if os.path.isfile(variant_file) and os.path.isfile(truth_file):
					caller_truth_overlap = get_overlap(caller_bedfile, truth_bedfile) # Get overlap statistics
					write_statistics(caller_truth_overlap[0],caller_truth_overlap[1],caller_truth_overlap[2],caller_truth_overlap[3], caller_truth_overlap[4], caller_truth_overlap[5],variant_file, sv_type)

				elif os.path.isfile(variant_file) and not os.path.isfile(truth_file):
					print("No truth file: " + truth_file)
					write_statistics(predicted_variant_count,simulated_variant_count, 0,0, predicted_variant_count, 0, variant_file, sv_type) # If no truth file, all predicted SVs are false positives

				elif not os.path.isfile(variant_file) and os.path.isfile(truth_file):
					print("No caller file: " + variant_file)
					write_statistics(predicted_variant_count,simulated_variant_count, 0, 0, 0, simulated_variant_count, variant_file, sv_type) # If no caller file, all simulated SVs are false negatives

				else:
					print("Truth and caller files missing for: " + truth_file + ", " + variant_file)

else:
	print("Incorrect caller: " + str(args.caller))
