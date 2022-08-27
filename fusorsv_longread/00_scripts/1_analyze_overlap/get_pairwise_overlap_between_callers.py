import configparser
import argparse
import os
from os import path
from pathlib import Path
from collections import defaultdict
from collections import namedtuple
import itertools
import pybedtools
import numpy as np
import pandas as pd
import seaborn as seaborn
import matplotlib.pylab as plt

config = configparser.ConfigParser()

parser = argparse.ArgumentParser()
parser.add_argument("input_config", help="config file for the variant caller paths, filenames, etc.")
parser.add_argument("variant_type", help="variant type to be analyzed")
parser.add_argument("--maxsize", default="50k", help="maximum variant size")
args = parser.parse_args()

config.read(args.input_config)

# Get the deletion or inversion bed file paths and store in dictionary
def get_variant_bedfiles(variant_type_prefix):
	caller_list = config["callers"]["SV_CALLERS"].split()
	sample_list = config["samples"]["CENDR_SAMPLES"].split()
	#sample_caller_bedfile_dict =  defaultdict(lambda: defaultdict(list))
	sample_caller_bedfile_dict =  defaultdict(lambda: defaultdict(str))
	for sample in sample_list:
		for caller in caller_list:
			caller_bed_dir = config[caller]["BED_DIR"]
			variant_name = variant_type_prefix + "_NAME"
			caller_variant_name = config[caller][variant_name]
			bedfile = caller_bed_dir + caller_variant_name
			bedfile = bedfile.replace("MAXSIZE", args.maxsize)
			bedfile = bedfile.replace("SAMPLE", sample)
			sample_caller_bedfile_dict[sample][caller] = [bedfile]
	return (sample_caller_bedfile_dict)

# Get caller svs from bed file
def get_pairwise_intersections(sample_caller_bedfile_dict):
	intersection_proportion_dict = defaultdict() # Store proportion intersecting calls for pairwise comparisons between callers. Store for all samples together.
	#sample_caller_total_intersection_dict =  defaultdict(lambda: defaultdict(str)) # Store proportion intersecting calls for pairwise comparisons between callers. Stores for each sample.

	for sample in sample_caller_bedfile_dict.keys():
		callers = sample_caller_bedfile_dict[sample].keys()
		prop_matrix = np.ones((len(callers), len(callers)))
		prop_df = pd.DataFrame(prop_matrix, columns=callers, index=callers)

		caller_pairs = itertools.combinations(callers, 2)
		for x in caller_pairs:
			first_caller = x[0]
			first_bedfile_path = sample_caller_bedfile_dict[sample][first_caller][0]
			second_caller = x[1]
			second_bedfile_path = sample_caller_bedfile_dict[sample][second_caller][0]

			if os.path.isfile(first_bedfile_path) and os.path.isfile(second_bedfile_path):
				first_bedfile = pybedtools.BedTool(first_bedfile_path)
				first_bedfile_count = len(first_bedfile)
				second_bedfile = pybedtools.BedTool(second_bedfile_path)
				second_bedfile_count = len(second_bedfile)
				bedfile_intersection = first_bedfile.intersect(second_bedfile, f=0.5, r=True)
				intersection_count = len(bedfile_intersection)
				first_bedfile_unique_count = first_bedfile_count - intersection_count
				second_bedfile_unique_count = second_bedfile_count - intersection_count
				first_second_bedfile_union_size = first_bedfile_count + second_bedfile_count - intersection_count
				intersection_proportion = intersection_count /  first_second_bedfile_union_size

				prop_df[first_caller][second_caller] = intersection_proportion # populate column then row
				prop_df.loc[first_caller, second_caller] = intersection_proportion # populate row then column

			else:
				if not os.path.isfile(first_bedfile_path):
					print("Missing bedfile: " + first_bedfile_path)
				if not os.path.isfile(second_bedfile_path):
						print("Missing bedfile: " + second_bedfile_path)
		intersection_proportion_dict[sample] = prop_df

	return intersection_proportion_dict

def write_df(df,output_dir, outfile):
	df.sort_index(axis=0, inplace=True)
	df.sort_index(axis=1, inplace=True)
	#cols = df.columns.tolist()
	#cols.sort()
	#df = df[cols]
	if not os.path.exists(output_dir): # Check if parent directory exists
		os.makedirs(output_dir)
	csv_file = output_dir + outfile
	print(csv_file)
	df.to_csv(csv_file, float_format= '%.2f')

