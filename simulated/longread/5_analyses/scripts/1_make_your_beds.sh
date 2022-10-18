find variant_calls/sniffles -type f -name "*_S0.vcf" | while read FILE ; do
	myfile="$(echo ${FILE}  | rev | cut -d '_' -f 2- | rev)".vcf ;
	python3 scripts/convert2bed.py ${myfile} sniffles --minsize 100 --maxsize 500000 ;
	python3 scripts/convert2bed.py ${FILE} svsim --minsize 100 --maxsize 500000 ;
done

find variant_calls/pbsv -type f -name "*_S0.vcf" | while read FILE ; do
	myfile="$(echo ${FILE}  | rev | cut -d '_' -f 2- | rev)".vcf ;
	python3 scripts/convert2bed.py ${myfile} pbsv --minsize 100 --maxsize 500000 ;
	python3 scripts/convert2bed.py ${FILE} svsim --minsize 100 --maxsize 500000 ;
done

find variant_calls/svim -type f -name "*_S0.vcf" | while read FILE ; do
	myfile="$(echo ${FILE}  | rev | cut -d '_' -f 2- | rev)".vcf ;
	python3 scripts/convert2bed.py ${myfile} svim --minsize 100 --maxsize 500000 --min_qual_svim 2;
	python3 scripts/convert2bed.py ${FILE} svsim --minsize 100 --maxsize 500000 ;
done
