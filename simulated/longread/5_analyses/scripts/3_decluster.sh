find variant_calls/pbsv/ -type f -name "*.clustered.bed" | while read FILE ; do
	python3 scripts/get_best_reads.py ${FILE} pbsv ;
done

find variant_calls/sniffles/ -type f -name "*.clustered.bed" | while read FILE ; do
	python3 scripts/get_best_reads.py ${FILE} sniffles ;
done

find variant_calls/svim/ -type f -name "*.clustered.bed" | while read FILE ; do
	python3 scripts/get_best_reads.py ${FILE} svim ;
done