def create_heatmap(df, outdir, outfile):
	df.sort_index(axis=0, inplace=True)
	df.sort_index(axis=1, inplace=True)
	#cols = df.columns.tolist()
	#cols.sort()
	#df = df[cols]
	if not os.path.exists(outdir): # Check if parent directory exists
		os.makedirs(output_dir)
	#ax = seaborn.heatmap(df, linewidth=0.5, cbar= True)
	#plt.show()
	png_file = outdir + outfile
	mask = np.zeros_like(df)
	mask[np.triu_indices_from(mask)] = True
	with seaborn.axes_style("white"):
		ax = seaborn.heatmap(df, mask=mask, annot=True, square=True,  cmap="YlGnBu")
		plt.tight_layout()
		plt.savefig(png_file)
		#plt.savefig(png_file, height = 8, aspect = 1.25)
		#plt.show()


if args.variant_type.lower() =="deletion" or args.variant_type.lower() =="deletions":
	caller_deletion_dict = get_variant_bedfiles("DELETION") # Get a dict with a key for each caller and values for the caller bed dirs and variant names
	sample_intersection_proportions = get_pairwise_intersections(caller_deletion_dict)

	deletion_dfs = []
	for x in sample_intersection_proportions.items():
		df = x[1]
		outdir = config["output"]["DEL_OUTDIR"]
		outdir = outdir + "strains/"
		outfile = x[0] + "_intersection_proportions.csv"
		write_df(df, outdir, outfile)
		outfile = x[0] + "_intersection_proportions.png"
		deletion_dfs.append(df)

	deletion_dfs_concat_mean = pd.concat(deletion_dfs).groupby(level=0).mean()
	outdir = config["output"]["DEL_OUTDIR"]
	write_df(deletion_dfs_concat_mean, outdir, "deletion_mean_intersection_proportions.csv")
	create_heatmap(deletion_dfs_concat_mean,outdir,"deletion_mean_intersection_proportions.png")

elif args.variant_type.lower() =="duplication" or args.variant_type.lower() =="duplications":
	caller_duplication_dict = get_variant_bedfiles("DUPLICATION") # Get a dict with a key for each caller and values for the caller bed dirs and variant names
	sample_intersection_proportions = get_pairwise_intersections(caller_duplication_dict)

	duplication_dfs = []
	for x in sample_intersection_proportions.items():
		df = x[1]
		outdir = config["output"]["DUP_OUTDIR"]
		outdir = outdir + "strains/"
		outfile = x[0] + "_intersection_proportions.csv"
		write_df(df, outdir, outfile)
		outfile = x[0] + "_intersection_proportions.png"
		duplication_dfs.append(df)

	duplication_dfs_concat_mean = pd.concat(duplication_dfs).groupby(level=0).mean()
	outdir = config["output"]["DUP_OUTDIR"]
	write_df(duplication_dfs_concat_mean, outdir, "duplication_mean_intersection_proportions.csv")
	create_heatmap(duplication_dfs_concat_mean,outdir,"duplication_mean_intersection_proportions.png")

elif args.variant_type.lower() =="inversion" or args.variant_type.lower() =="inversions":
	caller_inversion_dict = get_variant_bedfiles("INVERSION") # Get a dict with a key for each caller and values for the caller bed dirs and variant names
	sample_intersection_proportions = get_pairwise_intersections(caller_inversion_dict)

	inversion_dfs = []
	for x in sample_intersection_proportions.items():
		df = x[1]
		outdir = config["output"]["INV_OUTDIR"]
		outdir = outdir + "strains/"
		outfile = x[0] + "_intersection_proportions.csv"
		write_df(df, outdir, outfile)
		outfile = x[0] + "_intersection_proportions.png"
		inversion_dfs.append(df)

	inversion_dfs_concat_mean = pd.concat(inversion_dfs).groupby(level=0).mean()
	outdir = config["output"]["INV_OUTDIR"]
	write_df(inversion_dfs_concat_mean, outdir, "inversion_mean_intersection_proportions.csv")
	create_heatmap(inversion_dfs_concat_mean,outdir,"inversion_mean_intersection_proportions.png")
