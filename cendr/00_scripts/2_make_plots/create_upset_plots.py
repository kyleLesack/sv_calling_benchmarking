import configparser
import argparse
import os
import csv
from os import path
from pathlib import Path
from collections import defaultdict
#from collections import namedtuple
import pandas as pd
from matplotlib import pyplot as plt
from upsetplot import generate_counts, plot, UpSet


config = configparser.ConfigParser()
parser = argparse.ArgumentParser()
parser.add_argument("input_config", help="config file for the variant caller paths, filenames, etc.")
parser.add_argument("maximum_size", help="maximum variant size")
parser.add_argument("variant_type", help="variant type to be analyzed")
parser.add_argument("--max_combos", dest='max_combos',nargs='?',type=int,help="Maximum number of combos in the plot")
parser.add_argument("--min_degree", dest='min_degree',nargs='?', type=int, help="Combo minimum number of callers")
parser.add_argument('--subtitle', action='store_true')

args = parser.parse_args()

config.read(args.input_config) # Open configuration file

sv_callers = config["variant_callers"]["CALLERS"].split()
caller_shorthand_dict  = {"assemblytics_mummer4_canu":"assemblytics",  "mumandco_v3": "mumandco", "pbsv_pbmm2":"pbsv", "sniffles_ngmlr":"sniffles", "svim_ngmlr":"svim"} # Dictionary used to rename callers using shorter name and without assembler

# Open csv file with combinations for upset plot
def read_csv_file(filename):
	sv_intersection_dict = defaultdict()
	with open(filename, newline='') as csvfile:
		csvreader = csv.reader(csvfile, delimiter=',')
		for row in csvreader:
			caller_combination = row[0]
			intersection_count = row[1]
			sv_intersection_dict[caller_combination] = intersection_count
	return sv_intersection_dict

def create_upset(variant_dict,sv_callers):
	callers_boolean_line_all_comparisons = [] # List to store presence or absence of each caller in a comparison
	callers_intersection_all_comparisons = [] # List to store the intersection count for each comparison
	for comparison in variant_dict.keys():
		callers_boolean_line = []
		for caller in sv_callers:
			caller_in_comparison = caller in comparison
			callers_boolean_line.append(caller_in_comparison)
		callers_intersection_all_comparisons.append(int(variant_dict[comparison]))
		callers_boolean_line_all_comparisons.append(tuple(callers_boolean_line))
	index = pd.MultiIndex.from_tuples(callers_boolean_line_all_comparisons, names=sv_callers)
	variant_series = pd.Series(data=callers_intersection_all_comparisons, index=index)
	return(variant_series)


if args.variant_type.lower() =="deletion" or args.variant_type.lower() =="deletions":
	csv_file = config["input"]["CSV_FILE"]
	csv_file = csv_file.replace("MAXIMUMSIZE", args.maximum_size)
	deletion_dict =	read_csv_file(csv_file)

	# Create upset plot that limits the number of plotted combinations to those provided by user
	if args.max_combos:
		count_list = [int(x) for x in deletion_dict.values()]
		count_list.sort(reverse=True)
		min_subset_value = count_list[args.max_combos-1]
		my_upset = create_upset(deletion_dict, sv_callers)
		plot(my_upset, sort_by='cardinality', min_subset_size=min_subset_value, show_counts='%d')
		if args.subtitle:
			subtitle = "Gene set overlap for largest " + str(args.max_combos) + " largest sets"
			plt.suptitle(subtitle)
		plt.show()

	# Create upset plot that only plots combinations meeting the minimum number of callers. Minimum number of callers specified by user
	elif args.min_degree:
		my_upset = create_upset(deletion_dict, sv_callers)
		plot(my_upset, sort_by='cardinality', min_degree=args.min_degree, show_counts='%d')
		if args.subtitle:
			subtitle = "Gene set overlap for combinations with at least " + str(args.min_degree) + " callers"
			plt.suptitle(subtitle)
		plt.show()

	# Plot all combinations
	else:
		my_upset = create_upset(deletion_dict, sv_callers)
		plot(my_upset, sort_by='cardinality', show_counts='%d')
		if args.subtitle:
			subtitle = "Total gene set overlap"
			plt.suptitle(subtitle)
		plt.show()

if args.variant_type.lower() =="duplication" or args.variant_type.lower() =="duplications":
	csv_file = config["input"]["CSV_FILE"]
	csv_file = csv_file.replace("MAXIMUMSIZE", args.maximum_size)
	duplication_dict =	read_csv_file(csv_file)

	if args.max_combos:
		count_list = [int(x) for x in duplication_dict.values()]
		count_list.sort(reverse=True)
		min_subset_value = count_list[args.max_combos-1]
		my_upset = create_upset(duplication_dict, sv_callers)
		plot(my_upset, sort_by='cardinality', min_subset_size=min_subset_value, show_counts='%d')
		if args.subtitle:
			subtitle = "Gene set overlap for largest " + str(args.max_combos) + " largest sets"
			plt.suptitle(subtitle)
		plt.show()

	elif args.min_degree:
		my_upset = create_upset(duplication_dict, sv_callers)
		plot(my_upset, sort_by='cardinality', min_degree=args.min_degree, show_counts='%d')
		if args.subtitle:
			subtitle = "Gene set overlap for combinations with at least " + str(args.min_degree) + " callers"
			plt.suptitle(subtitle)
		plt.show()

	else:
		my_upset = create_upset(duplication_dict, sv_callers)
		plot(my_upset, sort_by='cardinality', show_counts='%d')
		if args.subtitle:
			subtitle = "Total gene set overlap"
			plt.suptitle(subtitle)
		plt.show()

if args.variant_type.lower() =="inversion" or args.variant_type.lower() =="inversions":
	csv_file = config["input"]["CSV_FILE"]
	csv_file = csv_file.replace("MAXIMUMSIZE", args.maximum_size)
	inversion_dict =	read_csv_file(csv_file)

	if args.max_combos:
		count_list = [int(x) for x in inversion_dict.values()]
		count_list.sort(reverse=True)
		min_subset_value = count_list[args.max_combos-1]
		my_upset = create_upset(inversion_dict, sv_callers)
		plot(my_upset, sort_by='cardinality', min_subset_size=min_subset_value, show_counts='%d')
		if args.subtitle:
			subtitle = "Gene set overlap for largest " + str(args.max_combos) + " largest sets"
			plt.suptitle(subtitle)
		plt.show()

	elif args.min_degree:
		my_upset = create_upset(inversion_dict, sv_callers)
		plot(my_upset, sort_by='cardinality', min_degree=args.min_degree, show_counts='%d')
		if args.subtitle:
			subtitle = "Gene set overlap for combinations with at least " + str(args.min_degree) + " callers"
			plt.suptitle(subtitle)
		plt.show()

	else:
		my_upset = create_upset(inversion_dict, sv_callers)
		plot(my_upset, sort_by='cardinality', show_counts='%d')
		if args.subtitle:
			subtitle = "Total gene set overlap"
			plt.suptitle(subtitle)
		plt.show()
