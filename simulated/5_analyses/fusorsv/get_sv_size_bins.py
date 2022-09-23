# Script reads vcf files writes to bed files based on FusorSV size bin membership
import argparse
import os
import re
import sys
import numpy as np
import collections
import csv
from itertools import compress

parser = argparse.ArgumentParser()
parser.add_argument("input_dir", help="Fusor vcf directory.")
args = parser.parse_args()

# Names for each FusorSV size bin
DEL_BIN_LABELS = ["1-50bp","50-100bp","100-400bp","400-600bp","600-950bp","950-1.2Kbp","1.2K-1.5Kbp","1.5K-1.9Kbp","1.9K-2.2Kbp","2.2K-2.9Kbp","2.9K-3.6Kbp","3.6K-4.8Kbp","4.8K-6.1Kbp","6.1K-9Kbp","9K-18.5Kbp","18.5K-100Kbp","100K-1Mbp"]
DUP_BIN_LABELS = ["1-50bp","50-1Kbp","1K-10Kbp","10K-50Kbp","50K-100Kbp","100K-250Kbp","250K-500Kbp","500K-1Mbp"]
INV_BIN_LABELS = ["1-50bp","50-2500bp","2500-3500bp","3500-45Kbp","45K-80Kbp","80K-115Kbp","115K-180Kbp","180K-260Kbp","260K-300Kbp","300K-375Kbp","375K-500Kbp","500K-1Mbp"]

# FusorSV Size bins
DEL_BINS = [1,50,100,400,600,950,1200, 1500, 1900, 2200, 2900, 3600, 4800, 6100, 9000, 18500, 100000,1000000]
DUP_BINS = [1,50,1000,10000,50000,100000,250000,500000,1000000]
INV_BINS = [1,50,2500,3500,45000,80000,115000,180000,260000,300000,375000,500000,1000000]

# Read vcf file and, for each sv call, extract the chromosome, coordinates, name, type, and size
def process_truth(truth_file):
	with open(truth_file) as f:
		read_data = f.readlines()
		vcf_lines = []

		for line in read_data:
			if line[0] != "#": # If not preceded by a #, then it should be a line describing a variant
				try:
					line_split = re.split(r'\t+', line)[0:8] # split line by tabs and extract the parts with desired information
					chromosome = line_split[0]
					start_coord = line_split[1]
					variant_name = line_split[2]
					variant_type = line_split[4]
					variant_info = line_split[7]
					variant_info_split = re.split(r';', variant_info)[0:8]
					end_coord = variant_info_split[5].split("=")[1]
					variant_size = int(end_coord) - int(start_coord)
					vcf_line = [chromosome,start_coord,end_coord, variant_name,variant_type, variant_size]
					vcf_lines.append(vcf_line)

				except:
					print("Unexpected error:", sys.exc_info()[0])
					print("Error occurred for vcf file: " + str(truth_file))

	return (vcf_lines)

# Read vcf file and, for each sv call, extract the chromosome, coordinates, name, type, and size
def process_fusor_calls(fusor_file):
	with open(fusor_file) as f:
		read_data = f.readlines()
		vcf_lines = []

		for line in read_data:
			if line[0] != "#": # If not preceded by a #, then it should be a line describing a variant
				try:
					line_split = re.split(r'\t+', line)[0:8] # split line by tabs and extract the parts with desired information
					chromosome = line_split[0]
					start_coord = line_split[1]
					variant_name = line_split[2]
					variant_type = line_split[4]
					variant_info = line_split[7]
					variant_info_split = re.split(r';', variant_info)[0:8]
					end_coord = variant_info_split[2].split("=")[1]
					variant_size = int(end_coord) - int(start_coord)
					vcf_line = [chromosome,start_coord,end_coord, variant_name,variant_type, variant_size]
					vcf_lines.append(vcf_line)

				except:
					print("Unexpected error:", sys.exc_info()[0])
					print("Error occurred for vcf file: " + str(truth_file))

	return (vcf_lines)

# Go through the provided directory and find vcf files
def find_vcfs(input_dir):
	for file in os.listdir(input_dir):
		if file.endswith("S-1.vcf"): # FusorSV vcf file
			fusor_file=(os.path.join(input_dir, file))
			fusor_data = process_fusor_calls(fusor_file)
		elif file.endswith("S0.vcf"): # Truth vcf file
			truth_file=(os.path.join(input_dir, file))
			truth_data = process_truth(truth_file)
	return (fusor_data,truth_data)

