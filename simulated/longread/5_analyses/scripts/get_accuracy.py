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
parser.add_argument("config_file", help="Config file with the paths for the input and output files")

args = parser.parse_args()
config.read(args.config_file)
callers = config.sections()

# Get precision, recall, F1 scores
def get_metrics(metric_file):
	if os.path.isfile(metric_file):
		with open(metric_file) as f:
			stat_lines = f.readlines()
			true_positives = stat_lines[0].strip()
			true_positives = int(true_positives.split(":")[1])
			false_positives = stat_lines[1].strip()
			false_positives = int(false_positives.split(":")[1])
			false_negatives = stat_lines[2].strip()
			false_negatives = int(false_negatives.split(":")[1])

			if (true_positives + false_negatives) != 0:
				recall = true_positives / (true_positives + false_negatives)
			else:
				recall = 0
			if (true_positives + false_positives) != 0:
				precision = true_positives / (true_positives + false_positives)
			else:
				precision = 0
			if (precision + recall) != 0:
				f1_score = 2 * (precision * recall)/(precision + recall)
			else:
				f1_score = 0
	else:
		print("Missing input file: " + metric_file)

	return(recall, precision, f1_score)

# Writes performance metrics to disk
def write_statistics(output_lines, output_file):
	path = Path(output_file)
	parent_path = path.parent.absolute() # Get the path for the variant file parent directory
	outputdir = str(parent_path)

	if not os.path.exists(outputdir): # Check if parent directory exists
		os.makedirs(outputdir)

	print("Writing to: " + output_file)
	with open(output_file, 'w', newline='\n') as f:
		for line in output_lines:
			f.write(line + "\n")

for sv_caller in callers:
	output_lines = []
	output_lines.append("Variant Type, Recall, Precision, F1-Score")

	deletion_file = config[sv_caller]["DEL_FILE"]
	deletion_metrics = get_metrics(deletion_file) # recall, precision, f1_score
	del_line = "deletions," + f"{deletion_metrics[0]:.3f}" + "," + f"{deletion_metrics[1]:.3f}" + "," + f"{deletion_metrics[2]:.3f}"
	output_lines.append(del_line)

	duplication_file = config[sv_caller]["DUP_FILE"]
	duplication_metrics = get_metrics(duplication_file) # recall, precision, f1_score
	dup_line = "duplications," + f"{duplication_metrics[0]:.3f}" + "," + f"{duplication_metrics[1]:.3f}" + "," + f"{duplication_metrics[2]:.3f}"
	output_lines.append(dup_line)

	inversion_file = config[sv_caller]["INV_FILE"]
	inversion_metrics = get_metrics(inversion_file) # recall, precision, f1_score
	inv_line = "inversions," + f"{inversion_metrics[0]:.3f}" + "," + f"{inversion_metrics[1]:.3f}" + "," + f"{inversion_metrics[2]:.3f}"
	output_lines.append(inv_line)

	output_file = config[sv_caller]["OUTFILE"]
	write_statistics(output_lines, output_file)
