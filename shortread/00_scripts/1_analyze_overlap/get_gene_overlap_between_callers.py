import configparser
import argparse
import os
from os import path
from pathlib import Path
from collections import defaultdict
from collections import namedtuple
import itertools
import pybedtools

config = configparser.ConfigParser()

parser = argparse.ArgumentParser()
parser.add_argument("input_config", help="config file for the variant caller paths, filenames, etc.")
parser.add_argument("variant_type", help="variant type to be analyzed")
args = parser.parse_args()

config.read(args.input_config)
variant_callers = config.sections()

samples = config["samples"]["CENDR_SAMPLES"].split()

def get_duplication_paths_filenames():
	caller_duplication_dict = defaultdict()

	caller_path_name = namedtuple('caller_path_name', 'BED_DIR VARIANT_NAME')

	for caller in config.sections():
		if caller != "samples" and caller != "output":
			caller_bed_dir = config[caller]["BED_DIR"]
			caller_duplication_name = config[caller]["DUPLICATION_NAME"]
			caller_details = caller_path_name(caller_bed_dir, caller_duplication_name)
			caller_duplication_dict[caller] = caller_details
	return (caller_duplication_dict)

def get_deletion_inversion_paths_filenames(variant_type_prefix):
	caller_variant_dict = defaultdict()
	caller_path_name = namedtuple('caller_path_name', 'BED_DIR VARIANT_NAME')

	for caller in config.sections():
		if caller != "samples" and caller != "output":

			caller_bed_dir = config[caller]["BED_DIR"]
			variant_name = variant_type_prefix + "_NAME"
			caller_variant_name = config[caller][variant_name]
			caller_details = caller_path_name(caller_bed_dir, caller_variant_name)
			caller_variant_dict[caller] = caller_details
	return (caller_variant_dict)


def get_caller_combinations(caller_variant_dict, output_dir):
	combos = defaultdict(list)
	missing_files = set([])
	caller_variant_combinations = list(itertools.combinations(caller_variant_dict.keys(), 2))
	for caller_combination in caller_variant_combinations:
		caller_1 = caller_combination[0]
		caller_2 = caller_combination[1]
		bed_dir_1 = caller_variant_dict[caller_1][0]
		variant_name_1 = caller_variant_dict[caller_1][1]

		bed_dir_2 = caller_variant_dict[caller_2][0]
		variant_name_2 = caller_variant_dict[caller_2][1]

		for strain in samples:
			variant_name_with_strain_1 = variant_name_1.replace("SAMPLE", strain)
			variant_call_1 = bed_dir_1 + "/" + variant_name_with_strain_1

			variant_name_with_strain_2 = variant_name_2.replace("SAMPLE", strain)
			variant_call_2 = bed_dir_2 + "/" + variant_name_with_strain_2

			# Some files don't exist because the callers did not predict that variant for the sample. Create empty files for these.
			if not os.path.isfile(variant_call_1):
				missing_files.add(variant_call_1)
				variant_call_1 = variant_call_1 + ".empty" # append empty to tag created file
				if not os.path.isfile(variant_call_1):
					parent_dir = Path(variant_call_1).parent.absolute()

					if not os.path.exists(parent_dir): # Check if parent directory exists
						os.makedirs(parent_dir)
					os.mknod(variant_call_1) # Create empty file

			if not os.path.isfile(variant_call_2):
				missing_files.add(variant_call_2)
				variant_call_2 = variant_call_2 + ".empty"
				if not os.path.isfile(variant_call_2):
					parent_dir = Path(variant_call_2).parent.absolute()
					if not os.path.exists(parent_dir):
						os.makedirs(parent_dir)
					os.mknod(variant_call_2)

			if os.path.isfile(variant_call_1) and os.path.isfile(variant_call_2):
				my_combo =  caller_1 + "-" + caller_2 + "\n"
				strain_dir = output_dir + "/" + my_combo.strip() + "/" + strain
				summary_file = strain_dir + "/summary/" + caller_1 + "-overlaps-" + caller_2 + ".txt"

				summarize_commands_list = []
				summarize_commands_list.append("echo -n " + caller_1 + " total calls: > " + summary_file) # Bash command to create summary file
				summarize_commands_list.append("wc -l < " + variant_call_1 + " >> " + summary_file)
				summarize_commands_list.append("echo -n " + caller_2 + " total calls: >> " + summary_file) # Bash command to create summary file
				summarize_commands_list.append("wc -l < " + variant_call_2 + " >> " + summary_file)
				for line in summarize_commands_list:
					combos[my_combo].append(line)

				# Get calls from caller 1 that do not overlap with at least one call from caller 2
				bedfile = strain_dir + "/" + caller_1 + "-no_overlap_with-" + caller_2 + ".bed"
				bedtools_command = "bedtools intersect -f 0.50 -r -v -a " + variant_call_1 + " -b " + variant_call_2 + " > " + bedfile

				summarize_commands_list = []
				summarize_commands_list.append("echo -n " + caller_1 + " unique calls: >> " + summary_file)
				summarize_commands_list.append("wc -l < " + bedfile + " >> " + summary_file)
				combos[my_combo].append(bedtools_command)
				for line in summarize_commands_list:
					combos[my_combo].append(line)

				# Get calls from caller 2 that do not overlap with at least one call from caller 1
				bedfile = strain_dir + "/" + caller_2 + "-no_overlap_with-" + caller_1 + ".bed"
				bedtools_command = "bedtools intersect -f 0.50 -r -v -a " + variant_call_2 + " -b " + variant_call_1 + " > " + bedfile + "\n"

				summarize_commands_list = []
				summarize_commands_list.append("echo -n " + caller_2 + " unique calls: >> " + summary_file)
				summarize_commands_list.append("wc -l < " + bedfile + " >> " + summary_file)
				summarize_command2 = "wc -l < " + bedfile + " >> " + summary_file
				combos[my_combo].append(bedtools_command)
				for line in summarize_commands_list:
					combos[my_combo].append(line)

				# Get overlapping calls
				summarize_commands_list = []
				bedfile = strain_dir + "/" + caller_1 + "-overlaps-" + caller_2 + ".bed"
				bedtools_command = "bedtools intersect -f 0.50 -r -u -a " + variant_call_1 + " -b " + variant_call_2 + " > " + bedfile
				summarize_commands_list.append("echo -n " + " Overlapping calls: >> " + summary_file)
				summarize_commands_list.append("wc -l < " + bedfile + " >> " + summary_file + "\n")
				combos[my_combo].append(bedtools_command)
				for line in summarize_commands_list:
					combos[my_combo].append(line)
			else:
					print("Error: Unable to create combo: " + my_combo)
					print(variant_call_1)
					print(os.path.isfile(variant_call_1))
					print(variant_call_2)
					print(os.path.isfile(variant_call_2))
					input("Press a key")
	return(combos, missing_files)

# Get number of lines in file. Source: https://stackoverflow.com/questions/845058/how-to-get-line-count-of-a-large-file-cheaply-in-python
def file_len(fname):
	num_lines = sum(1 for line in open(fname))
	return num_lines

# Function to get the number of variant calls from
def get_caller_stats(caller, caller_variant_dict, samples, variant_type):
	strain_variant_count_dict = defaultdict()
	bed_dir = caller_variant_dict[caller][0]
	variant_name = caller_variant_dict[caller][1]
	total_calls = 0

	# Loop through strains and get the path for each bedfile and get bedfile line count (variant calls)
	for strain in samples:
		variant_name_with_strain = variant_name.replace("SAMPLE", strain)
		bedfile = bed_dir + "/" + variant_name_with_strain
		if  os.path.isfile(bedfile):
			line_count = file_len(bedfile)
			total_calls = total_calls + line_count
			strain_variant_count_dict[strain] = line_count

	if variant_type == "deletion" or variant_type == "DELETION" or variant_type == "deletions" or variant_type == "DELETIONS":
		output_dir = config["output"]["DEL_OUTDIR"]
		output_dir = output_dir + "caller_stats/" + caller + "/"
	elif variant_type == "duplication" or variant_type == "DUPLICATION" or variant_type == "duplications" or variant_type == "DUPLICATIONS":
		output_dir = config["output"]["DUP_OUTDIR"]
		output_dir = output_dir + "caller_stats/" + caller + "/"
	elif variant_type == "inversion" or variant_type == "INVERSION" or variant_type == "inversions" or variant_type == "INVERSIONS":
		output_dir = config["output"]["INV_OUTDIR"]
		output_dir = output_dir + "caller_stats/" + caller + "/"
	elif variant_type.lower() == "duplication" or variant_type.lower() == "duplications":
		output_dir = config["output"]["DUP_OUTDIR"]
		output_dir = output_dir + "caller_stats/" + caller + "/"

	if not os.path.exists(output_dir): # Check if parent directory exists
		os.makedirs(output_dir)

	outfile = output_dir + "calls_summary.txt"
	print("Writing to: " + outfile)
	with open(outfile, 'w', newline='\n') as f:
		f.write("Total calls: " + str(total_calls) + "\n")
		for strain in strain_variant_count_dict.keys():
			f.write(strain + ": " + str(strain_variant_count_dict[strain]) + "\n")

	return(total_calls)

# Function to get the number of genes spanned by the variant calls for a given caller
def get_caller_gene_stats(caller, caller_variant_dict, samples, variant_type):
	strain_gene_count_dict = defaultdict()
	bed_dir = caller_variant_dict[caller][0]
	variant_name = caller_variant_dict[caller][1]
	total_genes = 0

	# Loop through strains and get the path for each bedfile and get bedfile line count (variant calls)
	for strain in samples:
		strain_gene_count = 0 # Variable to store the number of genes overlapped per strain for a caller
		variant_name_with_strain = variant_name.replace("SAMPLE", strain)
		bedfile = bed_dir + "/" + variant_name_with_strain
		if  os.path.isfile(bedfile):
			with open(bedfile) as f:
				variants = f.readlines()
				for line in variants:
					gene_col = line.split("\t")[4]
					variant_call_genes = gene_col.split(",")
					gene_count=len(variant_call_genes)
					strain_gene_count = strain_gene_count + gene_count
		total_genes = total_genes + strain_gene_count
		strain_gene_count_dict[strain] = strain_gene_count

	if variant_type == "deletion" or variant_type == "DELETION" or variant_type == "deletions" or variant_type == "DELETIONS":
		output_dir = config["output"]["DEL_OUTDIR"]
		output_dir = output_dir + "caller_stats/" + caller + "/"
	elif variant_type == "duplication" or variant_type == "DUPLICATION" or variant_type == "duplications" or variant_type == "DUPLICATIONS":
		output_dir = config["output"]["DUP_OUTDIR"]
		output_dir = output_dir + "caller_stats/" + caller + "/"
	elif variant_type == "inversion" or variant_type == "INVERSION" or variant_type == "inversions" or variant_type == "INVERSIONS":
		output_dir = config["output"]["INV_OUTDIR"]
		output_dir = output_dir + "caller_stats/" + caller + "/"
	elif variant_type.lower() == "duplication" or variant_type.lower() == "duplications":
		output_dir = config["output"]["DUP_OUTDIR"]
		output_dir = output_dir + "caller_stats/" + caller + "/"

	if not os.path.exists(output_dir): # Check if parent directory exists
		os.makedirs(output_dir)

	outfile = output_dir + "gene_summary.txt"
	print("Writing to: " + outfile)
	with open(outfile, 'w', newline='\n') as f:
		f.write("Total genes spanned by variants: " + str(total_genes) + "\n")
		for strain in strain_gene_count_dict.keys():
			f.write(strain + ": " + str(strain_gene_count_dict[strain]) + "\n")

	return(total_genes)


