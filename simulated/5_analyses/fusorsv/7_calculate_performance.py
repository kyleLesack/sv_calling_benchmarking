import csv
import os

del_bin_sizes = ["100-400bp","400-600bp","600-950bp","950-1.2Kbp","1.2K-1.5Kbp","1.5K-1.9Kbp","1.9K-2.2Kbp","2.2K-2.9Kbp","2.9K-3.6Kbp","3.6K-4.8Kbp","4.8K-6.1Kbp","6.1K-9Kbp","9K-18.5Kbp","18.5K-100Kbp","100K-1Mbp"]
dup_bin_sizes = ["50-1Kbp","1K-10Kbp","10K-50Kbp","50K-100Kbp","100K-250Kbp","250K-500Kbp"]
inv_bin_sizes = ["50-2500bp","2500-3500bp","3500-45Kbp","45K-80Kbp","80K-115Kbp","115K-180Kbp","180K-260Kbp"]

# Parse deletions
deletion_jaccard_scores = []
deletion_precision_scores = []
deletion_recall_scores = []
deletion_f1_scores = []
total_true_positive_deletions = 0
total_false_positive_deletions = 0
total_false_negative_deletions = 0

total_fusor_bp_deletions = 0
total_truth_bp_deletions = 0
total_fusor_truth_intersection_bp_deletions = 0

# The combined true positives, false positives, and false negatives for each size bin are saved in a text file ending in the bin size.
# For each size bin suffix, open the deletion TP, FP, and FN text files and get the number of TPs, FPs, and FNs as well the base pairs contained in each category
for suffix in del_bin_sizes:
	fusor_bp = 0
	truth_bp = 0
	fusor_truth_intersection_bp = 0

	deletion_true_positives = 0
	deletion_false_positives = 0
	deletion_false_negatives = 0

	del_fusor_tp = "./intermediate_results/deletions/deletions_fusor_true_positives_" + str(suffix) + ".txt"
	with open(del_fusor_tp) as fd:
		rd = csv.reader(fd, delimiter="\t", quotechar='"')
		for row in rd: # Determine the number of base pairs covered in each category
			fusor_start_coord = int(row[1])
			fusor_end_coord = int(row[2])
			fusor_size = fusor_end_coord - fusor_start_coord
			fusor_bp = fusor_bp + fusor_size
			truth_start_coord = int(row[5])
			truth_end_coord = int(row[6])
			truth_size = truth_end_coord - truth_start_coord
			truth_bp = truth_bp + truth_size
			fusor_truth_intersection = int(row[8])
			fusor_truth_intersection_bp = fusor_truth_intersection_bp + fusor_truth_intersection
			deletion_true_positives = deletion_true_positives + 1
			total_true_positive_deletions = total_true_positive_deletions + 1
			total_fusor_bp_deletions = total_fusor_bp_deletions + fusor_size
			total_truth_bp_deletions = total_truth_bp_deletions + truth_size
			total_fusor_truth_intersection_bp_deletions = total_fusor_truth_intersection_bp_deletions + fusor_truth_intersection

	del_fusor_fn = "./intermediate_results/deletions/deletions_fusor_false_negatives_" + str(suffix) + ".txt"
	if os.path.getsize(del_fusor_fn) > 0:
		with open(del_fusor_fn) as fd:
			rd = csv.reader(fd, delimiter="\t", quotechar='"')
			for row in rd: # Determine the number of base pairs covered in each category
				truth_start_coord = int(row[1])
				truth_end_coord = int(row[2])
				truth_size = truth_end_coord - truth_start_coord
				truth_bp = truth_bp + truth_size
				deletion_false_negatives = deletion_false_negatives + 1
				total_false_negative_deletions = total_false_negative_deletions + 1
				total_truth_bp_deletions = total_truth_bp_deletions + truth_size

	del_fusor_fp = "./intermediate_results/deletions/deletions_fusor_false_positives_" + str(suffix) + ".txt"
	if os.path.getsize(del_fusor_fp) > 0:
		with open(del_fusor_fp) as fd:
			rd = csv.reader(fd, delimiter="\t", quotechar='"')
			for row in rd: # Determine the number of base pairs covered in each category
				fusor_start_coord = int(row[1])
				fusor_end_coord = int(row[2])
				fusor_size = fusor_end_coord - fusor_start_coord
				fusor_bp = fusor_bp + fusor_size
				deletion_false_positives = deletion_false_positives + 1
				total_false_positive_deletions = total_false_positive_deletions + 1
				total_fusor_bp_deletions = total_fusor_bp_deletions + fusor_size

	fusor_truth_union = fusor_bp + truth_bp - fusor_truth_intersection_bp # Get the union of base pairs covered by the truth and fusorsv sets
	jaccard_score = fusor_truth_intersection_bp / fusor_truth_union # Calculate the Jaccard score
	deletion_jaccard_scores.append(jaccard_score)

	deletion_precision = 0
	deletion_recall = 0
	deletion_f1 = 0

	# Calculate the deletion precision, recall, and F1 scores
	if (deletion_true_positives + deletion_false_positives) != 0:
		deletion_precision = deletion_true_positives / (deletion_true_positives + deletion_false_positives) # Prec = TP / (TP + FP)

	if (deletion_true_positives + deletion_false_negatives) != 0:
		deletion_recall = deletion_true_positives / (deletion_true_positives + deletion_false_negatives) # Rec = TP / (TP + FN)

	if (deletion_precision + deletion_recall) != 0:
		deletion_f1 = (2 * deletion_precision * deletion_recall)/ (deletion_precision + deletion_recall) # F1 = 2 * prec * rec/ (prec + rec)

	deletion_precision_scores.append(deletion_precision)
	deletion_recall_scores.append(deletion_recall)
	deletion_f1_scores.append(deletion_f1)

