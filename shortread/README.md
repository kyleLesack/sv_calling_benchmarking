# cendr_benchmarking

Scripts for structural variant caller benchmarking using shortread data.

# Requirements

* Python 3
* bedtools (tested using v2.30.0)
* Python libraries
	* pybedtools (tested using v0.9.0)
	* pandas (tested using v1.1.3)
	* upsetplot (tested using v0.6.0)

# Steps
tar -zxvf 0_data.tar.gz # Extract the vcf files
sh 00_scripts/0_prepare_data/0_clean_files.sh; rm *.log
sh 00_scripts/0_prepare_data/1_make_your_beds.sh 2>&1 | tee -a 1_make_your_beds.log # convert output from caller to bed file with necessary data
sh 00_scripts/0_prepare_data/2_sort_cluster_beds.sh 2>&1 | tee -a 2_sort_cluster_beds.log # cluster variant calls to find duplicates
sh 00_scripts/0_prepare_data/3_decluster.sh 2>&1 | tee -a 3_decluster.log # Choose best variant call from calls with overlapping coords
bash 00_scripts/1_analyze_overlap/4_mask_sv_calls.sh | tee -a 4_mask_sv_calls.log # Mask svs that span repetitive regions
sh 00_scripts/1_analyze_overlap/5_get_gene_overlap.sh | tee -a 5_get_gene_overlap.log # Get SVs that span structural variants
sh 00_scripts/1_analyze_overlap/6_get_caller_overlap.sh | tee -a 6_get_caller_overlap.log # Get overlap between callers
sh 00_scripts/1_analyze_overlap/7_create_upset_plots.sh | tee -a 7_create_upset_plots.log # Create upset plots
