# Explanation of each script

## 0 - Clean up directories

0_clean_files.sh

## 1 - Convert vcf files to bed

This step converts the vcf files produced by the callers in the SVE pipeline to bed files.

`sh 00_scripts/0_prepare_data/1_make_your_beds.sh` # Script calls convert2bed.py to convert vcf to bed

* parameters in *1_make_your_beds.sh*
	* minsize
		* Minimum variant size to include in bedfiles
	* maxsize
		* Maximum variant size to include in bedfiles
* Note:
	* BreakDancer produced a small number of predictions where the end coordinate was reported as being before the start coordinate. These are excluded from the bed file.


## 2 - Sort and cluster bed files

This step sorts each of the bed files created in the last step and clusters overlapping SV predictions. The clustering is performed to identify overlapping SV predictions of the same type from the same strain and caller.

* `sh 00_scripts/0_prepare_data/2_sort_cluster_beds.sh` # Script sorts bed files using the bash sort command and clusters them using bedtools
	* Script sorts bed files using the bash sort command and clusters them using bedtools

## 3 Decluster and get best prediction from overlapping calls

`00_scripts/0_prepare_data/3_decluster.sh` # Script calls get_best_calls.py to select the best call for each SV call cluster

Note: The set of SV calls that result from this step may differ slightly when executed more than once on the same dataset because the best call was selected randomly when the support metric was tied or if the caller does not provide a metric that quantifies the support for each call.