# The combined true positives, false positives, and false negatives for each size bin are saved in a text file ending in the bin size.
# For each size bin suffix, open the duplication TP, FP, and FN text files and get the number of TPs, FPs, and FNs as well the base pairs contained in each category
duplication_jaccard_scores = []
duplication_precision_scores = []
duplication_recall_scores = []
duplication_f1_scores = []
total_true_positive_duplications = 0
total_false_positive_duplications = 0
total_false_negative_duplications = 0

total_fusor_bp_duplications = 0
total_truth_bp_duplications = 0
total_fusor_truth_intersection_bp_duplications = 0

for suffix in dup_bin_sizes:
	fusor_bp = 0
	truth_bp = 0
	fusor_truth_intersection_bp = 0
	duplication_true_positives = 0
	duplication_false_positives = 0
	duplication_false_negatives = 0

	dup_fusor_tp = "./intermediate_results/duplications/duplications_fusor_true_positives_" + str(suffix) + ".txt"
	with open(dup_fusor_tp) as fd:
		rd = csv.reader(fd, delimiter="\t", quotechar='"')
		for row in rd: # Determine the number of base pairs covered in each category
			fusor_start_coord = int(row[1])
			fusor_end_coord = int(row[2])
			fusor_size = fusor_end_coord - fusor_start_coord
			fusor_bp = fusor_bp + fusor_size
			truth_start_coord = int(row[5])
			truth_end_coord = int(row[6])
			truth_size = truth_end_coord - truth_start_coord
			truth_bp = truth_bp + truth_size
			fusor_truth_intersection = int(row[8])
			fusor_truth_intersection_bp = fusor_truth_intersection_bp + fusor_truth_intersection
			duplication_true_positives = duplication_true_positives + 1
			total_true_positive_duplications = total_true_positive_duplications + 1
			total_fusor_bp_duplications = total_fusor_bp_duplications + fusor_size
			total_truth_bp_duplications = total_truth_bp_duplications + truth_size
			total_fusor_truth_intersection_bp_duplications = total_fusor_truth_intersection_bp_duplications + fusor_truth_intersection

	dup_fusor_fn = "./intermediate_results/duplications/duplications_fusor_false_negatives_" + str(suffix) + ".txt"
	if os.path.getsize(dup_fusor_fn) > 0:
		with open(dup_fusor_fn) as fd:
			rd = csv.reader(fd, delimiter="\t", quotechar='"')
			for row in rd: # Determine the number of base pairs covered in each category

				truth_start_coord = int(row[1])
				truth_end_coord = int(row[2])
				truth_size = truth_end_coord - truth_start_coord
				truth_bp = truth_bp + truth_size
				duplication_false_negatives = duplication_false_negatives + 1
				total_false_negative_duplications = total_false_negative_duplications + 1
				total_truth_bp_duplications = total_truth_bp_duplications + truth_size

	dup_fusor_fp = "./intermediate_results/duplications/duplications_fusor_false_positives_" + str(suffix) + ".txt"
	if os.path.getsize(dup_fusor_fp) > 0:
		with open(dup_fusor_fp) as fd:
			rd = csv.reader(fd, delimiter="\t", quotechar='"') # Determine the number of base pairs covered in each category
			for row in rd:
				fusor_start_coord = int(row[1])
				fusor_end_coord = int(row[2])
				fusor_size = fusor_end_coord - fusor_start_coord
				fusor_bp = fusor_bp + fusor_size
				duplication_false_positives = duplication_false_positives + 1
				total_false_positive_duplications = total_false_positive_duplications + 1
				total_fusor_bp_duplications = total_fusor_bp_duplications + fusor_size

	fusor_truth_union = fusor_bp + truth_bp - fusor_truth_intersection_bp # Get the union of base pairs covered by the truth and fusorsv sets
	jaccard_score = fusor_truth_intersection_bp / fusor_truth_union # Calculate the Jaccard score
	duplication_jaccard_scores.append(jaccard_score)

	duplication_precision = 0
	duplication_recall = 0
	duplication_f1 = 0

	if (duplication_true_positives + duplication_false_positives) != 0:
		duplication_precision = duplication_true_positives / (duplication_true_positives + duplication_false_positives) # Prec = TP / (TP + FP)

	if (duplication_true_positives + duplication_false_negatives) != 0:
		duplication_recall = duplication_true_positives / (duplication_true_positives + duplication_false_negatives) # Rec = TP / (TP + FN)

	if (duplication_precision + duplication_recall) != 0:
		duplication_f1 = (2 * duplication_precision * duplication_recall)/ (duplication_precision + duplication_recall) # F1 = 2 * prec * rec/ (prec + rec)

	duplication_precision_scores.append(duplication_precision)
	duplication_recall_scores.append(duplication_recall)
	duplication_f1_scores.append(duplication_f1)