# Function takes a list of sv calls and
def make_variant_dict(vcf_lines):
	del_sizes = []
	del_dict = collections.defaultdict(list)
	dup_sizes = []
	dup_dict = collections.defaultdict(list)
	inv_sizes = []
	inv_dict = collections.defaultdict(list)

	for variant in vcf_lines:
		variant_name = variant[3]

		if "SVSIM" in variant_name: # svsim variant names have the size in the title. Remove the size.
			variant_name = variant_name.rpartition("_")[0]

		variant_type = variant[4].strip("<>")
		variant_size = int(variant[5])

		if variant_type == "DEL":
			del_bed_line = variant[0:4] # Line for the bed file
			del_sizes.append(variant_size)
			deletion_size = [variant_size]
			del_hist = np.histogram(deletion_size,DEL_BINS) # Use numpy to determine which FusorSV size bin the variant is in
			del_hist_truth = del_hist[0] == 1 # Convert the bin membership to boolean
			deletion_bin_name = str(list(compress(DEL_BIN_LABELS, del_hist_truth))) # Get string for variant size bin
			deletion_bin_name = deletion_bin_name.strip("[']")
			new_deletion_name = variant_name + "-" + deletion_bin_name # Rename the variant name with the variant size bin suffix
			del_bed_line[3] = new_deletion_name
			del_dict[deletion_bin_name].append(del_bed_line) # Add the line to a dict with the variant name as the key

		elif variant_type == "DUP":

			dup_bed_line = variant[0:4] # Line for the bed file
			dup_sizes.append(variant_size)
			duplication_size = [variant_size]
			dup_hist = np.histogram(duplication_size,DUP_BINS) # Use numpy to determine which FusorSV size bin the variant is in
			dup_hist_truth = dup_hist[0] == 1 # Convert the bin membership to boolean
			duplication_bin_name = str(list(compress(DUP_BIN_LABELS, dup_hist_truth))) # Get string for variant size bin
			duplication_bin_name = duplication_bin_name.strip("[']")
			new_duplication_name = variant_name + "-" + duplication_bin_name # Rename the variant name with the variant size bin suffix
			dup_bed_line[3] = new_duplication_name
			dup_dict[duplication_bin_name].append(dup_bed_line) # Add the line to a dict with the variant name as the key

		if variant_type == "INV":

			inv_bed_line = variant[0:4] # Line for the bed file
			inv_sizes.append(variant_size)
			inversion_size = [variant_size]
			inv_hist = np.histogram(inversion_size,INV_BINS) # Use numpy to determine which FusorSV size bin the variant is in
			inv_hist_truth = inv_hist[0] == 1 # Convert the bin membership to boolean
			inversion_bin_name = str(list(compress(INV_BIN_LABELS, inv_hist_truth))) # Get string for variant size bin
			inversion_bin_name = inversion_bin_name.strip("[']")
			new_inversion_name = variant_name + "-" + inversion_bin_name # Rename the variant name with the variant size bin suffix
			inv_bed_line[3] = new_inversion_name
			inv_dict[inversion_bin_name].append(inv_bed_line) # Add the line to a dict with the variant name as the key

	del_bin_counts = np.histogram(np.array(del_sizes),DEL_BINS) # Get the number of variants in each FusorSV size bin
	del_bin_total_bp = np.histogram(np.array(del_sizes),DEL_BINS, weights=np.array(del_sizes)) # Get the number of base pairs in each FusorSV size bin
	deletion_data = (del_dict,del_bin_counts,del_bin_total_bp)

	dup_bin_counts = np.histogram(np.array(dup_sizes),DUP_BINS) # Get the number of variants in each FusorSV size bin
	dup_bin_total_bp = np.histogram(np.array(dup_sizes),DUP_BINS, weights=np.array(dup_sizes)) # Get the number of base pairs in each FusorSV size bin
	duplication_data = (dup_dict,dup_bin_counts,dup_bin_total_bp)

	inv_bin_counts = np.histogram(np.array(inv_sizes),INV_BINS) # Get the number of variants in each FusorSV size bin
	inv_bin_total_bp = np.histogram(np.array(inv_sizes),INV_BINS, weights=np.array(inv_sizes)) # Get the number of base pairs in each FusorSV size bin
	inversion_data = (inv_dict,inv_bin_counts,inv_bin_total_bp)

	return (deletion_data,duplication_data,inversion_data)

# Writes the sv calls (from vcf file) as separate bed file for each size bin
def write_separate_beds(variant_dict, output_dir,file_prefix):
	if not os.path.exists(output_dir):
		try:
		    os.makedirs(output_dir)
		except OSError:
		    print ("Creation of the directory %s failed" % output_dir)

	for key in variant_dict:
		bedfile = output_dir + file_prefix + key + ".bed"

		with open(bedfile, 'w', newline='') as f_output:
			tsv_output = csv.writer(f_output, delimiter='\t')
			tsv_output.writerows(variant_dict[key])

