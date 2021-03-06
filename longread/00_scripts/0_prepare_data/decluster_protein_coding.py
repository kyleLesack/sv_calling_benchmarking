import argparse
import os
from collections import defaultdict
import random
parser = argparse.ArgumentParser()
parser.add_argument("input_bed", help="bed file with clustered reads. Created from a matching vcf file.")
args = parser.parse_args()

# Get clusters (generated by bedtools) and store them in a dict
def get_clusters(variants):
	cluster_dict = defaultdict(list)
	for line in variants:
		line_split = line.split()
		variant_name = line_split[3]
		cluster_dict[variant_name].append(line)
	return(cluster_dict)

# Separate variant call dict into sv call clusters with one member or multiple members
def resolve_cluster(sv_calls):
	gene_names = set()
	bed_line = sv_calls[0]
	bed_line_split = bed_line.split("\t")

	for line in sv_calls:
		sv_call_split = line.split("\t")
		gene_name = sv_call_split[4]
		gene_names.add(gene_name)

	gene_names = ','.join(str(s) for s in gene_names)
	bed_line_split[4] = gene_names
	return(bed_line_split)

def get_calls(cluster_dict):
	bed_lines = []
	for variant_name, variant_line in cluster_dict.items():
		if len(variant_line) == 1:
			split_variant_line = variant_line[0].split()
			# Get chromosome, coordinates,sv name, and genes
			new_bed_line = split_variant_line[0] + "\t" + split_variant_line[1] + "\t" + split_variant_line[2] + "\t" + split_variant_line[3] + "\t" + split_variant_line[4]
			bed_lines.append(new_bed_line)

		elif len(variant_line) > 1:
			multiple_genes_call = resolve_cluster(variant_line)
			new_bed_line = multiple_genes_call[0] + "\t" + multiple_genes_call[1] + "\t" + multiple_genes_call[2] + "\t" + multiple_genes_call[3] + "\t" + multiple_genes_call[4]
			bed_lines.append(new_bed_line)

	return(bed_lines)

def write_bed(bedlines):
	bed_dir = os.path.dirname(args.input_bed)
	bed_dir = bed_dir.replace("2_variant_calls_declustered", "3_variant_calls_spanning_genes")

	sample_name = os.path.basename(args.input_bed).split(".")[0]
	output_file = bed_dir + "/" + sample_name + ".spanning_genes.bed"

	# Check if output directories exist.
	if not os.path.exists(bed_dir):
		os.makedirs(bed_dir)

	#Check if files exist. If not, write to file.
	if os.path.isfile(output_file):
		print(str(output_file) + " exists. Not overwriting.")
	else:
		with open(output_file, 'w', newline='\n') as f:
				f.writelines("%s\n" % l for l in bedlines)

with open(args.input_bed) as f:
	variants = f.readlines()
variant_cluster_dict = get_clusters(variants)
variant_bedlines = get_calls(variant_cluster_dict)
write_bed(variant_bedlines)