# The combined true positives, false positives, and false negatives for each size bin are saved in a text file ending in the bin size.
# For each size bin suffix, open the inversion TP, FP, and FN text files and get the number of TPs, FPs, and FNs as well the base pairs contained in each category
inversion_jaccard_scores = []
inversion_precision_scores = []
inversion_recall_scores = []
inversion_f1_scores = []
total_true_positive_inversions = 0
total_false_positive_inversions = 0
total_false_negative_inversions = 0

total_fusor_bp_inversions = 0
total_truth_bp_inversions = 0
total_fusor_truth_intersection_bp_inversions = 0

for suffix in inv_bin_sizes:
	fusor_bp = 0
	truth_bp = 0
	fusor_truth_intersection_bp = 0
	inversion_true_positives = 0
	inversion_false_positives = 0
	inversion_false_negatives = 0

	inv_fusor_tp = "./intermediate_results/inversions/inversions_fusor_true_positives_" + str(suffix) + ".txt"
	with open(inv_fusor_tp) as fd:
		rd = csv.reader(fd, delimiter="\t", quotechar='"')
		for row in rd: # Determine the number of base pairs covered in each category
			fusor_start_coord = int(row[1])
			fusor_end_coord = int(row[2])
			fusor_size = fusor_end_coord - fusor_start_coord
			fusor_bp = fusor_bp + fusor_size
			truth_start_coord = int(row[5])
			truth_end_coord = int(row[6])
			truth_size = truth_end_coord - truth_start_coord
			truth_bp = truth_bp + truth_size
			fusor_truth_intersection = int(row[8])
			fusor_truth_intersection_bp = fusor_truth_intersection_bp + fusor_truth_intersection
			inversion_true_positives = inversion_true_positives + 1
			total_true_positive_inversions = total_true_positive_inversions +1

			total_fusor_bp_inversions = total_fusor_bp_inversions + fusor_size
			total_truth_bp_inversions = total_truth_bp_inversions + truth_size
			total_fusor_truth_intersection_bp_inversions = total_fusor_truth_intersection_bp_inversions + fusor_truth_intersection

	inv_fusor_fn = "./intermediate_results/inversions/inversions_fusor_false_negatives_" + str(suffix) + ".txt"
	if os.path.getsize(inv_fusor_fn) > 0:
		with open(inv_fusor_fn) as fd:
			rd = csv.reader(fd, delimiter="\t", quotechar='"')
			for row in rd: # Determine the number of base pairs covered in each category
				truth_start_coord = int(row[1])
				truth_end_coord = int(row[2])
				truth_size = truth_end_coord - truth_start_coord
				truth_bp = truth_bp + truth_size
				inversion_false_negatives = inversion_false_negatives + 1
				total_false_negative_inversions = total_false_negative_inversions +1

				total_truth_bp_inversions = total_truth_bp_inversions + truth_size

	inv_fusor_fp = "./intermediate_results/inversions/inversions_fusor_false_positives_" + str(suffix) + ".txt"
	if os.path.getsize(inv_fusor_fp) > 0:
		with open(inv_fusor_fp) as fd:
			rd = csv.reader(fd, delimiter="\t", quotechar='"')
			for row in rd: # Determine the number of base pairs covered in each category
				fusor_start_coord = int(row[1])
				fusor_end_coord = int(row[2])
				fusor_size = fusor_end_coord - fusor_start_coord
				fusor_bp = fusor_bp + fusor_size
				inversion_false_positives = inversion_false_positives + 1
				total_false_positive_inversions = total_false_positive_inversions + 1
				total_fusor_bp_inversions = total_fusor_bp_inversions + fusor_size

	fusor_truth_union = fusor_bp + truth_bp - fusor_truth_intersection_bp # Get the union of base pairs covered by the truth and fusorsv sets
	jaccard_score = fusor_truth_intersection_bp / fusor_truth_union # Calculate the Jaccard score
	inversion_jaccard_scores.append(jaccard_score)

	inversion_precision = 0
	inversion_recall = 0
	inversion_f1 = 0

	if (inversion_true_positives + inversion_false_positives) != 0:
		inversion_precision = inversion_true_positives / (inversion_true_positives + inversion_false_positives) # Prec = TP / (TP + FP)

	if (inversion_true_positives + inversion_false_negatives) != 0:
		inversion_recall = inversion_true_positives / (inversion_true_positives + inversion_false_negatives) # Rec = TP / (TP + FN)

	if (inversion_precision + inversion_recall) != 0:
		inversion_f1 = (2 * inversion_precision * inversion_recall)/ (inversion_precision + inversion_recall) # F1 = 2 * prec * rec/ (prec + rec)

	inversion_precision_scores.append(inversion_precision)
	inversion_recall_scores.append(inversion_recall)
	inversion_f1_scores.append(inversion_f1)

