import csv
import os
import argparse
from pathlib import Path

del_bin_sizes = ["100-400bp","400-600bp","600-950bp","950-1.2Kbp","1.2K-1.5Kbp","1.5K-1.9Kbp","1.9K-2.2Kbp","2.2K-2.9Kbp","2.9K-3.6Kbp","3.6K-4.8Kbp","4.8K-6.1Kbp","6.1K-9Kbp","9K-18.5Kbp","18.5K-100Kbp","100K-1Mbp","1Mbp"]
dup_bin_sizes = ["100-1Kbp","1K-10Kbp","10K-50Kbp","50K-100Kbp","100K-250Kbp","250K-500Kbp","500K-1Mbp","1Mbp"]
inv_bin_sizes = ["100-2500bp","2500-3500bp","3500-45Kbp","45K-80Kbp","80K-115Kbp","115K-180Kbp","180K-260Kbp","260K-300Kbp","300K-375Kbp","375K-500Kbp","500K-1Mbp","1Mbp"]

parser = argparse.ArgumentParser()
parser.add_argument("variant_dir", help="Variant directory with true and false positives and false negatives.")
args = parser.parse_args()

# Parse variants
def calculate_variant_stats(variant_dir,caller, variant_type):
	variant_jaccard_scores = []

	# List to store metric values
	caller_precision_scores = []
	caller_recall_scores = []
	caller_f1_scores = []

	# Store total counts here
	total_true_positives = 0
	total_false_positives = 0
	total_false_negatives = 0

	# Store total bps covered by each type here
	total_variant_bp = 0
	total_truth_bp = 0
	total_variant_truth_intersection_bp = 0

	if variant_type == "DEL":
		variant_bin_sizes = del_bin_sizes # Get bin size prefixes of filenames
		file_prefix = variant_dir + "/deletions_" + caller

	if variant_type == "DUP":
		variant_bin_sizes = dup_bin_sizes # Get bin size prefixes of filenames
		file_prefix = variant_dir + "/duplications_" + caller

	if variant_type == "INV":
		variant_bin_sizes = inv_bin_sizes # Get bin size prefixes of filenames
		file_prefix = variant_dir + "/inversions_" + caller

	# Loop through each bin size
	for suffix in variant_bin_sizes:
		variant_bp = 0
		truth_bp = 0
		variant_truth_intersection_bp = 0

		variant_true_positives = 0
		variant_false_positives = 0
		variant_false_negatives = 0

		my_variant_tp = file_prefix + "_true_positives_" + str(suffix) + ".txt" # Input file
		with open(my_variant_tp) as fd:
			rd = csv.reader(fd, delimiter="\t", quotechar='"')
			for row in rd:
				variant_start_coord = int(row[1])
				variant_end_coord = int(row[2])
				variant_size = variant_end_coord - variant_start_coord
				variant_bp = variant_bp + variant_size
				total_variant_bp = total_variant_bp + variant_size

				truth_start_coord = int(row[4])
				truth_end_coord = int(row[5])
				truth_size = truth_end_coord - truth_start_coord
				truth_bp = truth_bp + truth_size
				total_truth_bp = total_truth_bp + truth_size

				variant_truth_intersection = int(row[7])
				variant_truth_intersection_bp = variant_truth_intersection_bp + variant_truth_intersection
				total_variant_truth_intersection_bp = total_variant_truth_intersection_bp + variant_truth_intersection
				variant_true_positives = variant_true_positives + 1
				total_true_positives = total_true_positives + 1


		my_variant_fn = file_prefix + "_false_negatives_" + str(suffix) + ".txt" # Input file
		if os.path.getsize(my_variant_fn) > 0:
			with open(my_variant_fn) as fd:
				rd = csv.reader(fd, delimiter="\t", quotechar='"')
				for row in rd:
					truth_start_coord = int(row[1])
					truth_end_coord = int(row[2])
					truth_size = truth_end_coord - truth_start_coord
					truth_bp = truth_bp + truth_size
					total_truth_bp = total_truth_bp + truth_size
					variant_false_negatives = variant_false_negatives + 1
					total_false_negatives = total_false_negatives + 1

		my_variant_fp = file_prefix + "_false_positives_" + str(suffix) + ".txt"

		if os.path.getsize(my_variant_fp) > 0:
			with open(my_variant_fp) as fd:
				rd = csv.reader(fd, delimiter="\t", quotechar='"')
				for row in rd:
					variant_start_coord = int(row[1])
					variant_end_coord = int(row[2])
					variant_size = variant_end_coord - variant_start_coord
					variant_bp = variant_bp + variant_size
					total_variant_bp = total_variant_bp + variant_size

					variant_false_positives = variant_false_positives + 1
					total_false_positives = total_false_positives + 1

		variant_truth_union = variant_bp + truth_bp - variant_truth_intersection_bp
		if variant_truth_union == 0:
			jaccard_score = 0
		else:
			jaccard_score = variant_truth_intersection_bp / variant_truth_union # Jaccard = (tp) / (tp + fp + fn)
		variant_jaccard_scores.append(jaccard_score)

		caller_precision = 0
		caller_recall = 0
		caller_f1 = 0

		if (variant_true_positives + variant_false_positives) != 0: # If tps or fps exist, calculate precision
			caller_precision = variant_true_positives / (variant_true_positives + variant_false_positives) # Prec = TP / (TP + FP)

		if (variant_true_positives + variant_false_negatives) != 0: # If tps or fns exist, calculate recall
			caller_recall = variant_true_positives / (variant_true_positives + variant_false_negatives) # Rec = TP / (TP + FN)

		if (caller_precision + caller_recall) != 0: # If precision or recall not 0, calculate F1 score
			caller_f1 = (2 * caller_precision * caller_recall)/ (caller_precision + caller_recall) # F1 = 2 * prec * rec/ (prec + rec)

		caller_precision_scores.append(caller_precision)
		caller_recall_scores.append(caller_recall)
		caller_f1_scores.append(caller_f1)

	total_caller_precision = 0
	total_caller_recall = 0
	total_caller_f1 = 0

	total_variant_truth_union = total_variant_bp + total_truth_bp - total_variant_truth_intersection_bp

	if total_variant_truth_union == 0:
		total_jaccard_score = 0
	else:
		total_jaccard_score = total_variant_truth_intersection_bp / total_variant_truth_union # Jaccard = (tp) / (tp + fp + fn)


	if (total_true_positives + total_false_positives) != 0:
		total_caller_precision = total_true_positives / (total_true_positives + total_false_positives) # Prec = TP / (TP + FP)

	if (total_true_positives + total_false_negatives) != 0:
		total_caller_recall = total_true_positives / (total_true_positives + total_false_negatives) # Rec = TP / (TP + FN)

	if (total_caller_precision + total_caller_recall) != 0:
		total_caller_f1 = (2 * total_caller_precision * total_caller_recall)/ (total_caller_precision + total_caller_recall) # F1 = 2 * prec * rec/ (prec + rec)

	return variant_jaccard_scores,caller_precision_scores,caller_recall_scores,caller_f1_scores,total_jaccard_score,total_caller_precision,total_caller_recall,total_caller_f1

