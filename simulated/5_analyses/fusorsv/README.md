# Requirements

Python 3 (test with 3.10.4)
NumPy (tested with 1.23.1)
bedtools (tested with 2.30.0)

# Break down sv calls by size 

The following command finds all of the vcf files in the results directory and calls a Python script (get_sv_size_bins.py) to break the sv calls into the FusorSV size bin. Results are stored in BED files.

sh 1_prepare_python_calls.sh


# Compare FusorSV calls to truth

The following command uses bedtools intersect to find the true positives, false positives, and false negatives.

sh 2_call_bedtools.sh

# Concatenate results

The following scripts combines the separate results together to analyze the dataset as a whole

sh 3_concatenate_bedtools.sh
sh 4_summarize_true_positives.sh
sh 5_summarize_false_positives.sh
sh 6_summarize_false_negatives.sh

# Calculate performance statistics

The following script calculates the precision, recall, F1 score, and Jaccard simularity score for each variant type. Results are stored in the summary_statistics directory.

python3 7_calculate_performance.py