def get_uniq_calls(caller_variant_dict, callers, samples):
	for caller in callers:
		caller_variant_calls = set([])
		bed_dir = caller_variant_dict[caller][0]
		variant_name = caller_variant_dict[caller][1]

		caller_bedfile = bed_dir + "/" + variant_name

		for sample in samples:
			caller_strain_bedfile = caller_bedfile.replace("SAMPLE", sample)
			if os.path.isfile(caller_strain_bedfile):
				with open(caller_strain_bedfile) as f:
					variants = f.readlines()
					for line in variants:
						line_split = line.split()
						caller_line = line_split[0] + "\t" + line_split[1] + "\t" + line_split[2]
						caller_variant_calls.add(caller_line)
			else:
				print("Bedfile not found: " + caller_strain_bedfile)

		# Store variant_calls set elements in a list of lists to allow sorting
		caller_variant_calls_list = []
		for line in caller_variant_calls:
			split_line = line.split()
			chr = split_line[0]
			start_coord = int(split_line[1])
			end_coord = int(split_line[2])
			tuple_line = (chr, start_coord, end_coord)
			caller_variant_calls_list.append(tuple_line)

		caller_variant_calls_list.sort(key=lambda row: (row[0], row[1], row[2]), reverse=False) # Sort the variant calls for bedtools. Sort by chromosome, start coord, then stop coord

		other_callers = set(callers) # Create a set of the callers. Currect caller will be removed to get the other callers
		other_callers.remove(caller)
		other_callers = list(other_callers) # Get a list of the callers that will be checked to see if they don't have any of the calls in the caller of interest
		other_variant_calls = set([]) # Set to store union of all bedfile lines from other callers. Set used to exclude duplicate calls.

		for other_caller in other_callers: # Get variant callers from other callers
			bed_dir = caller_variant_dict[other_caller][0]
			variant_name = caller_variant_dict[other_caller][1]

			other_caller_bedfile = bed_dir + "/" + variant_name

			for sample in samples:
				other_caller_strain_bedfile = other_caller_bedfile.replace("SAMPLE", sample)
				if os.path.isfile(other_caller_strain_bedfile):
					with open(other_caller_strain_bedfile) as f:
						variants = f.readlines()
						for line in variants:
							line_split = line.split()
							other_caller_line = line_split[0] + "\t" + line_split[1] + "\t" + line_split[2]
							other_variant_calls.add(other_caller_line)
				else:
					print("Bedfile not found: " + other_caller_strain_bedfile)

		# Store other_variant_calls set elements in a list of lists to allow sorting
		other_variant_calls_list = []
		for line in other_variant_calls:
			split_line = line.split()
			chr = split_line[0]
			start_coord = int(split_line[1])
			end_coord = int(split_line[2])
			tuple_line = (chr, start_coord, end_coord)
			other_variant_calls_list.append(tuple_line)

		other_variant_calls_list.sort(key=lambda row: (row[0], row[1], row[2]), reverse=False) # Sort the variant calls for bedtools. Sort by chromosome, start coord, then stop coord
		caller_variant_calls_genes = (caller_variant_calls_list)
		other_variant_calls_genes = (other_variant_calls_list)

def get_caller_svs(caller_config_dict, callers, samples):
	caller_variant_dict = defaultdict(lambda: defaultdict(set))
	for caller in callers: # For each caller get variant call bedfile
		caller_svs_by_strain = set([])
		bed_dir = caller_config_dict[caller][0]
		variant_name = caller_config_dict[caller][1]

		caller_bedfile = bed_dir + "/" + variant_name

		for sample in samples:
			gene_set = set()

			caller_strain_bedfile = caller_bedfile.replace("SAMPLE", sample)
			if os.path.isfile(caller_strain_bedfile):
				with open(caller_strain_bedfile) as f:
					variants = f.readlines()
					for line in variants:
						line_split = line.split()
						gene_col = line_split[4]
						gene_list = gene_col.split(",")

						for gene in gene_list:
							gene_set.add(gene)
						caller_variant_dict[caller][sample] = gene_set
			else:
				print("Bedfile not found: " + caller_strain_bedfile)

	return caller_variant_dict