# Write summaries of different performance metrics to disk, but round the results first
def write_summaries_rounded(summary_path, outfile_prefix, caller_variant_type_stats,variant_bin_sizes):
	variant_type_jaccard_scores = caller_variant_type_stats[0]
	variant_type_precision_scores = caller_variant_type_stats[1]
	variant_type_recall_scores = caller_variant_type_stats[2]
	variant_type_f1_scores = caller_variant_type_stats[3]

	variant_type_jaccard_scores_rounded =  [ round(elem, 2) for elem in variant_type_jaccard_scores ]
	variant_type_precision_scores_rounded = [ round(elem, 2) for elem in variant_type_precision_scores ]
	variant_type_recall_scores_rounded = [ round(elem, 2) for elem in variant_type_recall_scores ]
	variant_type_f1_scores_rounded = [ round(elem, 2) for elem in variant_type_f1_scores ]

	variant_jaccard_output_file = outfile_prefix +  "_rounded_jaccard.csv"
	with open(variant_jaccard_output_file, 'w', newline='') as csvfile:
		jaccardwriter = csv.writer(csvfile, delimiter=',')
		jaccardwriter.writerow(variant_bin_sizes)
		jaccardwriter.writerow(variant_type_jaccard_scores_rounded)

	variant_precision_output_file = outfile_prefix +  "_rounded_precision.csv"
	with open(variant_precision_output_file, 'w', newline='') as csvfile:
		precisionwriter = csv.writer(csvfile, delimiter=',')
		precisionwriter.writerow(variant_bin_sizes)
		precisionwriter.writerow(variant_type_precision_scores_rounded)

	variant_recall_output_file = outfile_prefix +  "_rounded_recall.csv"
	with open(variant_recall_output_file, 'w', newline='') as csvfile:
		recallwriter = csv.writer(csvfile, delimiter=',')
		recallwriter.writerow(variant_bin_sizes)
		recallwriter.writerow(variant_type_recall_scores_rounded)

	variant_f1_output_file = outfile_prefix +  "_rounded_f1.csv"
	with open(variant_f1_output_file, 'w', newline='') as csvfile:
		f1writer = csv.writer(csvfile, delimiter=',')
		f1writer.writerow(variant_bin_sizes)
		f1writer.writerow(variant_type_f1_scores_rounded)

