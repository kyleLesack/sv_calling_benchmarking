# Select best read among overlaps
find 1_processed_beds/1_includes_overlap/assemblytics_mummer4_canu/ -type f -name "*.clustered.bed" | while read FILE ; do
	python3 00_scripts/0_prepare_data/get_best_reads.py ${FILE} assemblytics ;
done

find 1_processed_beds/1_includes_overlap/mumandco_v3/ -type f -name "*.clustered.bed" | while read FILE ; do
	python3 00_scripts/0_prepare_data/get_best_reads.py ${FILE} mumandco ;
done

find 1_processed_beds/1_includes_overlap/pbsv_pbmm2/ -type f -name "*.clustered.bed" | while read FILE ; do
	python3 00_scripts/0_prepare_data/get_best_reads.py ${FILE} pbsv ;
done

find 1_processed_beds/1_includes_overlap/sniffles_ngmlr/ -type f -name "*.clustered.bed" | while read FILE ; do
	python3 00_scripts/0_prepare_data/get_best_reads.py ${FILE} sniffles ;
done

find 1_processed_beds/1_includes_overlap/svim_ngmlr/ -type f -name "*.clustered.bed" | while read FILE ; do
	python3 00_scripts/0_prepare_data/get_best_reads.py ${FILE} svim ;
done

find 1_processed_beds/1_includes_overlap/fusorsv/ -type f -name "*.clustered.bed" | while read FILE ; do
	python3 00_scripts/0_prepare_data/get_best_reads.py ${FILE} fusorsv ;
done