# Writes the sv calls (from vcf file) to bed file
def write_bed(variant_dict, output_dir,file_prefix):
	if not os.path.exists(output_dir):
		try:
		    os.makedirs(output_dir)
		except OSError:
		    print ("Creation of the directory %s failed" % output_dir)

	bedfile = output_dir + file_prefix + ".bed"
	variant_lines =[]

	for key in variant_dict:
		for line in variant_dict[key]:
			variant_lines.append(line)
	with open(bedfile, 'w', newline='') as f_output:
		tsv_output = csv.writer(f_output, delimiter='\t')
		tsv_output.writerows(variant_lines)

# Summarize results and write to disk
def write_summary(variant_counts, variant_total_bp, output_dir,file_prefix):
	if not os.path.exists(output_dir):
		try:
		    os.makedirs(output_dir)
		except OSError:
		    print ("Creation of the directory %s failed" % output_dir)

	count_file = output_dir + file_prefix + ".counts"
	total_bp_file = output_dir + file_prefix + ".bases"

	with open(count_file, 'w', newline='') as f_output:
		csv_output = csv.writer(f_output, delimiter=',')
		csv_output.writerow(variant_counts)

	with open(total_bp_file, 'w', newline='') as f_output:
		csv_output = csv.writer(f_output, delimiter=',')
		csv_output.writerow(variant_total_bp)

vcf_data = find_vcfs(args.input_dir) # Find vcf files in the provided directory and imports the vcf lines containing sv calls. Returns a tuple with the sv calls for fusorsv and truth
fusor_data = vcf_data[0]
truth_data = vcf_data[1]

fusor_data_processed = make_variant_dict(fusor_data)
fusor_deletions = fusor_data_processed[0]
fusor_duplications = fusor_data_processed[1]
fusor_inversions = fusor_data_processed[2]

truth_data_processed = make_variant_dict(truth_data)
truth_deletions = truth_data_processed[0]
truth_duplications = truth_data_processed[1]
truth_inversions = truth_data_processed[2]

# Results will be stored as bedfiles in the following dirs
bed_output_dir = os.path.abspath(args.input_dir) + "/bedfiles/"
deletion_output_dir = os.path.abspath(args.input_dir) + "/bedfiles/deletions/"
duplication_output_dir = os.path.abspath(args.input_dir) + "/bedfiles/duplications/"
inversion_output_dir = os.path.abspath(args.input_dir) + "/bedfiles/inversions/"

# Write bed files for fusorsv vcf files
write_separate_beds(fusor_deletions[0], deletion_output_dir,"fusor_del_") # Write sv calls to a separate bed file for each size bin
write_bed(fusor_deletions[0], bed_output_dir,"fusor_deletions") # Write sv calls to a bed file

write_separate_beds(fusor_duplications[0], duplication_output_dir,"fusor_dup_") # Write sv calls to a separate bed file for each size bin
write_bed(fusor_duplications[0], bed_output_dir,"fusor_duplications") # Write sv calls to a bed file
write_separate_beds(fusor_inversions[0], inversion_output_dir,"fusor_inv_") # Write sv calls to a separate bed file for each size bin
write_bed(fusor_inversions[0], bed_output_dir,"fusor_inversions") # Write sv calls to a bed file

# Write bed files for truth vcf files
write_separate_beds(truth_deletions[0], deletion_output_dir,"truth_del_") # Write sv calls to a separate bed file for each size bin
write_bed(truth_deletions[0], bed_output_dir,"truth_deletions") # Write sv calls to a bed file
write_separate_beds(truth_duplications[0], duplication_output_dir,"truth_dup_") # Write sv calls to a separate bed file for each size bin
write_bed(truth_duplications[0], bed_output_dir,"truth_duplications") # Write sv calls to a bed file
write_separate_beds(truth_inversions[0], inversion_output_dir,"truth_inv_") # Write sv calls to a separate bed file for each size bin
write_bed(truth_inversions[0], bed_output_dir,"truth_inversions") # Write sv calls to a bed file

# Summarize results and write to disk
summary_output_dir = os.path.abspath(args.input_dir) + "/summary/"
write_summary(fusor_deletions[1][0],fusor_deletions[2][0], summary_output_dir,"fusor_deletions")
write_summary(truth_deletions[1][0],truth_deletions[2][0], summary_output_dir,"truth_deletions")