# Write the performance metrics calculated from the totals to disk after rounding first
def write_total_summaries_rounded(summary_path, outfile_prefix, caller_variant_type_stats):
	variant_type_jaccard_scores = caller_variant_type_stats[4]
	variant_type_precision_scores = caller_variant_type_stats[5]
	variant_type_recall_scores = caller_variant_type_stats[6]
	variant_type_f1_scores = caller_variant_type_stats[7]

	variant_type_jaccard_scores_rounded = round(variant_type_jaccard_scores, 2)
	variant_type_precision_scores_rounded = round(variant_type_precision_scores, 2)
	variant_type_recall_scores_rounded = round(variant_type_recall_scores, 2)
	variant_type_f1_scores_rounded = round(variant_type_f1_scores, 2)


	variant_jaccard_output_file = outfile_prefix +  "_statistics_total.txt"
	with open(variant_jaccard_output_file, 'w', newline='') as txtfile:
		txtfile.write("Overall precision: " + str(variant_type_precision_scores_rounded))
		txtfile.write("\nOverall recall: " + str(variant_type_recall_scores_rounded))
		txtfile.write("\nOverall F1: " + str(variant_type_f1_scores_rounded))
		txtfile.write("\nOverall Jaccard: " + str(variant_type_jaccard_scores_rounded))


path = Path(args.variant_dir)
caller = str(path).rsplit("/")[1]
caller_del_path = str(path) + "/deletions/"
caller_dup_path = str(path) + "/duplications/"
caller_inv_path = str(path) + "/inversions/"
caller_deletion_stats = calculate_variant_stats(caller_del_path,caller,"DEL")
caller_duplication_stats = calculate_variant_stats(caller_dup_path,caller,"DUP")
caller_inversion_stats = calculate_variant_stats(caller_inv_path,caller,"INV")

summary_path =  str(path) + "/summary/"
if not os.path.isdir(summary_path):
	try:
	    os.mkdir(summary_path)
	except OSError:
	    print ("Creation of the directory %s failed" % summary_path)

delfile_prefix = summary_path + caller + "_deletions"
dupfile_prefix = summary_path + caller + "_duplications"
invfile_prefix = summary_path + caller + "_inversions"

write_summaries_rounded(summary_path, delfile_prefix, caller_deletion_stats, del_bin_sizes)
write_summaries_rounded(summary_path, dupfile_prefix, caller_duplication_stats,dup_bin_sizes)
write_summaries_rounded(summary_path, invfile_prefix, caller_inversion_stats,inv_bin_sizes)

summary_path =  str(path) + "/total_summaries/"
if not os.path.isdir(summary_path):
	try:
	    os.mkdir(summary_path)
	except OSError:
	    print ("Creation of the directory %s failed" % summary_path)

delfile_prefix = summary_path + caller + "_deletions"
dupfile_prefix = summary_path + caller + "_duplications"
invfile_prefix = summary_path + caller + "_inversions"

write_total_summaries_rounded(summary_path, delfile_prefix, caller_deletion_stats)
write_total_summaries_rounded(summary_path, dupfile_prefix, caller_duplication_stats)
write_total_summaries_rounded(summary_path, invfile_prefix, caller_inversion_stats)