def get_caller_intersections(caller_sv_dict):
	no_variant_calls = set() # Set to store the caller and strain if no variants were predicted
	combo_strain_intersection_dict = defaultdict(lambda: defaultdict(int))
	all_caller_combinations = []
	for r in range(1, len(caller_sv_dict.keys())+ 1):
		caller_combination = itertools.combinations(caller_sv_dict.keys(), r) # Get pairwise comparisons between callers
		all_caller_combinations.append(caller_combination)
	#print("Creating combinations from 1 callers to " + str(r) + " callers." )

	# Iterate through all combinations of callers to determine the agreement between them
	for combo in list(all_caller_combinations):
		if len(caller_sv_dict.keys()) == 7:
			for x in (list(combo)):
				if len(x) == 1:
					combo_name = x[0]
					caller_1 = x[0]

					no_intersection_caller_list = list(caller_sv_dict.keys()) # Create a list to store callers that aren't in combination. Used to get non-intersection set.
					no_intersection_caller_list.remove(caller_1)
					no_intersection_caller_2 = no_intersection_caller_list.pop()
					no_intersection_caller_3 = no_intersection_caller_list.pop()
					no_intersection_caller_4 = no_intersection_caller_list.pop()
					no_intersection_caller_5 = no_intersection_caller_list.pop()
					no_intersection_caller_6 = no_intersection_caller_list.pop()
					no_intersection_caller_7 = no_intersection_caller_list.pop()

					for sample in caller_sv_dict[caller_1].keys():
						if sample in caller_sv_dict[no_intersection_caller_2] and sample in caller_sv_dict[no_intersection_caller_3] and sample in caller_sv_dict[no_intersection_caller_4] and sample in caller_sv_dict[no_intersection_caller_5] and sample in caller_sv_dict[no_intersection_caller_6] and sample in caller_sv_dict[no_intersection_caller_7]:
							caller_1_genes = caller_sv_dict[caller_1][sample]

							no_intersection_caller_2_genes = caller_sv_dict[no_intersection_caller_2][sample]
							no_intersection_caller_3_genes = caller_sv_dict[no_intersection_caller_3][sample]
							no_intersection_caller_4_genes = caller_sv_dict[no_intersection_caller_4][sample]
							no_intersection_caller_5_genes = caller_sv_dict[no_intersection_caller_5][sample]
							no_intersection_caller_6_genes = caller_sv_dict[no_intersection_caller_6][sample]
							no_intersection_caller_7_genes = caller_sv_dict[no_intersection_caller_7][sample]
							sv_intersection = caller_1_genes-no_intersection_caller_2_genes-no_intersection_caller_3_genes-no_intersection_caller_4_genes-no_intersection_caller_5_genes-no_intersection_caller_6_genes-no_intersection_caller_7_genes
							combo_strain_intersection_dict[combo_name][sample] = sv_intersection
						else:

							if sample not in caller_sv_dict[no_intersection_caller_2]:
								no_variant_calls.add("No " + str(args.variant_type.lower()) + "s found in " + no_intersection_caller_2 + " for sample: " + sample)
							if sample not in caller_sv_dict[no_intersection_caller_3]:
								no_variant_calls.add("No " + str(args.variant_type.lower()) + "s found in " + no_intersection_caller_3 + " for sample: " + sample)
							if sample not in caller_sv_dict[no_intersection_caller_4]:
								no_variant_calls.add("No " + str(args.variant_type.lower()) + "s found in " + no_intersection_caller_4 + " for sample: " + sample)
							if sample not in caller_sv_dict[no_intersection_caller_5]:
								no_variant_calls.add("No " + str(args.variant_type.lower()) + "s found in " + no_intersection_caller_5 + " for sample: " + sample)
							if sample not in caller_sv_dict[no_intersection_caller_6]:
								no_variant_calls.add("No " + str(args.variant_type.lower()) + "s found in " + no_intersection_caller_6 + " for sample: " + sample)
							if sample not in caller_sv_dict[no_intersection_caller_7]:
								no_variant_calls.add("No " + str(args.variant_type.lower()) + "s found in " + no_intersection_caller_7 + " for sample: " + sample)

				if len(x) == 2:
					combo_name = ('-'.join(x))
					combo_name = combo_name
					caller_1 = x[0]
					caller_2 = x[1]

					no_intersection_caller_list = list(caller_sv_dict.keys()) # Create a list to store callers that aren't in combination. Used to get non-intersection set.
					no_intersection_caller_list.remove(caller_1)
					no_intersection_caller_list.remove(caller_2)
					no_intersection_caller_3 = no_intersection_caller_list.pop()
					no_intersection_caller_4 = no_intersection_caller_list.pop()
					no_intersection_caller_5 = no_intersection_caller_list.pop()
					no_intersection_caller_6 = no_intersection_caller_list.pop()
					no_intersection_caller_7 = no_intersection_caller_list.pop()

					for sample in caller_sv_dict[caller_1].keys():
						if sample in caller_sv_dict[caller_2] and sample in caller_sv_dict[no_intersection_caller_3] and sample in caller_sv_dict[no_intersection_caller_4] and sample in caller_sv_dict[no_intersection_caller_5] and sample in caller_sv_dict[no_intersection_caller_6] and sample in caller_sv_dict[no_intersection_caller_7]:
							caller_1_genes = caller_sv_dict[caller_1][sample]
							caller_2_genes = caller_sv_dict[caller_2][sample]
							caller_1_and_2_genes = caller_1_genes.intersection(caller_2_genes)

							no_intersection_caller_3_genes = caller_sv_dict[no_intersection_caller_3][sample]
							no_intersection_caller_4_genes = caller_sv_dict[no_intersection_caller_4][sample]
							no_intersection_caller_5_genes = caller_sv_dict[no_intersection_caller_5][sample]
							no_intersection_caller_6_genes = caller_sv_dict[no_intersection_caller_6][sample]
							no_intersection_caller_7_genes = caller_sv_dict[no_intersection_caller_7][sample]
							sv_intersection = caller_1_and_2_genes-no_intersection_caller_3_genes-no_intersection_caller_4_genes-no_intersection_caller_5_genes-no_intersection_caller_6_genes-no_intersection_caller_7_genes

							combo_strain_intersection_dict[combo_name][sample] = sv_intersection
						else:

							if sample not in caller_sv_dict[caller_2]:
								no_variant_calls.add("No " + str(args.variant_type.lower()) + "s found in " + caller_2 + " for sample: " + sample)
							if sample not in caller_sv_dict[no_intersection_caller_3]:
								no_variant_calls.add("No " + str(args.variant_type.lower()) + "s found in " + no_intersection_caller_3 + " for sample: " + sample)
							if sample not in caller_sv_dict[no_intersection_caller_4]:
								no_variant_calls.add("No " + str(args.variant_type.lower()) + "s found in " + no_intersection_caller_4 + " for sample: " + sample)
							if sample not in caller_sv_dict[no_intersection_caller_5]:
								no_variant_calls.add("No " + str(args.variant_type.lower()) + "s found in " + no_intersection_caller_5 + " for sample: " + sample)
							if sample not in caller_sv_dict[no_intersection_caller_6]:
								no_variant_calls.add("No " + str(args.variant_type.lower()) + "s found in " + no_intersection_caller_6 + " for sample: " + sample)
							if sample not in caller_sv_dict[no_intersection_caller_7]:
								no_variant_calls.add("No " + str(args.variant_type.lower()) + "s found in " + no_intersection_caller_7 + " for sample: " + sample)

				if len(x) == 3:
					combo_name = ('-'.join(x))
					combo_name = combo_name
					caller_1 = x[0]
					caller_2 = x[1]
					caller_3 = x[2]

					no_intersection_caller_list = list(caller_sv_dict.keys()) # Create a list to store callers that aren't in combination. Used to get non-intersection set.
					no_intersection_caller_list.remove(caller_1)
					no_intersection_caller_list.remove(caller_2)
					no_intersection_caller_list.remove(caller_3)
					no_intersection_caller_4 = no_intersection_caller_list.pop()
					no_intersection_caller_5 = no_intersection_caller_list.pop()
					no_intersection_caller_6 = no_intersection_caller_list.pop()
					no_intersection_caller_7 = no_intersection_caller_list.pop()

					for sample in caller_sv_dict[caller_1].keys():
						if sample in caller_sv_dict[caller_2] and sample in caller_sv_dict[caller_3] and sample in caller_sv_dict[no_intersection_caller_4] and sample in caller_sv_dict[no_intersection_caller_5] and sample in caller_sv_dict[no_intersection_caller_6] and sample in caller_sv_dict[no_intersection_caller_7]:
							caller_1_genes = caller_sv_dict[caller_1][sample]
							caller_2_genes = caller_sv_dict[caller_2][sample]
							caller_3_genes = caller_sv_dict[caller_3][sample]
							caller_1_and_2_genes = caller_1_genes.intersection(caller_2_genes)
							caller_1_2_and_3_genes = caller_1_and_2_genes.intersection(caller_3_genes)
							no_intersection_caller_4_genes = caller_sv_dict[no_intersection_caller_4][sample]
							no_intersection_caller_5_genes = caller_sv_dict[no_intersection_caller_5][sample]
							no_intersection_caller_6_genes = caller_sv_dict[no_intersection_caller_6][sample]
							no_intersection_caller_7_genes = caller_sv_dict[no_intersection_caller_7][sample]
							sv_intersection = caller_1_2_and_3_genes-no_intersection_caller_4_genes-no_intersection_caller_5_genes-no_intersection_caller_6_genes-no_intersection_caller_7_genes
							combo_strain_intersection_dict[combo_name][sample] = sv_intersection

						else:

							if sample not in caller_sv_dict[caller_2]:
								no_variant_calls.add("No " + str(args.variant_type.lower()) + "s found in " + caller_2 + " for sample: " + sample)
							if sample not in caller_sv_dict[caller_3]:
								no_variant_calls.add("No " + str(args.variant_type.lower()) + "s found in " + caller_3 + " for sample: " + sample)
							if sample not in caller_sv_dict[no_intersection_caller_4]:
								no_variant_calls.add("No " + str(args.variant_type.lower()) + "s found in " + no_intersection_caller_4 + " for sample: " + sample)
							if sample not in caller_sv_dict[no_intersection_caller_5]:
								no_variant_calls.add("No " + str(args.variant_type.lower()) + "s found in " + no_intersection_caller_5 + " for sample: " + sample)
							if sample not in caller_sv_dict[no_intersection_caller_6]:
								no_variant_calls.add("No " + str(args.variant_type.lower()) + "s found in " + no_intersection_caller_6 + " for sample: " + sample)
							if sample not in caller_sv_dict[no_intersection_caller_7]:
								no_variant_calls.add("No " + str(args.variant_type.lower()) + "s found in " + no_intersection_caller_7 + " for sample: " + sample)

				if len(x) == 4:
					combo_name = ('-'.join(x))
					combo_name = combo_name
					caller_1 = x[0]
					caller_2 = x[1]
					caller_3 = x[2]
					caller_4 = x[3]

					no_intersection_caller_list = list(caller_sv_dict.keys()) # Create a list to store callers that aren't in combination. Used to get non-intersection set.
					no_intersection_caller_list.remove(caller_1)
					no_intersection_caller_list.remove(caller_2)
					no_intersection_caller_list.remove(caller_3)
					no_intersection_caller_list.remove(caller_4)
					no_intersection_caller_5 = no_intersection_caller_list.pop()
					no_intersection_caller_6 = no_intersection_caller_list.pop()
					no_intersection_caller_7 = no_intersection_caller_list.pop()

					for sample in caller_sv_dict[caller_1].keys():
						if sample in caller_sv_dict[caller_2] and sample in caller_sv_dict[caller_3] and sample in caller_sv_dict[caller_4] and sample in caller_sv_dict[no_intersection_caller_5] and sample in caller_sv_dict[no_intersection_caller_6] and sample in caller_sv_dict[no_intersection_caller_7]:
							caller_1_genes = caller_sv_dict[caller_1][sample]
							caller_2_genes = caller_sv_dict[caller_2][sample]
							caller_3_genes = caller_sv_dict[caller_3][sample]
							caller_4_genes = caller_sv_dict[caller_4][sample]

							caller_1_and_2_genes = caller_1_genes.intersection(caller_2_genes)
							caller_1_2_and_3_genes = caller_1_and_2_genes.intersection(caller_3_genes)
							caller_1_2_3_and_4_genes = caller_1_2_and_3_genes.intersection(caller_4_genes)

							no_intersection_caller_5_genes = caller_sv_dict[no_intersection_caller_5][sample]
							no_intersection_caller_6_genes = caller_sv_dict[no_intersection_caller_6][sample]
							no_intersection_caller_7_genes = caller_sv_dict[no_intersection_caller_7][sample]
							sv_intersection = caller_1_2_3_and_4_genes-no_intersection_caller_5_genes-no_intersection_caller_6_genes-no_intersection_caller_7_genes
							combo_strain_intersection_dict[combo_name][sample] = sv_intersection
						else:

							if sample not in caller_sv_dict[caller_2]:
								no_variant_calls.add("No " + str(args.variant_type.lower()) + "s found in " + caller_2 + " for sample: " + sample)
							if sample not in caller_sv_dict[caller_3]:
								no_variant_calls.add("No " + str(args.variant_type.lower()) + "s found in " + caller_3 + " for sample: " + sample)
							if sample not in caller_sv_dict[caller_4]:
								no_variant_calls.add("No " + str(args.variant_type.lower()) + "s found in " + caller_4 + " for sample: " + sample)
							if sample not in caller_sv_dict[no_intersection_caller_5]:
								no_variant_calls.add("No " + str(args.variant_type.lower()) + "s found in " + no_intersection_caller_5 + " for sample: " + sample)
							if sample not in caller_sv_dict[no_intersection_caller_6]:
								no_variant_calls.add("No " + str(args.variant_type.lower()) + "s found in " + no_intersection_caller_6 + " for sample: " + sample)
							if sample not in caller_sv_dict[no_intersection_caller_7]:
								no_variant_calls.add("No " + str(args.variant_type.lower()) + "s found in " + no_intersection_caller_7 + " for sample: " + sample)

				if len(x) == 5:
					combo_name = ('-'.join(x))
					combo_name = combo_name
					caller_1 = x[0]
					caller_2 = x[1]
					caller_3 = x[2]
					caller_4 = x[3]
					caller_5 = x[4]

					no_intersection_caller_list = list(caller_sv_dict.keys()) # Create a list to store callers that aren't in combination. Used to get non-intersection set.
					no_intersection_caller_list.remove(caller_1)
					no_intersection_caller_list.remove(caller_2)
					no_intersection_caller_list.remove(caller_3)
					no_intersection_caller_list.remove(caller_4)
					no_intersection_caller_list.remove(caller_5)
					no_intersection_caller_6 = no_intersection_caller_list.pop()
					no_intersection_caller_7 = no_intersection_caller_list.pop()

					for sample in caller_sv_dict[caller_1].keys():
						if sample in caller_sv_dict[caller_2] and sample in caller_sv_dict[caller_3] and sample in caller_sv_dict[caller_4] and sample in caller_sv_dict[caller_5] and sample in caller_sv_dict[no_intersection_caller_6] and sample in caller_sv_dict[no_intersection_caller_7]:
							caller_1_genes = caller_sv_dict[caller_1][sample]
							caller_2_genes = caller_sv_dict[caller_2][sample]
							caller_3_genes = caller_sv_dict[caller_3][sample]
							caller_4_genes = caller_sv_dict[caller_4][sample]
							caller_5_genes = caller_sv_dict[caller_5][sample]
							caller_1_and_2_genes = caller_1_genes.intersection(caller_2_genes)
							caller_1_2_and_3_genes = caller_1_and_2_genes.intersection(caller_3_genes)
							caller_1_2_3_and_4_genes = caller_1_2_and_3_genes.intersection(caller_4_genes)
							caller_1_2_3_4_and_5_genes = caller_1_2_3_and_4_genes.intersection(caller_5_genes)
							no_intersection_caller_6_genes = caller_sv_dict[no_intersection_caller_6][sample]
							no_intersection_caller_7_genes = caller_sv_dict[no_intersection_caller_7][sample]
							sv_intersection = caller_1_2_3_4_and_5_genes-no_intersection_caller_6_genes-no_intersection_caller_7_genes
							combo_strain_intersection_dict[combo_name][sample] = sv_intersection
						else:

							if sample not in caller_sv_dict[caller_2]:
								no_variant_calls.add("No " + str(args.variant_type.lower()) + "s found in " + caller_2 + " for sample: " + sample)
							if sample not in caller_sv_dict[caller_3]:
								no_variant_calls.add("No " + str(args.variant_type.lower()) + "s found in " + caller_3 + " for sample: " + sample)
							if sample not in caller_sv_dict[caller_4]:
								no_variant_calls.add("No " + str(args.variant_type.lower()) + "s found in " + caller_4 + " for sample: " + sample)
							if sample not in caller_sv_dict[caller_5]:
								no_variant_calls.add("No " + str(args.variant_type.lower()) + "s found in " + caller_5 + " for sample: " + sample)
							if sample not in caller_sv_dict[no_intersection_caller_6]:
								no_variant_calls.add("No " + str(args.variant_type.lower()) + "s found in " + no_intersection_caller_6 + " for sample: " + sample)
							if sample not in caller_sv_dict[no_intersection_caller_7]:
								no_variant_calls.add("No " + str(args.variant_type.lower()) + "s found in " + no_intersection_caller_7 + " for sample: " + sample)

				if len(x) == 6:
					combo_name = ('-'.join(x))
					combo_name = combo_name
					caller_1 = x[0]
					caller_2 = x[1]
					caller_3 = x[2]
					caller_4 = x[3]
					caller_5 = x[4]
					caller_6 = x[5]

					no_intersection_caller_list = list(caller_sv_dict.keys()) # Create a list to store callers that aren't in combination. Used to get non-intersection set.
					no_intersection_caller_list.remove(caller_1)
					no_intersection_caller_list.remove(caller_2)
					no_intersection_caller_list.remove(caller_3)
					no_intersection_caller_list.remove(caller_4)
					no_intersection_caller_list.remove(caller_5)
					no_intersection_caller_list.remove(caller_6)
					no_intersection_caller_7 = no_intersection_caller_list.pop()

					for sample in caller_sv_dict[caller_1].keys():
						if sample in caller_sv_dict[caller_2] and sample in caller_sv_dict[caller_3] and sample in caller_sv_dict[caller_4] and sample in caller_sv_dict[caller_5] and sample in caller_sv_dict[caller_6]and sample in caller_sv_dict[no_intersection_caller_7]:
							caller_1_genes = caller_sv_dict[caller_1][sample]
							caller_2_genes = caller_sv_dict[caller_2][sample]
							caller_3_genes = caller_sv_dict[caller_3][sample]
							caller_4_genes = caller_sv_dict[caller_4][sample]
							caller_5_genes = caller_sv_dict[caller_5][sample]
							caller_6_genes = caller_sv_dict[caller_6][sample]

							caller_1_and_2_genes = caller_1_genes.intersection(caller_2_genes)
							caller_1_2_and_3_genes = caller_1_and_2_genes.intersection(caller_3_genes)
							caller_1_2_3_and_4_genes = caller_1_2_and_3_genes.intersection(caller_4_genes)
							caller_1_2_3_4_and_5_genes = caller_1_2_3_and_4_genes.intersection(caller_5_genes)
							caller_1_2_3_4_5_and_6_genes = caller_1_2_3_4_and_5_genes.intersection(caller_6_genes)
							no_intersection_caller_7_genes = caller_sv_dict[no_intersection_caller_7][sample]
							sv_intersection = caller_1_2_3_4_5_and_6_genes-no_intersection_caller_7_genes
							combo_strain_intersection_dict[combo_name][sample] = sv_intersection
						else:

							if sample not in caller_sv_dict[caller_2]:
								no_variant_calls.add("No " + str(args.variant_type.lower()) + "s found in " + caller_2 + " for sample: " + sample)
							if sample not in caller_sv_dict[caller_3]:
								no_variant_calls.add("No " + str(args.variant_type.lower()) + "s found in " + caller_3 + " for sample: " + sample)
							if sample not in caller_sv_dict[caller_4]:
								no_variant_calls.add("No " + str(args.variant_type.lower()) + "s found in " + caller_4 + " for sample: " + sample)
							if sample not in caller_sv_dict[caller_5]:
								no_variant_calls.add("No " + str(args.variant_type.lower()) + "s found in " + caller_5 + " for sample: " + sample)
							if sample not in caller_sv_dict[caller_6]:
								no_variant_calls.add("No " + str(args.variant_type.lower()) + "s found in " + caller_6 + " for sample: " + sample)
							if sample not in caller_sv_dict[no_intersection_caller_7]:
								no_variant_calls.add("No " + str(args.variant_type.lower()) + "s found in " + no_intersection_caller_7 + " for sample: " + sample)

				if len(x) == 7:
					combo_name = ('-'.join(x))
					combo_name = combo_name
					caller_1 = x[0]
					caller_2 = x[1]
					caller_3 = x[2]
					caller_4 = x[3]
					caller_5 = x[4]
					caller_6 = x[5]
					caller_7 = x[6]

					for sample in caller_sv_dict[caller_1].keys():
						if sample in caller_sv_dict[caller_2] and sample in caller_sv_dict[caller_3] and sample in caller_sv_dict[caller_4] and sample in caller_sv_dict[caller_5] and sample in caller_sv_dict[caller_6] and sample in caller_sv_dict[caller_7]:
							caller_1_genes = caller_sv_dict[caller_1][sample]
							caller_2_genes = caller_sv_dict[caller_2][sample]
							caller_3_genes = caller_sv_dict[caller_3][sample]
							caller_4_genes = caller_sv_dict[caller_4][sample]
							caller_5_genes = caller_sv_dict[caller_5][sample]
							caller_6_genes = caller_sv_dict[caller_6][sample]
							caller_7_genes = caller_sv_dict[caller_7][sample]

							caller_1_and_2_genes = caller_1_genes.intersection(caller_2_genes)
							caller_1_2_and_3_genes = caller_1_and_2_genes.intersection(caller_3_genes)
							caller_1_2_3_and_4_genes = caller_1_2_and_3_genes.intersection(caller_4_genes)
							caller_1_2_3_4_and_5_genes = caller_1_2_3_and_4_genes.intersection(caller_5_genes)
							caller_1_2_3_4_5_and_6_genes = caller_1_2_3_4_and_5_genes.intersection(caller_6_genes)
							caller_1_2_3_4_5_6_and_7_genes = caller_1_2_3_4_5_and_6_genes.intersection(caller_7_genes)

							sv_intersection = caller_1_2_3_4_5_6_and_7_genes
							combo_strain_intersection_dict[combo_name][sample] = sv_intersection
						else:

							if sample not in caller_sv_dict[caller_2]:
								no_variant_calls.add("No " + str(args.variant_type.lower()) + "s found in " + caller_2 + " for sample: " + sample)
							if sample not in caller_sv_dict[caller_3]:
								no_variant_calls.add("No " + str(args.variant_type.lower()) + "s found in " + caller_3 + " for sample: " + sample)
							if sample not in caller_sv_dict[caller_4]:
								no_variant_calls.add("No " + str(args.variant_type.lower()) + "s found in " + caller_4 + " for sample: " + sample)
							if sample not in caller_sv_dict[caller_5]:
								no_variant_calls.add("No " + str(args.variant_type.lower()) + "s found in " + caller_5 + " for sample: " + sample)
							if sample not in caller_sv_dict[caller_6]:
								no_variant_calls.add("No " + str(args.variant_type.lower()) + "s found in " + caller_6 + " for sample: " + sample)
							if sample not in caller_sv_dict[caller_7]:
								no_variant_calls.add("No " + str(args.variant_type.lower()) + "s found in " + caller_7 + " for sample: " + sample)



		if len(caller_sv_dict.keys()) == 6:
			for x in (list(combo)):
				if len(x) == 1:
					combo_name = x[0]
					caller_1 = x[0]

					no_intersection_caller_list = list(caller_sv_dict.keys()) # Create a list to store callers that aren't in combination. Used to get non-intersection set.
					no_intersection_caller_list.remove(caller_1)
					no_intersection_caller_2 = no_intersection_caller_list.pop()
					no_intersection_caller_3 = no_intersection_caller_list.pop()
					no_intersection_caller_4 = no_intersection_caller_list.pop()
					no_intersection_caller_5 = no_intersection_caller_list.pop()
					no_intersection_caller_6 = no_intersection_caller_list.pop()

					for sample in caller_sv_dict[caller_1].keys():
						if sample in caller_sv_dict[no_intersection_caller_2] and sample in caller_sv_dict[no_intersection_caller_3] and sample in caller_sv_dict[no_intersection_caller_4] and sample in caller_sv_dict[no_intersection_caller_5] and sample in caller_sv_dict[no_intersection_caller_6]:
							caller_1_genes = caller_sv_dict[caller_1][sample]
							no_intersection_caller_2_genes = caller_sv_dict[no_intersection_caller_2][sample]
							no_intersection_caller_3_genes = caller_sv_dict[no_intersection_caller_3][sample]
							no_intersection_caller_4_genes = caller_sv_dict[no_intersection_caller_4][sample]
							no_intersection_caller_5_genes = caller_sv_dict[no_intersection_caller_5][sample]
							no_intersection_caller_6_genes = caller_sv_dict[no_intersection_caller_6][sample]
							sv_intersection = caller_1_genes-no_intersection_caller_2_genes-no_intersection_caller_3_genes-no_intersection_caller_4_genes-no_intersection_caller_5_genes-no_intersection_caller_6_genes
							combo_strain_intersection_dict[combo_name][sample] = sv_intersection
						else:

							if sample not in caller_sv_dict[no_intersection_caller_2]:
								print(sample + " not in " + no_intersection_caller_2)
							if sample not in caller_sv_dict[no_intersection_caller_3]:
								no_variant_calls.add("No " + str(args.variant_type.lower()) + "s found in " + no_intersection_caller_3 + " for sample: " + sample)
							if sample not in caller_sv_dict[no_intersection_caller_4]:
								no_variant_calls.add("No " + str(args.variant_type.lower()) + "s found in " + no_intersection_caller_4 + " for sample: " + sample)
							if sample not in caller_sv_dict[no_intersection_caller_5]:
								no_variant_calls.add("No " + str(args.variant_type.lower()) + "s found in " + no_intersection_caller_5 + " for sample: " + sample)
							if sample not in caller_sv_dict[no_intersection_caller_6]:
								no_variant_calls.add("No " + str(args.variant_type.lower()) + "s found in " + no_intersection_caller_6 + " for sample: " + sample)

				if len(x) == 2:
					combo_name = ('-'.join(x))
					combo_name = combo_name
					caller_1 = x[0]
					caller_2 = x[1]

					no_intersection_caller_list = list(caller_sv_dict.keys()) # Create a list to store callers that aren't in combination. Used to get non-intersection set.
					no_intersection_caller_list.remove(caller_1)
					no_intersection_caller_list.remove(caller_2)
					no_intersection_caller_3 = no_intersection_caller_list.pop()
					no_intersection_caller_4 = no_intersection_caller_list.pop()
					no_intersection_caller_5 = no_intersection_caller_list.pop()
					no_intersection_caller_6 = no_intersection_caller_list.pop()

					for sample in caller_sv_dict[caller_1].keys():
						if sample in caller_sv_dict[caller_2] and sample in caller_sv_dict[no_intersection_caller_3] and sample in caller_sv_dict[no_intersection_caller_4] and sample in caller_sv_dict[no_intersection_caller_5] and sample in caller_sv_dict[no_intersection_caller_6]:
							caller_1_genes = caller_sv_dict[caller_1][sample]
							caller_2_genes = caller_sv_dict[caller_2][sample]
							caller_1_and_2_genes = caller_1_genes.intersection(caller_2_genes)

							no_intersection_caller_3_genes = caller_sv_dict[no_intersection_caller_3][sample]
							no_intersection_caller_4_genes = caller_sv_dict[no_intersection_caller_4][sample]
							no_intersection_caller_5_genes = caller_sv_dict[no_intersection_caller_5][sample]
							no_intersection_caller_6_genes = caller_sv_dict[no_intersection_caller_6][sample]
							sv_intersection = caller_1_and_2_genes-no_intersection_caller_3_genes-no_intersection_caller_4_genes-no_intersection_caller_5_genes-no_intersection_caller_6_genes
							combo_strain_intersection_dict[combo_name][sample] = sv_intersection
						else:

							if sample not in caller_sv_dict[caller_2]:
								no_variant_calls.add("No " + str(args.variant_type.lower()) + "s found in " + caller_2 + " for sample: " + sample)
							if sample not in caller_sv_dict[no_intersection_caller_3]:
								no_variant_calls.add("No " + str(args.variant_type.lower()) + "s found in " + no_intersection_caller_3 + " for sample: " + sample)
							if sample not in caller_sv_dict[no_intersection_caller_4]:
								no_variant_calls.add("No " + str(args.variant_type.lower()) + "s found in " + no_intersection_caller_4 + " for sample: " + sample)
							if sample not in caller_sv_dict[no_intersection_caller_5]:
								no_variant_calls.add("No " + str(args.variant_type.lower()) + "s found in " + no_intersection_caller_5 + " for sample: " + sample)
							if sample not in caller_sv_dict[no_intersection_caller_6]:
								no_variant_calls.add("No " + str(args.variant_type.lower()) + "s found in " + no_intersection_caller_6 + " for sample: " + sample)

				if len(x) == 3:
					combo_name = ('-'.join(x))
					combo_name = combo_name
					caller_1 = x[0]
					caller_2 = x[1]
					caller_3 = x[2]

					no_intersection_caller_list = list(caller_sv_dict.keys()) # Create a list to store callers that aren't in combination. Used to get non-intersection set.
					no_intersection_caller_list.remove(caller_1)
					no_intersection_caller_list.remove(caller_2)
					no_intersection_caller_list.remove(caller_3)
					no_intersection_caller_4 = no_intersection_caller_list.pop()
					no_intersection_caller_5 = no_intersection_caller_list.pop()
					no_intersection_caller_6 = no_intersection_caller_list.pop()

					for sample in caller_sv_dict[caller_1].keys():
						if sample in caller_sv_dict[caller_2] and sample in caller_sv_dict[caller_3] and sample in caller_sv_dict[no_intersection_caller_4] and sample in caller_sv_dict[no_intersection_caller_5] and sample in caller_sv_dict[no_intersection_caller_6]:
							caller_1_genes = caller_sv_dict[caller_1][sample]
							caller_2_genes = caller_sv_dict[caller_2][sample]
							caller_3_genes = caller_sv_dict[caller_3][sample]
							caller_1_and_2_genes = caller_1_genes.intersection(caller_2_genes)
							caller_1_2_and_3_genes = caller_1_and_2_genes.intersection(caller_3_genes)
							no_intersection_caller_4_genes = caller_sv_dict[no_intersection_caller_4][sample]
							no_intersection_caller_5_genes = caller_sv_dict[no_intersection_caller_5][sample]
							no_intersection_caller_6_genes = caller_sv_dict[no_intersection_caller_6][sample]
							sv_intersection = caller_1_2_and_3_genes-no_intersection_caller_4_genes-no_intersection_caller_5_genes-no_intersection_caller_6_genes
							combo_strain_intersection_dict[combo_name][sample] = sv_intersection
						else:

							if sample not in caller_sv_dict[caller_2]:
								no_variant_calls.add("No " + str(args.variant_type.lower()) + "s found in " + caller_2 + " for sample: " + sample)
							if sample not in caller_sv_dict[caller_3]:
								no_variant_calls.add("No " + str(args.variant_type.lower()) + "s found in " + caller_3 + " for sample: " + sample)
							if sample not in caller_sv_dict[no_intersection_caller_4]:
								no_variant_calls.add("No " + str(args.variant_type.lower()) + "s found in " + no_intersection_caller_4 + " for sample: " + sample)
							if sample not in caller_sv_dict[no_intersection_caller_5]:
								no_variant_calls.add("No " + str(args.variant_type.lower()) + "s found in " + no_intersection_caller_5 + " for sample: " + sample)
							if sample not in caller_sv_dict[no_intersection_caller_6]:
								no_variant_calls.add("No " + str(args.variant_type.lower()) + "s found in " + no_intersection_caller_6 + " for sample: " + sample)

				if len(x) == 4:
					combo_name = ('-'.join(x))
					combo_name = combo_name
					caller_1 = x[0]
					caller_2 = x[1]
					caller_3 = x[2]
					caller_4 = x[3]

					no_intersection_caller_list = list(caller_sv_dict.keys()) # Create a list to store callers that aren't in combination. Used to get non-intersection set.
					no_intersection_caller_list.remove(caller_1)
					no_intersection_caller_list.remove(caller_2)
					no_intersection_caller_list.remove(caller_3)
					no_intersection_caller_list.remove(caller_4)
					no_intersection_caller_5 = no_intersection_caller_list.pop()
					no_intersection_caller_6 = no_intersection_caller_list.pop()

					for sample in caller_sv_dict[caller_1].keys():
						if sample in caller_sv_dict[caller_2] and sample in caller_sv_dict[no_intersection_caller_3] and sample in caller_sv_dict[caller_4] and sample in caller_sv_dict[no_intersection_caller_5] and sample in caller_sv_dict[no_intersection_caller_6]:
							caller_1_genes = caller_sv_dict[caller_1][sample]
							caller_2_genes = caller_sv_dict[caller_2][sample]
							caller_3_genes = caller_sv_dict[caller_3][sample]
							caller_4_genes = caller_sv_dict[caller_4][sample]

							caller_1_and_2_genes = caller_1_genes.intersection(caller_2_genes)
							caller_1_2_and_3_genes = caller_1_and_2_genes.intersection(caller_3_genes)
							caller_1_2_3_and_4_genes = caller_1_2_and_3_genes.intersection(caller_4_genes)

							no_intersection_caller_5_genes = caller_sv_dict[no_intersection_caller_5][sample]
							no_intersection_caller_6_genes = caller_sv_dict[no_intersection_caller_6][sample]
							sv_intersection = caller_1_2_3_and_4_genes-no_intersection_caller_5_genes-no_intersection_caller_6_genes
							combo_strain_intersection_dict[combo_name][sample] = sv_intersection
						else:

							if sample not in caller_sv_dict[caller_2]:
								no_variant_calls.add("No " + str(args.variant_type.lower()) + "s found in " + caller_2 + " for sample: " + sample)
							if sample not in caller_sv_dict[caller_3]:
								no_variant_calls.add("No " + str(args.variant_type.lower()) + "s found in " + caller_3 + " for sample: " + sample)
							if sample not in caller_sv_dict[caller_4]:
								no_variant_calls.add("No " + str(args.variant_type.lower()) + "s found in " + caller_4 + " for sample: " + sample)
							if sample not in caller_sv_dict[no_intersection_caller_5]:
								no_variant_calls.add("No " + str(args.variant_type.lower()) + "s found in " + no_intersection_caller_5 + " for sample: " + sample)
							if sample not in caller_sv_dict[no_intersection_caller_6]:
								no_variant_calls.add("No " + str(args.variant_type.lower()) + "s found in " + no_intersection_caller_6 + " for sample: " + sample)

				if len(x) == 5:
					combo_name = ('-'.join(x))
					combo_name = combo_name
					caller_1 = x[0]
					caller_2 = x[1]
					caller_3 = x[2]
					caller_4 = x[3]
					caller_5 = x[4]

					no_intersection_caller_list = list(caller_sv_dict.keys()) # Create a list to store callers that aren't in combination. Used to get non-intersection set.
					no_intersection_caller_list.remove(caller_1)
					no_intersection_caller_list.remove(caller_2)
					no_intersection_caller_list.remove(caller_3)
					no_intersection_caller_list.remove(caller_4)
					no_intersection_caller_list.remove(caller_5)
					no_intersection_caller_6 = no_intersection_caller_list.pop()

					for sample in caller_sv_dict[caller_1].keys():
						if sample in caller_sv_dict[caller_2] and sample in caller_sv_dict[no_intersection_caller_3] and sample in caller_sv_dict[no_intersection_caller_4] and sample in caller_sv_dict[no_intersection_caller_5] and sample in caller_sv_dict[no_intersection_caller_6]:
							caller_1_genes = caller_sv_dict[caller_1][sample]
							caller_2_genes = caller_sv_dict[caller_2][sample]
							caller_3_genes = caller_sv_dict[caller_3][sample]
							caller_4_genes = caller_sv_dict[caller_4][sample]
							caller_5_genes = caller_sv_dict[caller_5][sample]
							caller_1_and_2_genes = caller_1_genes.intersection(caller_2_genes)
							caller_1_2_and_3_genes = caller_1_and_2_genes.intersection(caller_3_genes)
							caller_1_2_3_and_4_genes = caller_1_2_and_3_genes.intersection(caller_4_genes)
							caller_1_2_3_4_and_5_genes = caller_1_2_3_and_4_genes.intersection(caller_5_genes)

							no_intersection_caller_6_genes = caller_sv_dict[no_intersection_caller_6][sample]
							sv_intersection = caller_1_2_3_4_and_5_genes-no_intersection_caller_6_genes
							combo_strain_intersection_dict[combo_name][sample] = sv_intersection
						else:

							if sample not in caller_sv_dict[caller_2]:
								no_variant_calls.add("No " + str(args.variant_type.lower()) + "s found in " + caller_2 + " for sample: " + sample)
							if sample not in caller_sv_dict[caller_3]:
								no_variant_calls.add("No " + str(args.variant_type.lower()) + "s found in " + caller_3 + " for sample: " + sample)
							if sample not in caller_sv_dict[caller_4]:
								no_variant_calls.add("No " + str(args.variant_type.lower()) + "s found in " + caller_4 + " for sample: " + sample)
							if sample not in caller_sv_dict[caller_5]:
								no_variant_calls.add("No " + str(args.variant_type.lower()) + "s found in " + caller_5 + " for sample: " + sample)
							if sample not in caller_sv_dict[no_intersection_caller_6]:
								no_variant_calls.add("No " + str(args.variant_type.lower()) + "s found in " + no_intersection_caller_6 + " for sample: " + sample)

				if len(x) == 6:
					combo_name = ('-'.join(x))
					combo_name = combo_name
					caller_1 = x[0]
					caller_2 = x[1]
					caller_3 = x[2]
					caller_4 = x[3]
					caller_5 = x[4]
					caller_6 = x[5]

					for sample in caller_sv_dict[caller_1].keys():
						if sample in caller_sv_dict[caller_2] and sample in caller_sv_dict[no_intersection_caller_3] and sample in caller_sv_dict[no_intersection_caller_4] and sample in caller_sv_dict[no_intersection_caller_5] and sample in caller_sv_dict[no_intersection_caller_6]:
							caller_1_genes = caller_sv_dict[caller_1][sample]
							caller_2_genes = caller_sv_dict[caller_2][sample]
							caller_3_genes = caller_sv_dict[caller_3][sample]
							caller_4_genes = caller_sv_dict[caller_4][sample]
							caller_5_genes = caller_sv_dict[caller_5][sample]
							caller_6_genes = caller_sv_dict[caller_6][sample]

							caller_1_and_2_genes = caller_1_genes.intersection(caller_2_genes)
							caller_1_2_and_3_genes = caller_1_and_2_genes.intersection(caller_3_genes)
							caller_1_2_3_and_4_genes = caller_1_2_and_3_genes.intersection(caller_4_genes)
							caller_1_2_3_4_and_5_genes = caller_1_2_3_and_4_genes.intersection(caller_5_genes)
							caller_1_2_3_4_5_and_6_genes = caller_1_2_3_4_and_5_genes.intersection(caller_6_genes)

							sv_intersection = caller_1_2_3_4_5_and_6_genes
							combo_strain_intersection_dict[combo_name][sample] = sv_intersection
						else:

							if sample not in caller_sv_dict[caller_2]:
								no_variant_calls.add("No " + str(args.variant_type.lower()) + "s found in " + caller_2 + " for sample: " + sample)
							if sample not in caller_sv_dict[caller_3]:
								no_variant_calls.add("No " + str(args.variant_type.lower()) + "s found in " + caller_3 + " for sample: " + sample)
							if sample not in caller_sv_dict[caller_4]:
								no_variant_calls.add("No " + str(args.variant_type.lower()) + "s found in " + caller_4 + " for sample: " + sample)
							if sample not in caller_sv_dict[caller_5]:
								no_variant_calls.add("No " + str(args.variant_type.lower()) + "s found in " + caller_5 + " for sample: " + sample)
							if sample not in caller_sv_dict[caller_6]:
								no_variant_calls.add("No " + str(args.variant_type.lower()) + "s found in " + caller_6 + " for sample: " + sample)

		if len(caller_sv_dict.keys()) == 5:
			for x in (list(combo)):
				if len(x) == 1:
					combo_name = (x)
					combo_name = combo_name[0]
					caller_1 = x[0]

					no_intersection_caller_list = list(caller_sv_dict.keys()) # Create a list to store callers that aren't in combination. Used to get non-intersection set.
					no_intersection_caller_list.remove(caller_1)
					no_intersection_caller_2 = no_intersection_caller_list.pop()
					no_intersection_caller_3 = no_intersection_caller_list.pop()
					no_intersection_caller_4 = no_intersection_caller_list.pop()
					no_intersection_caller_5 = no_intersection_caller_list.pop()


					for sample in caller_sv_dict[caller_1].keys():
						if sample in caller_sv_dict[no_intersection_caller_2] and sample in caller_sv_dict[no_intersection_caller_3] and sample in caller_sv_dict[no_intersection_caller_4] and sample in caller_sv_dict[no_intersection_caller_5]:
							caller_1_genes = caller_sv_dict[caller_1][sample]
							no_intersection_caller_2_genes = caller_sv_dict[no_intersection_caller_2][sample]
							no_intersection_caller_3_genes = caller_sv_dict[no_intersection_caller_3][sample]
							no_intersection_caller_4_genes = caller_sv_dict[no_intersection_caller_4][sample]
							no_intersection_caller_5_genes = caller_sv_dict[no_intersection_caller_5][sample]

							sv_intersection_uniq = caller_1_genes-no_intersection_caller_2_genes-no_intersection_caller_3_genes-no_intersection_caller_4_genes-no_intersection_caller_5_genes
							combo_strain_intersection_dict[combo_name][sample] = sv_intersection_uniq

						else:

							if sample not in caller_sv_dict[no_intersection_caller_2]:
								print(sample + " not in " + no_intersection_caller_2)
							if sample not in caller_sv_dict[no_intersection_caller_3]:
								no_variant_calls.add("No " + str(args.variant_type.lower()) + "s found in " + no_intersection_caller_3 + " for sample: " + sample)
							if sample not in caller_sv_dict[no_intersection_caller_4]:
								no_variant_calls.add("No " + str(args.variant_type.lower()) + "s found in " + no_intersection_caller_4 + " for sample: " + sample)
							if sample not in caller_sv_dict[no_intersection_caller_5]:
								no_variant_calls.add("No " + str(args.variant_type.lower()) + "s found in " + no_intersection_caller_5 + " for sample: " + sample)

				if len(x) == 2:
					combo_name = ('-'.join(x))
					caller_1 = x[0]
					caller_2 = x[1]

					no_intersection_caller_list = list(caller_sv_dict.keys()) # Create a list to store callers that aren't in combination. Used to get non-intersection set.
					no_intersection_caller_list.remove(caller_1)
					no_intersection_caller_list.remove(caller_2)
					no_intersection_caller_3 = no_intersection_caller_list.pop()
					no_intersection_caller_4 = no_intersection_caller_list.pop()
					no_intersection_caller_5 = no_intersection_caller_list.pop()

					for sample in caller_sv_dict[caller_1].keys():
						if sample in caller_sv_dict[caller_2] and sample in caller_sv_dict[no_intersection_caller_3] and sample in caller_sv_dict[no_intersection_caller_4] and sample in caller_sv_dict[no_intersection_caller_5]:
							caller_1_genes = caller_sv_dict[caller_1][sample]
							caller_2_genes = caller_sv_dict[caller_2][sample]
							caller_1_and_2_genes = caller_1_genes.intersection(caller_2_genes)
							no_intersection_caller_3_genes = caller_sv_dict[no_intersection_caller_3][sample]
							no_intersection_caller_4_genes = caller_sv_dict[no_intersection_caller_4][sample]
							no_intersection_caller_5_genes = caller_sv_dict[no_intersection_caller_5][sample]
							sv_intersection_uniq = caller_1_and_2_genes-no_intersection_caller_3_genes-no_intersection_caller_4_genes-no_intersection_caller_5_genes
							combo_strain_intersection_dict[combo_name][sample] = sv_intersection_uniq

						else:

							if sample not in caller_sv_dict[caller_2]:
								no_variant_calls.add("No " + str(args.variant_type.lower()) + "s found in " + caller_2 + " for sample: " + sample)
							if sample not in caller_sv_dict[no_intersection_caller_3]:
								no_variant_calls.add("No " + str(args.variant_type.lower()) + "s found in " + no_intersection_caller_3 + " for sample: " + sample)
							if sample not in caller_sv_dict[no_intersection_caller_4]:
								no_variant_calls.add("No " + str(args.variant_type.lower()) + "s found in " + no_intersection_caller_4 + " for sample: " + sample)
							if sample not in caller_sv_dict[no_intersection_caller_5]:
								no_variant_calls.add("No " + str(args.variant_type.lower()) + "s found in " + no_intersection_caller_5 + " for sample: " + sample)

				if len(x) == 3:
					combo_name = ('-'.join(x))
					caller_1 = x[0]
					caller_2 = x[1]
					caller_3 = x[2]
					no_intersection_caller_list = list(caller_sv_dict.keys()) # Create a list to store callers that aren't in combination. Used to get non-intersection set.
					no_intersection_caller_list.remove(caller_1)
					no_intersection_caller_list.remove(caller_2)
					no_intersection_caller_list.remove(caller_3)
					no_intersection_caller_4 = no_intersection_caller_list.pop()
					no_intersection_caller_5 = no_intersection_caller_list.pop()


					for sample in caller_sv_dict[caller_1].keys():
						if sample in caller_sv_dict[caller_2] and sample in caller_sv_dict[caller_3] and sample in caller_sv_dict[no_intersection_caller_4] and sample in caller_sv_dict[no_intersection_caller_5]:
							caller_1_genes = caller_sv_dict[caller_1][sample]
							caller_2_genes = caller_sv_dict[caller_2][sample]
							caller_3_genes = caller_sv_dict[caller_3][sample]
							no_intersection_caller_4_genes = caller_sv_dict[no_intersection_caller_4][sample]
							no_intersection_caller_5_genes = caller_sv_dict[no_intersection_caller_5][sample]
							caller_1_and_2_genes = caller_1_genes.intersection(caller_2_genes)
							caller_1_2_and_3_genes = caller_1_and_2_genes.intersection(caller_3_genes)
							sv_intersection_uniq = caller_1_2_and_3_genes-no_intersection_caller_4_genes-no_intersection_caller_5_genes
							combo_strain_intersection_dict[combo_name][sample] = sv_intersection_uniq

						else:

							if sample not in caller_sv_dict[caller_2]:
								no_variant_calls.add("No " + str(args.variant_type.lower()) + "s found in " + caller_2 + " for sample: " + sample)
							if sample not in caller_sv_dict[caller_3]:
								no_variant_calls.add("No " + str(args.variant_type.lower()) + "s found in " + caller_3 + " for sample: " + sample)
							if sample not in caller_sv_dict[no_intersection_caller_4]:
								no_variant_calls.add("No " + str(args.variant_type.lower()) + "s found in " + no_intersection_caller_4 + " for sample: " + sample)
							if sample not in caller_sv_dict[no_intersection_caller_5]:
								no_variant_calls.add("No " + str(args.variant_type.lower()) + "s found in " + no_intersection_caller_5 + " for sample: " + sample)

				if len(x) == 4:
					combo_name = ('-'.join(x))
					caller_1 = x[0]
					caller_2 = x[1]
					caller_3 = x[2]
					caller_4 = x[3]

					no_intersection_caller_list = list(caller_sv_dict.keys()) # Create a list to store callers that aren't in combination. Used to get non-intersection set.
					no_intersection_caller_list.remove(caller_1)
					no_intersection_caller_list.remove(caller_2)
					no_intersection_caller_list.remove(caller_3)
					no_intersection_caller_list.remove(caller_4)
					no_intersection_caller_5 = no_intersection_caller_list.pop()


					for sample in caller_sv_dict[caller_1].keys():
						if sample in caller_sv_dict[caller_2] and sample in caller_sv_dict[no_intersection_caller_3] and sample in caller_sv_dict[caller_4] and sample in caller_sv_dict[no_intersection_caller_5]:
							caller_1_genes = caller_sv_dict[caller_1][sample]
							caller_2_genes = caller_sv_dict[caller_2][sample]
							caller_3_genes = caller_sv_dict[caller_3][sample]
							caller_4_genes = caller_sv_dict[caller_4][sample]
							no_intersection_caller_5_genes = caller_sv_dict[no_intersection_caller_5][sample]
							caller_1_and_2_genes = caller_1_genes.intersection(caller_2_genes)
							caller_1_2_and_3_genes = caller_1_and_2_genes.intersection(caller_3_genes)
							caller_1_2_3_and_4_genes = caller_1_2_and_3_genes.intersection(caller_4_genes)
							sv_intersection_uniq = caller_1_2_3_and_4_genes-no_intersection_caller_5_genes
							combo_strain_intersection_dict[combo_name][sample] = sv_intersection_uniq

						else:

							if sample not in caller_sv_dict[caller_2]:
								no_variant_calls.add("No " + str(args.variant_type.lower()) + "s found in " + caller_2 + " for sample: " + sample)
							if sample not in caller_sv_dict[caller_3]:
								no_variant_calls.add("No " + str(args.variant_type.lower()) + "s found in " + caller_3 + " for sample: " + sample)
							if sample not in caller_sv_dict[caller_4]:
								no_variant_calls.add("No " + str(args.variant_type.lower()) + "s found in " + caller_4 + " for sample: " + sample)
							if sample not in caller_sv_dict[no_intersection_caller_5]:
								no_variant_calls.add("No " + str(args.variant_type.lower()) + "s found in " + no_intersection_caller_5 + " for sample: " + sample)


				if len(x) == 5:
					combo_name = ('-'.join(x))
					caller_1 = x[0]
					caller_2 = x[1]
					caller_3 = x[2]
					caller_4 = x[3]
					caller_5 = x[4]

					for sample in caller_sv_dict[caller_1].keys():
						if sample in caller_sv_dict[caller_2] and sample in caller_sv_dict[no_intersection_caller_3] and sample in caller_sv_dict[no_intersection_caller_4] and sample in caller_sv_dict[no_intersection_caller_5]:
							caller_1_genes = caller_sv_dict[caller_1][sample]
							caller_2_genes = caller_sv_dict[caller_2][sample]
							caller_3_genes = caller_sv_dict[caller_3][sample]
							caller_4_genes = caller_sv_dict[caller_4][sample]
							caller_5_genes = caller_sv_dict[caller_5][sample]

							caller_1_and_2_genes = caller_1_genes.intersection(caller_2_genes)
							caller_1_2_and_3_genes = caller_1_and_2_genes.intersection(caller_3_genes)
							caller_1_2_3_and_4_genes = caller_1_2_and_3_genes.intersection(caller_4_genes)
							caller_1_2_3_4_and_5_genes = caller_1_2_3_and_4_genes.intersection(caller_5_genes)
							sv_intersection_uniq = caller_1_2_3_4_and_5_genes
							combo_strain_intersection_dict[combo_name][sample] = sv_intersection_uniq

						else:

							if sample not in caller_sv_dict[caller_2]:
								no_variant_calls.add("No " + str(args.variant_type.lower()) + "s found in " + caller_2 + " for sample: " + sample)
							if sample not in caller_sv_dict[caller_3]:
								no_variant_calls.add("No " + str(args.variant_type.lower()) + "s found in " + caller_3 + " for sample: " + sample)
							if sample not in caller_sv_dict[caller_4]:
								no_variant_calls.add("No " + str(args.variant_type.lower()) + "s found in " + caller_4 + " for sample: " + sample)
							if sample not in caller_sv_dict[caller_5]:
								no_variant_calls.add("No " + str(args.variant_type.lower()) + "s found in " + caller_5 + " for sample: " + sample)


		if len(caller_sv_dict.keys()) == 4:
			for x in (list(combo)):
				if len(x) == 1:
					combo_name = x[0]
					caller_1 = x[0]

					no_intersection_caller_list = list(caller_sv_dict.keys()) # Create a list to store callers that aren't in combination. Used to get non-intersection set.
					no_intersection_caller_list.remove(caller_1)
					no_intersection_caller_2 = no_intersection_caller_list.pop()
					no_intersection_caller_3 = no_intersection_caller_list.pop()
					no_intersection_caller_4 = no_intersection_caller_list.pop()

					for sample in caller_sv_dict[caller_1].keys():
						if sample in caller_sv_dict[no_intersection_caller_2] and sample in caller_sv_dict[no_intersection_caller_3] and sample in caller_sv_dict[no_intersection_caller_4]:
							caller_1_genes = caller_sv_dict[caller_1][sample]
							no_intersection_caller_2_genes = caller_sv_dict[no_intersection_caller_2][sample]
							no_intersection_caller_3_genes = caller_sv_dict[no_intersection_caller_3][sample]
							no_intersection_caller_4_genes = caller_sv_dict[no_intersection_caller_4][sample]

							sv_intersection = caller_1_genes-no_intersection_caller_2_genes-no_intersection_caller_3_genes-no_intersection_caller_4_genes
							combo_strain_intersection_dict[combo_name][sample] = sv_intersection
						else:

							if sample not in caller_sv_dict[no_intersection_caller_2]:
								print(sample + " not in " + no_intersection_caller_2)
							if sample not in caller_sv_dict[no_intersection_caller_3]:
								no_variant_calls.add("No " + str(args.variant_type.lower()) + "s found in " + no_intersection_caller_3 + " for sample: " + sample)
							if sample not in caller_sv_dict[no_intersection_caller_4]:
								no_variant_calls.add("No " + str(args.variant_type.lower()) + "s found in " + no_intersection_caller_4 + " for sample: " + sample)

				if len(x) == 2:
					combo_name = ('-'.join(x))
					combo_name = combo_name
					caller_1 = x[0]
					caller_2 = x[1]

					no_intersection_caller_list = list(caller_sv_dict.keys()) # Create a list to store callers that aren't in combination. Used to get non-intersection set.
					no_intersection_caller_list.remove(caller_1)
					no_intersection_caller_list.remove(caller_2)
					no_intersection_caller_3 = no_intersection_caller_list.pop()
					no_intersection_caller_4 = no_intersection_caller_list.pop()

					for sample in caller_sv_dict[caller_1].keys():
						if sample in caller_sv_dict[caller_2] and sample in caller_sv_dict[no_intersection_caller_3] and sample in caller_sv_dict[no_intersection_caller_4]:
							caller_1_genes = caller_sv_dict[caller_1][sample]
							caller_2_genes = caller_sv_dict[caller_2][sample]
							no_intersection_caller_3_genes = caller_sv_dict[no_intersection_caller_3][sample]
							no_intersection_caller_4_genes = caller_sv_dict[no_intersection_caller_4][sample]
							caller_1_and_2_genes = caller_1_genes.intersection(caller_2_genes)
							sv_intersection= caller_1_and_2_genes-no_intersection_caller_3_genes-no_intersection_caller_4_genes
							combo_strain_intersection_dict[combo_name][sample] = sv_intersection

						else:

							if sample not in caller_sv_dict[caller_2]:
								no_variant_calls.add("No " + str(args.variant_type.lower()) + "s found in " + caller_2 + " for sample: " + sample)
							if sample not in caller_sv_dict[no_intersection_caller_3]:
								no_variant_calls.add("No " + str(args.variant_type.lower()) + "s found in " + no_intersection_caller_3 + " for sample: " + sample)
							if sample not in caller_sv_dict[no_intersection_caller_4]:
								no_variant_calls.add("No " + str(args.variant_type.lower()) + "s found in " + no_intersection_caller_4 + " for sample: " + sample)

				if len(x) == 3:
					combo_name = ('-'.join(x))
					combo_name = combo_name
					caller_1 = x[0]
					caller_2 = x[1]
					caller_3 = x[2]

					no_intersection_caller_list = list(caller_sv_dict.keys()) # Create a list to store callers that aren't in combination. Used to get non-intersection set.
					no_intersection_caller_list.remove(caller_1)
					no_intersection_caller_list.remove(caller_2)
					no_intersection_caller_list.remove(caller_3)
					no_intersection_caller_4 = no_intersection_caller_list.pop()

					for sample in caller_sv_dict[caller_1].keys():
						if sample in caller_sv_dict[caller_2] and sample in caller_sv_dict[caller_3] and sample in caller_sv_dict[no_intersection_caller_4]:
							caller_1_genes = caller_sv_dict[caller_1][sample]
							caller_2_genes = caller_sv_dict[caller_2][sample]
							caller_3_genes = caller_sv_dict[caller_3][sample]
							no_intersection_caller_4_genes = caller_sv_dict[no_intersection_caller_4][sample]
							caller_1_and_2_genes = caller_1_genes.intersection(caller_2_genes)
							caller_1_2_and_3_genes = caller_1_and_2_genes.intersection(caller_3_genes)
							sv_intersection = caller_1_2_and_3_genes-no_intersection_caller_4_genes
							combo_strain_intersection_dict[combo_name][sample] = sv_intersection
						else:

							if sample not in caller_sv_dict[caller_2]:
								no_variant_calls.add("No " + str(args.variant_type.lower()) + "s found in " + caller_2 + " for sample: " + sample)
							if sample not in caller_sv_dict[caller_3]:
								no_variant_calls.add("No " + str(args.variant_type.lower()) + "s found in " + caller_3 + " for sample: " + sample)
							if sample not in caller_sv_dict[no_intersection_caller_4]:
								no_variant_calls.add("No " + str(args.variant_type.lower()) + "s found in " + no_intersection_caller_4 + " for sample: " + sample)

				if len(x) == 4:
					combo_name = ('-'.join(x))
					combo_name = combo_name
					caller_1 = x[0]
					caller_2 = x[1]
					caller_3 = x[2]
					caller_4 = x[3]

					for sample in caller_sv_dict[caller_1].keys():
						if sample in caller_sv_dict[caller_2] and sample in caller_sv_dict[no_intersection_caller_3] and sample in caller_sv_dict[caller_4]:
							caller_1_genes = caller_sv_dict[caller_1][sample]
							caller_2_genes = caller_sv_dict[caller_2][sample]
							caller_3_genes = caller_sv_dict[caller_3][sample]
							caller_4_genes = caller_sv_dict[caller_4][sample]
							caller_1_and_2_genes = caller_1_genes.intersection(caller_2_genes)
							caller_1_2_and_3_genes = caller_1_and_2_genes.intersection(caller_3_genes)
							caller_1_2_3_and_4_genes = caller_1_2_and_3_genes.intersection(caller_4_genes)
							sv_intersection = caller_1_2_3_and_4_genes
							combo_strain_intersection_dict[combo_name][sample] = sv_intersection
						else:

							if sample not in caller_sv_dict[caller_2]:
								no_variant_calls.add("No " + str(args.variant_type.lower()) + "s found in " + caller_2 + " for sample: " + sample)
							if sample not in caller_sv_dict[caller_3]:
								no_variant_calls.add("No " + str(args.variant_type.lower()) + "s found in " + caller_3 + " for sample: " + sample)
							if sample not in caller_sv_dict[caller_4]:
								no_variant_calls.add("No " + str(args.variant_type.lower()) + "s found in " + caller_4 + " for sample: " + sample)


		if len(caller_sv_dict.keys()) == 3:
			for x in (list(combo)):
				if len(x) == 1:
					combo_name = (x)
					combo_name = combo_name
					caller_1 = x[0]

					no_intersection_caller_list = list(caller_sv_dict.keys()) # Create a list to store callers that aren't in combination. Used to get non-intersection set.
					no_intersection_caller_list.remove(caller_1)
					no_intersection_caller_2 = no_intersection_caller_list.pop()
					no_intersection_caller_3 = no_intersection_caller_list.pop()

					for sample in caller_sv_dict[caller_1].keys():
						if sample in caller_sv_dict[no_intersection_caller_2] and sample in caller_sv_dict[no_intersection_caller_3]:
							caller_1_genes = caller_sv_dict[caller_1][sample]
							no_intersection_caller_2_genes = caller_sv_dict[no_intersection_caller_2][sample]
							no_intersection_caller_3_genes = caller_sv_dict[no_intersection_caller_3][sample]

							sv_intersection = caller_1_genes-no_intersection_caller_2_genes-no_intersection_caller_3_genes
							combo_strain_intersection_dict[combo_name][sample] = sv_intersection
						else:
							caller_1_genes = caller_sv_dict[caller_1][sample]
							if sample not in caller_sv_dict[no_intersection_caller_2]:
								print(sample + " not in " + no_intersection_caller_2 + " (no_intersection_caller_2)")
								if sample not in caller_sv_dict[no_intersection_caller_3]:
									print(sample + " not in " + no_intersection_caller_3 + " (no_intersection_caller_3)")
									sv_intersection = caller_1_genes
									combo_strain_intersection_dict[combo_name][sample] = sv_intersection
								else:
									no_intersection_caller_3_genes = caller_sv_dict[no_intersection_caller_3][sample]
									sv_intersection = caller_1_genes-no_intersection_caller_3_genes
							if sample not in caller_sv_dict[no_intersection_caller_3]:
								no_intersection_caller_2_genes = caller_sv_dict[no_intersection_caller_2][sample]
								print(sample + " not in " + no_intersection_caller_3 + " (no_intersection_caller_3)")
								sv_intersection = caller_1_genes-no_intersection_caller_2_genes
							combo_strain_intersection_dict[combo_name][sample] = sv_intersection

				if len(x) == 2:
					combo_name = ('-'.join(x))
					combo_name = combo_name
					caller_1 = x[0]
					caller_2 = x[1]

					no_intersection_caller_list = list(caller_sv_dict.keys()) # Create a list to store callers that aren't in combination. Used to get non-intersection set.
					no_intersection_caller_list.remove(caller_1)
					no_intersection_caller_list.remove(caller_2)
					no_intersection_caller_3 = no_intersection_caller_list.pop()

					for sample in caller_sv_dict[caller_1].keys():
						if sample in caller_sv_dict[caller_2] and sample in caller_sv_dict[no_intersection_caller_3]:
							caller_1_genes = caller_sv_dict[caller_1][sample]
							caller_2_genes = caller_sv_dict[caller_2][sample]
							no_intersection_caller_3_genes = caller_sv_dict[no_intersection_caller_3][sample]
							caller_1_and_2_genes = caller_1_genes.intersection(caller_2_genes)
							sv_intersection= caller_1_and_2_genes-no_intersection_caller_3_genes
							combo_strain_intersection_dict[combo_name][sample] = sv_intersection
						else:
							caller_1_genes = caller_sv_dict[caller_1][sample]
							if sample not in caller_sv_dict[caller_2]:
								print(sample + " not in " + caller_2 + " (caller_2)")
								if sample not in caller_sv_dict[no_intersection_caller_3]:
									print(sample + " not in " + no_intersection_caller_3 + " (no_intersection_caller_3)")
									sv_intersection= caller_1_genes
								else:
									no_intersection_caller_3_genes = caller_sv_dict[no_intersection_caller_3][sample]
									sv_intersection= caller_1_genes-no_intersection_caller_3_genes

							if sample not in caller_sv_dict[no_intersection_caller_3]:
								print(sample + " not in " + no_intersection_caller_3 + " (no_intersection_caller_3)")
								caller_2_genes = caller_sv_dict[caller_2][sample]
								caller_1_and_2_genes = caller_1_genes.intersection(caller_2_genes)
								sv_intersection= caller_1_and_2_genes
							combo_strain_intersection_dict[combo_name][sample] = sv_intersection

				if len(x) == 3:
					combo_name = ('-'.join(x))
					combo_name = combo_name
					caller_1 = x[0]
					caller_2 = x[1]
					caller_3 = x[2]

					for sample in caller_sv_dict[caller_1].keys():
						if sample in caller_sv_dict[caller_2] and sample in caller_sv_dict[caller_3]:
							caller_1_genes = caller_sv_dict[caller_1][sample]
							caller_2_genes = caller_sv_dict[caller_2][sample]
							caller_3_genes = caller_sv_dict[caller_3][sample]
							caller_1_and_2_genes = caller_1_genes.intersection(caller_2_genes)
							caller_1_2_and_3_genes = caller_1_and_2_genes.intersection(caller_3_genes)
							sv_intersection = caller_1_2_and_3_genes
							combo_strain_intersection_dict[combo_name][sample] = sv_intersection
						else:
							caller_1_genes = caller_sv_dict[caller_1][sample]
							if sample not in caller_sv_dict[caller_2]:
								print(sample + " not in " + caller_2 + " (caller_2)")
								if sample not in caller_sv_dict[caller_3]:
									print(sample + " not in " + caller_3 + " (caller_3)")
									sv_intersection = caller_1_genes
								else:
									caller_3_genes = caller_sv_dict[caller_3][sample]
									caller_1_and_3_genes = caller_1_genes.intersection(caller_3_genes)
									sv_intersection = caller_1_and_3_genes

							if sample not in caller_sv_dict[caller_3]:
								caller_2_genes = caller_sv_dict[caller_2][sample]
								print(sample + " not in " + caller_3 + " (caller_3)")
								caller_1_and_2_genes = caller_1_genes.intersection(caller_2_genes)
								sv_intersection = caller_1_and_2_genes
							combo_strain_intersection_dict[combo_name][sample] = sv_intersection

		if len(caller_sv_dict.keys()) == 2:
			for x in (list(combo)):
				if len(x) == 1:
					combo_name = x[0]
					caller_1 = x[0]

					no_intersection_caller_list = list(caller_sv_dict.keys()) # Create a list to store callers that aren't in combination. Used to get non-intersection set.
					no_intersection_caller_list.remove(caller_1)
					no_intersection_caller_2 = no_intersection_caller_list.pop()


					for sample in caller_sv_dict[caller_1].keys():
						if sample in caller_sv_dict[no_intersection_caller_2]:
							caller_1_genes = caller_sv_dict[caller_1][sample]
							no_intersection_caller_2_genes = caller_sv_dict[no_intersection_caller_2][sample]

							sv_intersection = caller_1_genes-no_intersection_caller_2_genes
							combo_strain_intersection_dict[combo_name][sample] = sv_intersection
						else:

							if sample not in caller_sv_dict[no_intersection_caller_2]:
								print(sample + " not in " + no_intersection_caller_2)

				if len(x) == 2:
					combo_name = ('-'.join(x))
					combo_name = combo_name
					caller_1 = x[0]
					caller_2 = x[1]

					for sample in caller_sv_dict[caller_1].keys():
						if sample in caller_sv_dict[caller_2] :
							caller_1_genes = caller_sv_dict[caller_1][sample]
							caller_2_genes = caller_sv_dict[caller_2][sample]
							caller_1_and_2_genes = caller_1_genes.intersection(caller_2_genes)
							sv_intersection= caller_1_and_2_genes
							combo_strain_intersection_dict[combo_name][sample] = sv_intersection
						else:

							if sample not in caller_sv_dict[caller_2]:
								no_variant_calls.add("No " + str(args.variant_type.lower()) + "s found in " + caller_2 + " for sample: " + sample)

	for x in no_variant_calls:
		print(x)
	return(combo_strain_intersection_dict)

