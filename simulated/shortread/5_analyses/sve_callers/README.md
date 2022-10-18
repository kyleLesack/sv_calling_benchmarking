# Requirements

Python 3 (tested with 3.10.4)
NumPy (tested with 1.23.1)
bedtools (tested with 2.30.0)

The vcf files from the entire dataset are located in sve_calls/

The following scripts can be run (in numerical order) to quantify the performance of BreakDancer, cnMOPS, CNVnator, Delly, Hydra, and Lumpy.


* 1_prepare_python_sve_calls.sh
	* Calls get_sv_size_bins.py to convert vcf files to separate BED files for each variant type and size range (based on FusorSV size bins)
* 2_sort_beds.sh, 3_merge_beds.sh
	* Combine overlapping SV predictions contained in the BED files for each caller
* 4_call_bedtools.sh
	* Calls bedtools to identify true positives, false positives, and false negatives
* 5_concatenate_bedtools.sh
	* Concatenate the bedtools results from all samples into single files for each SV type
* 6_summarize_true_positives.sh
	* Breakdown TPs by size and type
* 7_label_false_positives.sh
	* Add a name for false postive variants in bedfile. Makes it easier to keep track of false positives during analysis.
* 8_summarize_false_positives.sh
	* Breakdown FPs by size and type
* 9_summarize_false_negatives.sh
	* Breakdown FNs by size and type
* 10_call_calculate_stats.sh
	* Calls calculate_performance.py to summarize performance metrics for each caller
