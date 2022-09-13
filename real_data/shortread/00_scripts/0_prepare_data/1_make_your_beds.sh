find 0_data/1_variant_calls/BreakDancer/ -type f -name '*S4.vcf' | while read FILE ; do
	python3 00_scripts/0_prepare_data/convert2bed.py ${FILE} breakdancer --minsize 100 --maxsize 500000 ;
done

find 0_data/1_variant_calls/cnMOPS/ -type f -name '*S9.vcf' | while read FILE ; do
	python3 00_scripts/0_prepare_data/convert2bed.py ${FILE} cnmops --minsize 100 --maxsize 500000 ;
done

find 0_data/1_variant_calls/CNVnator/ -type f -name '*S10.vcf' | while read FILE ; do
	python3 00_scripts/0_prepare_data/convert2bed.py ${FILE} cnvnator --minsize 100 --maxsize 500000 ;
done

find 0_data/1_variant_calls/Delly/ -type f -name '*S11.vcf' | while read FILE ; do
	python3 00_scripts/0_prepare_data/convert2bed.py ${FILE} delly --minsize 100 --maxsize 500000 ;
done

find 0_data/1_variant_calls/Hydra/ -type f -name '*S17.vcf' | while read FILE ; do
	python3 00_scripts/0_prepare_data/convert2bed.py ${FILE} hydra --minsize 100 --maxsize 500000 ;
done

find 0_data/1_variant_calls/Lumpy/ -type f -name '*S18.vcf' | while read FILE ; do
	python3 00_scripts/0_prepare_data/convert2bed.py ${FILE} lumpy --minsize 100 --maxsize 500000 ;
done

find 0_data/1_variant_calls/fusorsv -type f -name '*S-1.vcf' | while read FILE ; do
	python3 00_scripts/0_prepare_data/convert2bed.py ${FILE} fusorsv --minsize 100 --maxsize 500000 ;
done