def write_intersections(combo_strain_intersection_dict, outdir):

	for combo in combo_strain_intersection_dict.keys():
		combo_name = combo
		if "-" in combo:
			combo_length = len(combo.split("-"))

		else:
			combo_length = 1

		outputdir = outdir + "/intersections/" + str(combo_length) + "-callers/" + combo_name
		if not os.path.exists(outputdir): # Check if parent directory exists
			os.makedirs(outputdir)
		intersection_count = 0 # variable to store the sum of interesecting sv calls for all samples
		outfile = outputdir + "/count_by_strain.txt"

		with open(outfile, 'w', newline='\n') as f:
			for sample in combo_strain_intersection_dict[combo].keys():
				strain_intersection_size = len(combo_strain_intersection_dict[combo][sample])
				intersection_count = intersection_count + strain_intersection_size
				combo_strain_intersection_value = sample + ": " + str(strain_intersection_size)

				f.write(combo_strain_intersection_value + "\n")
			total_intersection_line = "Sum of all strain intersections: " + str(intersection_count) + "\n"
			f.write(total_intersection_line)

		outputdir = outputdir + "/strains"
		if not os.path.exists(outputdir): # Check if parent directory exists
			os.makedirs(outputdir)

		for sample in combo_strain_intersection_dict[combo].keys():
			outfile = outputdir + "/" + sample + ".txt"

			with open(outfile, 'w', newline='\n') as f:
				for gene in combo_strain_intersection_dict[combo][sample]:
					f.write(gene + "\n")

		outputdir = outdir + "/intersections/"
		if not os.path.exists(outputdir): # Check if parent directory exists
			os.makedirs(outputdir)

	outfile = outdir + "/all_caller_combinations_genes.csv" # Create csv to write all combinations to

	with open(outfile, 'w', newline='\n') as f:
		for combo in combo_strain_intersection_dict.keys():
			if "-" in combo:
				combo_name = combo
			else:
				combo_name = combo

			intersection_total = 0 # variable to store the sum of interesecting sv calls for all samples

			for sample in combo_strain_intersection_dict[combo].keys():
				intersection_total = intersection_total + len(combo_strain_intersection_dict[combo][sample])

			total_intersection_line = combo_name + "," + str(intersection_total) + "\n"
			f.write(total_intersection_line)


