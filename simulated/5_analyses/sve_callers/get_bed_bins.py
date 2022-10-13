import argparse
import os
import re
import sys
import numpy as np
import collections
import csv
from itertools import compress

parser = argparse.ArgumentParser()
parser.add_argument("input_file", help="SVE bed directory.")
parser.add_argument("prefix", help="Variant prefix to be added to bed file")
parser.add_argument("type", help="Variant type")
args = parser.parse_args()

DEL_BIN_LABELS = ["100-400bp","400-600bp","600-950bp","950-1.2Kbp","1.2K-1.5Kbp","1.5K-1.9Kbp","1.9K-2.2Kbp","2.2K-2.9Kbp","2.9K-3.6Kbp","3.6K-4.8Kbp","4.8K-6.1Kbp","6.1K-9Kbp","9K-18.5Kbp","18.5K-100Kbp","100K-1Mbp","1Mbp+"]
DUP_BIN_LABELS = ["100-1Kbp","1K-10Kbp","10K-50Kbp","50K-100Kbp","100K-250Kbp","250K-500Kbp","500K-1Mbp","1Mbp+"]
INV_BIN_LABELS = ["100-2500bp","2500-3500bp","3500-45Kbp","45K-80Kbp","80K-115Kbp","115K-180Kbp","180K-260Kbp","260K-300Kbp","300K-375Kbp","375K-500Kbp","500K-1Mbp","1Mbp+"]

DEL_BINS = [100,400,600,950,1200, 1500, 1900, 2200, 2900, 3600, 4800, 6100, 9000, 18500, 100000,1000000,21000000]
DUP_BINS = [100,1000,10000,50000,100000,250000,500000,1000000,21000000]
INV_BINS = [100,2500,3500,45000,80000,115000,180000,260000,300000,375000,500000,1000000,21000000]

def make_variant_dict(bed_lines,prefix, variant_type):
	variant_sizes = []
	variant_dict = collections.defaultdict(list)

	for variant in bed_lines:
		variant_chr = variant[0]
		variant_start = int(variant[1])
		variant_end = int(variant[2])
		variant_size = variant_end - variant_start
		variant_sizes.append(variant_size)

		variant_bed_line = variant[0:3] # Line for the bed file
		if variant_type == "DEL":
			var_hist = np.histogram(variant_size,DEL_BINS)
			var_hist_truth = var_hist[0] == 1
			var_bin_name = str(list(compress(DEL_BIN_LABELS, var_hist_truth)))
			var_bin_name = var_bin_name.strip("[']")
			new_var_name = prefix + "-" + var_bin_name
			variant_bed_line.append(new_var_name)
			variant_dict[var_bin_name].append(variant_bed_line)

		elif variant_type == "DUP":
			var_hist = np.histogram(variant_size,DUP_BINS)
			var_hist_truth = var_hist[0] == 1
			var_bin_name = str(list(compress(DUP_BIN_LABELS, var_hist_truth)))
			var_bin_name = var_bin_name.strip("[']")
			new_var_name = prefix + "-" + var_bin_name
			variant_bed_line.append(new_var_name)
			variant_dict[var_bin_name].append(variant_bed_line)

		elif variant_type == "INV":
			var_hist = np.histogram(variant_size,INV_BINS)
			var_hist_truth = var_hist[0] == 1
			var_bin_name = str(list(compress(INV_BIN_LABELS, var_hist_truth)))
			var_bin_name = var_bin_name.strip("[']")
			new_var_name = prefix + "-" + var_bin_name
			variant_bed_line.append(new_var_name)
			variant_dict[var_bin_name].append(variant_bed_line)

	var_bin_counts = np.histogram(np.array(variant_sizes),DEL_BINS)
	var_bin_total_bp = np.histogram(np.array(variant_sizes),DEL_BINS, weights=np.array(variant_sizes))
	var_data = (variant_dict,var_bin_counts,var_bin_total_bp)

	return (var_data)

def parse_bed(bed_file):
	bed_lines = []
	with open(bed_file) as f:
		read_data = f.readlines()
		for line in read_data:
			line_split = re.split(r'\t+', line)[0:3]
			bed_lines.append(line_split)
	return bed_lines

def write_bed(variant_dict, bedfile):
	variant_lines =[]
	for key in variant_dict:
		for line in variant_dict[key]:
			variant_lines.append(line)
	variant_lines.sort()
	with open(bedfile, 'w', newline='') as f_output:
		tsv_output = csv.writer(f_output, delimiter='\t')
		tsv_output.writerows(variant_lines)

# Main Code
bed_lines = parse_bed(args.input_file)
variant_data = make_variant_dict(bed_lines,args.prefix,args.type)
new_variant_file = args.input_file.rsplit(".",1)[0] + "_renamed.bed"

write_bed(variant_data[0], new_variant_file)