### Overall Statistics

total_fusor_truth_union_deletions = total_fusor_bp_deletions + total_truth_bp_deletions - total_fusor_truth_intersection_bp_deletions
total_jaccard_score_deletions = total_fusor_truth_intersection_bp_deletions / total_fusor_truth_union_deletions
total_fusor_truth_union_duplications = total_fusor_bp_duplications + total_truth_bp_duplications - total_fusor_truth_intersection_bp_duplications
total_jaccard_score_duplications = total_fusor_truth_intersection_bp_duplications / total_fusor_truth_union_duplications
total_fusor_truth_union_inversions = total_fusor_bp_inversions + total_truth_bp_inversions - total_fusor_truth_intersection_bp_inversions
total_jaccard_score_inversions = total_fusor_truth_intersection_bp_inversions / total_fusor_truth_union_inversions

total_deletion_precision = 0
total_deletion_recall = 0
total_deletion_f1 = 0

# Calculate the precision for the entire dataset
if (total_true_positive_deletions + total_false_positive_deletions) != 0:
	total_deletion_precision = total_true_positive_deletions / (total_true_positive_deletions + total_false_positive_deletions) # Prec = TP / (TP + FP)
# Calculate the recall for the entire dataset
if (total_true_positive_deletions + total_false_negative_deletions) != 0:
	total_deletion_recall = total_true_positive_deletions / (total_true_positive_deletions + total_false_negative_deletions) # Rec = TP / (TP + FN)
# Calculate the F1 score for the entire dataset
if (total_deletion_precision + total_deletion_recall) != 0:
	total_deletion_f1 = (2 * total_deletion_precision * total_deletion_recall)/ (total_deletion_precision + total_deletion_recall) # F1 = 2 * prec * rec/ (prec + rec)

total_duplication_precision = 0
total_duplication_recall = 0
total_duplication_f1 = 0

# Calculate the precision for the entire dataset
if (total_true_positive_duplications + total_false_positive_duplications) != 0:
	total_duplication_precision = total_true_positive_duplications / (total_true_positive_duplications + total_false_positive_duplications) # Prec = TP / (TP + FP)
# Calculate the recall for the entire dataset
if (total_true_positive_duplications + total_false_negative_duplications) != 0:
	total_duplication_recall = total_true_positive_duplications / (total_true_positive_duplications + total_false_negative_duplications) # Rec = TP / (TP + FN)