if args.variant_type.lower() =="deletion" or args.variant_type.lower() =="deletions":
	print("Analyzing deletions")
	caller_deletion_dict = get_deletion_inversion_paths_filenames("DELETION") # Get a dict with a key for each caller and values for the caller bed dirs and variant names
	caller_list = []
	total_call_dict = defaultdict() # Dict to store total number of sv calls for each caller (sum of all samples)
	total_gene_dict = defaultdict() # Dict to store total number of genes spanned by sv calls for each caller (sum of all samples)

	for caller in caller_deletion_dict.keys(): # Get the different callers and total number of deletions they called
		caller_list.append(caller)
		caller_total_calls = get_caller_stats(caller, caller_deletion_dict, samples, "deletion")
		caller_total_genes = get_caller_gene_stats(caller, caller_deletion_dict, samples, "deletion")
		total_call_dict[caller] = caller_total_calls
		total_gene_dict[caller] = caller_total_genes

	output_dir = config["output"]["DEL_OUTDIR"]
	output_dir = output_dir + "caller_stats/"
	if not os.path.exists(output_dir): # Check if parent directory exists
		os.makedirs(output_dir)
	outfile = output_dir + "total_calls_each_caller.txt"

	with open(outfile, 'w', newline='\n') as f:
		print("Writing to: " + outfile)
		for caller in total_call_dict.keys():
			f.write(caller + ": " + str(total_call_dict[caller]) + "\n")

	outfile = output_dir + "total_genes_each_caller.txt"

	with open(outfile, 'w', newline='\n') as f:
		print("Writing to: " + outfile)
		for caller in total_gene_dict.keys():
			f.write(caller + ": " + str(total_call_dict[caller]) + "\n")

	caller_sv_dict = get_caller_svs(caller_deletion_dict, caller_list, samples)

	combo_strain_intersection_dict = get_caller_intersections(caller_sv_dict)
	output_dir = config["output"]["DEL_OUTDIR"]

	write_intersections(combo_strain_intersection_dict, output_dir)

