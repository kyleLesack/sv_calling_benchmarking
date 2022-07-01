find 0_data/1_variant_calls/sniffles_ngmlr/ -type f -name '*.vcf' | while read FILE ; do
	python3 00_scripts/0_prepare_data/convert2bed.py ${FILE} sniffles --minsize 100 --maxsize 500000 ;
done

find 0_data/1_variant_calls/pbsv_pbmm2/repeat_annotated -type f -name '*.vcf' | while read FILE ; do
	python3 00_scripts/0_prepare_data/convert2bed.py ${FILE} pbsv --minsize 100 --maxsize 500000 ;
done

find 0_data/1_variant_calls/svim_ngmlr/ -type f -name '*.vcf' | while read FILE ; do
	#python3 00_scripts/0_prepare_data/convert2bed.py ${FILE} svim --minsize 100 --maxsize 500000 --min_qual_svim 10 ;
	python3 00_scripts/0_prepare_data/convert2bed.py ${FILE} svim --minsize 100 --maxsize 500000 --min_qual_svim 15 ;
done

find 0_data/1_variant_calls/mumandco_v3/ -type f -name '*.tsv' | while read FILE ; do
	python3 00_scripts/0_prepare_data/convert2bed.py ${FILE} mumandco --minsize 100 --maxsize 500000 ;
done

# NOTE: The Assemblytics authors don't recommend using it to call large variants. To limit the Assemblytics analysis to 50kbp, uncomment the following lines.
find 0_data/1_variant_calls/assemblytics_mummer4_canu/ -type f -name '*50k*.bed' | while read FILE ; do
	python3 00_scripts/0_prepare_data/convert2bed.py ${FILE} assemblytics --minsize 100 --maxsize 50000 ;
done

# NOTE: The Assemblytics authors don't recommend using it to call large variants. To limit the Assemblytics analysis to 500kbp, uncomment the following lines.
#find 0_data/1_variant_calls/assemblytics_mummer4_canu/ -type f -name '*1M*.bed' | while read FILE ; do
#	python3 00_scripts/0_prepare_data/convert2bed.py ${FILE} assemblytics --minsize 100 --maxsize 500000 ;
#done
