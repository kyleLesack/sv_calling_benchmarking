# Select best read among overlaps
find 1_processed_beds/1_includes_overlap/BreakDancer/ -type f -name "*.clustered.bed" | while read FILE ; do
	python3 00_scripts/0_prepare_data/get_best_calls.py ${FILE} breakdancer ;
done

find 1_processed_beds/1_includes_overlap/cnMOPS/ -type f -name "*.clustered.bed" | while read FILE ; do
	python3 00_scripts/0_prepare_data/get_best_calls.py ${FILE} cnmops ;
done

find 1_processed_beds/1_includes_overlap/CNVnator/ -type f -name "*.clustered.bed" | while read FILE ; do
	python3 00_scripts/0_prepare_data/get_best_calls.py ${FILE} cnvnator ;
done

find 1_processed_beds/1_includes_overlap/Delly/ -type f -name "*.clustered.bed" | while read FILE ; do
	python3 00_scripts/0_prepare_data/get_best_calls.py ${FILE} delly ;
done

find 1_processed_beds/1_includes_overlap/Hydra/ -type f -name "*.clustered.bed" | while read FILE ; do
	python3 00_scripts/0_prepare_data/get_best_calls.py ${FILE} hydra ;
done

find 1_processed_beds/1_includes_overlap/Lumpy/ -type f -name "*.clustered.bed" | while read FILE ; do
	python3 00_scripts/0_prepare_data/get_best_calls.py ${FILE} lumpy ;
done

find 1_processed_beds/1_includes_overlap/fusorsv/ -type f -name "*.clustered.bed" | while read FILE ; do
	python3 00_scripts/0_prepare_data/get_best_calls.py ${FILE} fusorsv ;
done