if args.variant_type.lower() =="inversion" or args.variant_type.lower() =="inversions":
	print("Analyzing inversions")
	caller_inversion_dict = get_deletion_inversion_paths_filenames("INVERSION") # Get a dict with a key for each caller and values for the caller bed dirs and variant names
	caller_list = []
	total_call_dict = defaultdict() # Dict to store total number of sv calls for each caller (sum of all samples)
	total_gene_dict = defaultdict() # Dict to store total number of genes spanned by sv calls for each caller (sum of all samples)

	for caller in caller_inversion_dict.keys(): # Get the different callers and total number of inversions they called
		caller_list.append(caller)
		caller_total_calls = get_caller_stats(caller, caller_inversion_dict, samples, "inversion")
		caller_total_genes = get_caller_gene_stats(caller, caller_inversion_dict, samples, "inversion")
		total_call_dict[caller] = caller_total_calls
		total_gene_dict[caller] = caller_total_genes

	output_dir = config["output"]["INV_OUTDIR"]
	output_dir = output_dir + "caller_stats/"
	if not os.path.exists(output_dir): # Check if parent directory exists
		os.makedirs(output_dir)
	outfile = output_dir + "total_calls_each_caller.txt"

	with open(outfile, 'w', newline='\n') as f:
		print("Writing to: " + outfile)
		for caller in total_call_dict.keys():
			f.write(caller + ": " + str(total_call_dict[caller]) + "\n")

	outfile = output_dir + "total_genes_each_caller.txt"

	with open(outfile, 'w', newline='\n') as f:
		print("Writing to: " + outfile)
		for caller in total_gene_dict.keys():
			f.write(caller + ": " + str(total_call_dict[caller]) + "\n")

	caller_sv_dict = get_caller_svs(caller_inversion_dict, caller_list, samples)
	combo_strain_intersection_dict = get_caller_intersections(caller_sv_dict)
	output_dir = config["output"]["INV_OUTDIR"]

	write_intersections(combo_strain_intersection_dict, output_dir)

