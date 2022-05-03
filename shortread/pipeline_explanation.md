# Explanation of each script

## 0 - Clean up directories

* 0_clean_files.sh
	* Removes results and log files from a previous run to start over

## 1 - Convert vcf files to bed

This step converts the vcf files produced by the callers in the SVE pipeline to bed files.

* `sh 00_scripts/0_prepare_data/1_make_your_beds.sh`
	* Script calls convert2bed.py to convert vcf to bed
* parameters in *1_make_your_beds.sh*
	* minsize
		* Minimum variant size to include in bedfiles
	* maxsize
		* Maximum variant size to include in bedfiles
* Note:
	* BreakDancer produced a small number of predictions where the end coordinate was reported as being before the start coordinate. These are excluded from the bed file.


## 2 - Sort and cluster bed files

This step sorts each of the bed files created in the last step and clusters overlapping SV predictions. The clustering is performed to identify overlapping SV predictions of the same type from the same strain and caller.

* `sh 00_scripts/0_prepare_data/2_sort_cluster_beds.sh`
	* Script sorts bed files using the bash sort command and clusters them using bedtools

## 3 - Decluster and get best prediction from overlapping calls

Many tools will predict multiple overlapping variant calls of the same type for a given strain. This step selects a single best call instead of including multiple overlapping variants of the same type. This was performed to allow predictions to be compared to a truth set and to avoid inflating SV estimates.

* `00_scripts/0_prepare_data/3_decluster.sh`
	* Script calls get_best_calls.py to select the best call for each SV call cluster
* Note: The set of SV calls that result from this step may differ slightly when executed more than once on the same dataset because the best call was selected randomly when the support metric was tied or if the caller does not provide a metric that quantifies the support for each call.

## 4 - Get gene overlap

* `sh 00_scripts/1_analyze_overlap/4_get_gene_overlap.sh`
	* Calls bedtools to determine which SVs overlap with genes in the *C. elegans* reference genome.
	* Results are formatted to store the list of genes that overlap a given call in the last field of the bed file.

## 5 - Get caller overlap

Determine the agreement between callers for which genes are spanned by SVs.

* `00_scripts/1_analyze_overlap/5_get_caller_overlap.sh`
	* Calls Python script to determine agreement between callers
		* get_gene_overlap_between_callers.py
			* Requires config files that specify the file locations and names, and samples to include in the analysis.
				* 00_scripts/1_analyze_overlap/config_files/deletions_high_confidence-cnv.conf
				* 00_scripts/1_analyze_overlap/config_files/duplications_high_confidence-cnv.conf
				* 00_scripts/1_analyze_overlap/config_files/inversions_high_confidence-cnv.conf

## Create upset plots

Plot the agreement between callers for genes that are spanned by SVs.

* `00_scripts/1_analyze_overlap/6_create_upset_plots.sh`
	* Calls Python script to create upset plots
		* create_upset_plots.py
			* Requires config files that specify the csv file containing the overlapping calls from each caller, and the callers to analyze
				* 00_scripts/2_make_plots/config_files/deletion_high_confidence-cnv.conf
				* 00_scripts/2_make_plots/config_files/duplication_high_confidence-cnv.conf
				* 00_scripts/2_make_plots/config_files/inversion_high_confidence-cnv.conf
* parameters in *6_create_upset_plots.sh*
	* input_config
		* config file to pass to script
	* variant_type
		* variant type to plot
	* --max_combos
		* Maximum number of combinations to include in each upset plot. Recommended when the total of combinations is too large to plot effectively
	* --min_degree
		* Optional parameter for the minimum number of callers required to overlap to be included in the plot
50k deletion --max_combos 20
