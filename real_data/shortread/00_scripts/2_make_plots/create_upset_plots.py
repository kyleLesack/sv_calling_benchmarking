import configparser
import argparse
import os
import csv
from os import path
from pathlib import Path
from collections import defaultdict
from collections import namedtuple
import pandas as pd
from upsetplot import UpSet
from matplotlib import pyplot as plt
from upsetplot import generate_counts, plot

config = configparser.ConfigParser()
parser = argparse.ArgumentParser()
parser.add_argument("input_config", help="config file for the variant caller paths, filenames, etc.")
parser.add_argument("variant_type", help="variant type to be analyzed")
parser.add_argument("--max_combos", dest='max_combos',nargs='?',type=int,help="Maximum number of combos in the plot")
parser.add_argument("--min_degree", dest='min_degree',nargs='?', type=int, help="Combo minimum number of callers")

args = parser.parse_args()

config.read(args.input_config)
sv_callers = config["variant_callers"]["CALLERS"].split()

caller_shorthand_dict  = {"assemblytics_mummer4_canu":"assemblytics",  "mumandco_v3": "mumandco", "pbsv_pbmm2":"pbsv", "sniffles_ngmlr":"sniffles", "svim_ngmlr":"svim"}

# Read csv file with caller combinations and set sizes
def read_csv_file(filename):
	sv_intersection_dict = defaultdict()
	with open(filename, newline='') as csvfile:
		spamreader = csv.reader(csvfile, delimiter=',')
		for row in spamreader:
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
	csv_file = config["input"]["CSV_FILE"] # Get location of cnv file with the combination set sizes
	deletion_dict =	read_csv_file(csv_file)

	# If user provided parameter to plot a maximum number of combinations
	if args.max_combos:
		count_list = [int(x) for x in deletion_dict.values()] # Get the set size for each caller combination
		count_list.sort(reverse=True)
		min_subset_value = count_list[args.max_combos-1]
		my_upset = create_upset(deletion_dict, sv_callers) # Create upset plot
		plot(my_upset, sort_by='cardinality', min_subset_size=min_subset_value, show_counts='%d')
		subtitle = "Gene set overlap for largest " + str(args.max_combos) + " largest deletion sets"
		plt.suptitle(subtitle)
		plt.show()
	elif args.min_degree:
		my_upset = create_upset(deletion_dict, sv_callers)
		plot(my_upset, sort_by='cardinality', min_degree=args.min_degree, show_counts='%d')
		subtitle = "Gene set overlap for deletion combinations with at least " + str(args.min_degree) + " callers"
		plt.show()
	else:
		my_upset = create_upset(deletion_dict, sv_callers)
		plot(my_upset, sort_by='cardinality', show_counts='%d')
		subtitle = "Total gene set overlap"
		plt.show()

if args.variant_type.lower() =="duplication" or args.variant_type.lower() =="duplications":
	csv_file = config["input"]["CSV_FILE"] # Get location of cnv file with the combination set sizes
	duplication_dict =	read_csv_file(csv_file)

	# If user provided parameter to plot a maximum number of combinations
	if args.max_combos:
		count_list = [int(x) for x in duplication_dict.values()] # Get the set size for each caller combination
		count_list.sort(reverse=True)
		min_subset_value = count_list[args.max_combos-1]
		my_upset = create_upset(duplication_dict, sv_callers)
		plot(my_upset, sort_by='cardinality', min_subset_size=min_subset_value, show_counts='%d')
		subtitle = "Gene set overlap for largest " + str(args.max_combos) + " largest duplication sets"
		plt.suptitle(subtitle)
		plt.show()
	elif args.min_degree:
		my_upset = create_upset(duplication_dict, sv_callers)
		plot(my_upset, sort_by='cardinality', min_degree=args.min_degree, show_counts='%d')
		subtitle = "Gene set overlap for duplication combinations with at least " + str(args.min_degree) + " callers"
		plt.show()
	else:
		my_upset = create_upset(duplication_dict, sv_callers)
		plot(my_upset, sort_by='cardinality', show_counts='%d')
		subtitle = "Total gene set overlap"
		plt.show()

if args.variant_type.lower() =="inversion" or args.variant_type.lower() =="inversions":
	csv_file = config["input"]["CSV_FILE"] # Get location of cnv file with the combination set sizes
	inversion_dict =	read_csv_file(csv_file)

	if args.max_combos:
		count_list = [int(x) for x in inversion_dict.values()] # Get the set size for each caller combination
		count_list.sort(reverse=True)
		min_subset_value = count_list[args.max_combos-1]
		my_upset = create_upset(inversion_dict, sv_callers)
		plot(my_upset, sort_by='cardinality', min_subset_size=min_subset_value, show_counts='%d')
		subtitle = "Gene set overlap for largest " + str(args.max_combos) + " largest inversion sets"
		plt.suptitle(subtitle)
		plt.show()
	elif args.min_degree:
		my_upset = create_upset(inversion_dict, sv_callers)
		plot(my_upset, sort_by='cardinality', min_degree=args.min_degree, show_counts='%d')
		subtitle = "Gene set overlap for inversion combinations with at least " + str(args.min_degree) + " callers"
		plt.show()
	else:
		my_upset = create_upset(inversion_dict, sv_callers)
		plot(my_upset, sort_by='cardinality', show_counts='%d')
		subtitle = "Total gene set overlap"
		plt.show()