# Calculate the F1 score for the entire dataset
if (total_duplication_precision + total_duplication_recall) != 0:
	total_duplication_f1 = (2 * total_duplication_precision * total_duplication_recall)/ (total_duplication_precision + total_duplication_recall) # F1 = 2 * prec * rec/ (prec + rec)

total_inversion_precision = 0
total_inversion_recall = 0
total_inversion_f1 = 0

# Calculate the precision for the entire dataset
if (total_true_positive_inversions + total_false_positive_inversions) != 0:
	total_inversion_precision = total_true_positive_inversions / (total_true_positive_inversions + total_false_positive_inversions) # Prec = TP / (TP + FP)
# Calculate the recall for the entire dataset
if (total_true_positive_inversions + total_false_negative_inversions) != 0:
	total_inversion_recall = total_true_positive_inversions / (total_true_positive_inversions + total_false_negative_inversions) # Rec = TP / (TP + FN)
# Calculate F1 score for the entire dataset
if (total_inversion_precision + total_inversion_recall) != 0:
	total_inversion_f1 = (2 * total_inversion_precision * total_inversion_recall)/ (total_inversion_precision + total_inversion_recall) # F1 = 2 * prec * rec/ (prec + rec)

path = "./summary_statistics/" # Output directory

if not os.path.isdir(path):
	try:
	    os.mkdir(path)
	except OSError:
	    print ("Creation of the directory %s failed" % path)


# Round the results before writing to disk
total_deletion_precision = round(total_deletion_precision, 2)
total_deletion_recall = round(total_deletion_recall, 2)
total_deletion_f1 = round(total_deletion_f1, 2)
total_duplication_precision = round(total_duplication_precision, 2)
total_duplication_recall = round(total_duplication_recall, 2)
total_duplication_f1 = round(total_duplication_f1, 2)
total_inversion_precision = round(total_inversion_precision, 2)
total_inversion_recall = round(total_inversion_recall, 2)
total_inversion_f1 = round(total_inversion_f1, 2)

total_jaccard_score_deletions = round(total_jaccard_score_deletions, 2)
total_jaccard_score_duplications = round(total_jaccard_score_duplications, 2)
total_jaccard_score_inversions = round(total_jaccard_score_inversions, 2)

total_summary_file = path +  "fusor_totals.txt"
with open(total_summary_file, 'w') as the_file: # Write the results summary to a file
	the_file.write("# Deletions")
	the_file.write("\nOverall deletion precision: " + str(total_deletion_precision))
	the_file.write("\nOverall deletion recall: " + str(total_deletion_recall))
	the_file.write("\nOverall deletion F1: " + str(total_deletion_f1))
	the_file.write("\nOverall deletion Jaccard: " + str(total_jaccard_score_deletions))
	the_file.write("\n# Duplications")
	the_file.write("\nOverall duplication precision: " + str(total_duplication_precision))
	the_file.write("\nOverall duplication recall: " + str(total_duplication_recall))
	the_file.write("\nOverall duplication F1: " + str(total_duplication_f1))
	the_file.write("\nOverall duplication Jaccard: " + str(total_jaccard_score_duplications))
	the_file.write("\n# Inversions")
	the_file.write("\nOverall inversion precision: " + str(total_inversion_precision))
	the_file.write("\nOverall inversion recall: "  + str(total_inversion_recall))
	the_file.write("\nOverall inversion F1: "  + str(total_inversion_f1))
	the_file.write("\nOverall inversion Jaccard: " + str(total_jaccard_score_inversions ) + "\n")

# Write to 2 decimal places
deletion_jaccard_scores_rounded = [ round(elem, 2) for elem in deletion_jaccard_scores ]
duplication_jaccard_scores_rounded = [ round(elem, 2) for elem in duplication_jaccard_scores ]
inversion_jaccard_scores_rounded = [ round(elem, 2) for elem in inversion_jaccard_scores ]

# Jaccard
del_jaccard_output_file = path +  "deletions_rounded_jaccard.csv"
with open(del_jaccard_output_file, 'w', newline='') as csvfile:
	jaccardwriter = csv.writer(csvfile, delimiter=',')
	jaccardwriter.writerow(del_bin_sizes)
	jaccardwriter.writerow(deletion_jaccard_scores_rounded)

