# Requirements

Python 3 (tested with v3.10.4)
NumPy (tested with v1.23.1)
bedtools (tested with v2.30.0)
pybedtools (tested with v0.8.1)

The vcf files from the entire dataset are located in variant_calls

# Instructions

The following scripts can be run (in numerical order) to quantify the performance of BreakDancer, cnMOPS, CNVnator, Delly, Hydra, and Lumpy.

* sh scripts/1_make_your_beds.sh
	* Calls convert2bed.py to convert vcf files to separate BED files for each variant type and vcf filter value
* sh scripts/2_sort_cluster_beds.sh
	* Find overlapping SV calls and cluster them
* sh scripts/3_decluster.sh
	* Calls get_best_reads.py to pick best call among overlapping calls
* sh scripts/4_get_caller_truth_overlap.sh
	* Get overlap between caller predictions and truth
* sh scripts/5_summarize_clusters.sh
	* Summarize SVs discarded from clusters
* sh scripts/6_summarize_accuracy.sh
   * Calculate sensitiviy, precision, and F1 scores. Calls get_accuracy.py