if args.variant_type.lower() =="duplication" or args.variant_type.lower() =="duplications":
	print("Analyzing duplications")
	caller_duplication_dict = get_duplication_paths_filenames() # Get a dict with a key for each caller and values for the caller bed dirs and variant names

	duplication_caller_list = []
	duplication_total_call_dict = defaultdict() # Dict to store total number of sv calls for each caller (sum of all samples)
	duplication_total_gene_dict = defaultdict() # Dict to store total number of genes spanned by sv calls for each caller (sum of all samples)

	for caller in caller_duplication_dict.keys(): # Get the different callers and total number of duplications they called
		duplication_caller_list.append(caller)
		duplication_caller_total_calls = get_caller_stats(caller, caller_duplication_dict, samples, "duplication")
		duplication_caller_total_genes = get_caller_gene_stats(caller, caller_duplication_dict, samples, "duplication")
		duplication_total_call_dict[caller] = duplication_caller_total_calls
		duplication_total_gene_dict[caller] = duplication_caller_total_genes

	output_dir = config["output"]["DUP_OUTDIR"]
	output_dir = output_dir + "caller_stats/"
	if not os.path.exists(output_dir): # Check if parent directory exists
		os.makedirs(output_dir)
	outfile = output_dir + "total_calls_each_caller.txt"

	with open(outfile, 'w', newline='\n') as f:
		print("Writing to: " + outfile)
		for caller in duplication_total_call_dict.keys():
			f.write(caller + ": " + str(duplication_total_call_dict[caller]) + "\n")

	outfile = output_dir + "total_genes_each_caller.txt"

	with open(outfile, 'w', newline='\n') as f:
		print("Writing to: " + outfile)
		for caller in duplication_total_gene_dict.keys():
			f.write(caller + ": " + str(duplication_total_call_dict[caller]) + "\n")

	duplication_caller_sv_dict = get_caller_svs(caller_duplication_dict, duplication_caller_list, samples)
	duplication_combo_strain_intersection_dict = get_caller_intersections(duplication_caller_sv_dict)
	output_dir = config["output"]["DUP_OUTDIR"]

	write_intersections(duplication_combo_strain_intersection_dict, output_dir)