dup_jaccard_output_file = path +  "duplications_rounded_jaccard.csv"
with open(dup_jaccard_output_file, 'w', newline='') as csvfile:
	jaccardwriter = csv.writer(csvfile, delimiter=',')
	jaccardwriter.writerow(dup_bin_sizes)
	jaccardwriter.writerow(duplication_jaccard_scores_rounded)

inv_jaccard_output_file = path +  "inversions_rounded_jaccard.csv"
with open(inv_jaccard_output_file, 'w', newline='') as csvfile:
	jaccardwriter = csv.writer(csvfile, delimiter=',')
	jaccardwriter.writerow(inv_bin_sizes)
	jaccardwriter.writerow(inversion_jaccard_scores_rounded)

# Precision
deletion_precision_scores_rounded = [ round(elem, 2) for elem in deletion_precision_scores ]
duplication_precision_scores_rounded = [ round(elem, 2) for elem in duplication_precision_scores ]
inversion_precision_scores_rounded = [ round(elem, 2) for elem in inversion_precision_scores ]

del_precision_output_file = path +  "deletions_rounded_precision.csv"
with open(del_precision_output_file, 'w', newline='') as csvfile:
	precisionwriter = csv.writer(csvfile, delimiter=',')
	precisionwriter.writerow(del_bin_sizes)
	precisionwriter.writerow(deletion_precision_scores_rounded)

dup_precision_output_file = path +  "duplications_rounded_precision.csv"
with open(dup_precision_output_file, 'w', newline='') as csvfile:
	precisionwriter = csv.writer(csvfile, delimiter=',')
	precisionwriter.writerow(dup_bin_sizes)
	precisionwriter.writerow(duplication_precision_scores_rounded)

inv_precision_output_file = path +  "inversions_rounded_precision.csv"
with open(inv_precision_output_file, 'w', newline='') as csvfile:
	precisionwriter = csv.writer(csvfile, delimiter=',')
	precisionwriter.writerow(inv_bin_sizes)
	precisionwriter.writerow(inversion_precision_scores_rounded)

# recall
deletion_recall_scores_rounded = [ round(elem, 2) for elem in deletion_recall_scores ]
duplication_recall_scores_rounded = [ round(elem, 2) for elem in duplication_recall_scores ]
inversion_recall_scores_rounded = [ round(elem, 2) for elem in inversion_recall_scores ]

del_recall_output_file = path +  "deletions_rounded_recall.csv"
with open(del_recall_output_file, 'w', newline='') as csvfile:
	recallwriter = csv.writer(csvfile, delimiter=',')
	recallwriter.writerow(del_bin_sizes)
	recallwriter.writerow(deletion_recall_scores_rounded)

dup_recall_output_file = path +  "duplications_rounded_recall.csv"
with open(dup_recall_output_file, 'w', newline='') as csvfile:
	recallwriter = csv.writer(csvfile, delimiter=',')
	recallwriter.writerow(dup_bin_sizes)
	recallwriter.writerow(duplication_recall_scores_rounded)

inv_recall_output_file = path +  "inversions_rounded_recall.csv"
with open(inv_recall_output_file, 'w', newline='') as csvfile:
	recallwriter = csv.writer(csvfile, delimiter=',')
	recallwriter.writerow(inv_bin_sizes)
	recallwriter.writerow(inversion_recall_scores_rounded)

# f1
deletion_f1_scores_rounded = [ round(elem, 2) for elem in deletion_f1_scores ]
duplication_f1_scores_rounded = [ round(elem, 2) for elem in duplication_f1_scores ]
inversion_f1_scores_rounded = [ round(elem, 2) for elem in inversion_f1_scores ]

del_f1_output_file = path +  "deletions_rounded_f1.csv"
with open(del_f1_output_file, 'w', newline='') as csvfile:
	f1writer = csv.writer(csvfile, delimiter=',')
	f1writer.writerow(del_bin_sizes)
	f1writer.writerow(deletion_f1_scores_rounded)

dup_f1_output_file = path +  "duplications_rounded_f1.csv"
with open(dup_f1_output_file, 'w', newline='') as csvfile:
	f1writer = csv.writer(csvfile, delimiter=',')
	f1writer.writerow(dup_bin_sizes)
	f1writer.writerow(duplication_f1_scores_rounded)

inv_f1_output_file = path +  "inversions_rounded_f1.csv"
with open(inv_f1_output_file, 'w', newline='') as csvfile:
	f1writer = csv.writer(csvfile, delimiter=',')
	f1writer.writerow(inv_bin_sizes)
	f1writer.writerow(inversion_f1_scores_rounded)
