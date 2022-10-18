# Find bedtools clustered bedfiles and get the number of predicted variants and number of clusters

find variant_calls/pbsv -type f -name "*DEL.sorted.clustered.bed" | while read FILE ; do
	myfile="$(echo ${FILE}  | rev | cut -d '_' -f 2- | rev)".discarded_deletion_stats.txt ;
	echo -n "Total predicted deletions: " > ${myfile};
	cat ${FILE} | wc -l >> ${myfile};
	echo -n "Total deletion clusters: " >> ${myfile};
	cat ${FILE} | cut -f 7 | sort -u | wc -l >> ${myfile};
done

find variant_calls/pbsv -type f -name "*DUP.sorted.clustered.bed" | while read FILE ; do
	myfile="$(echo ${FILE}  | rev | cut -d '_' -f 2- | rev)".discarded_duplication_stats.txt ;
	echo -n "Total predicted duplications: " > ${myfile};
	cat ${FILE} | wc -l >> ${myfile};
	echo -n "Total duplication clusters: " >> ${myfile};
	cat ${FILE} | cut -f 7 | sort -u | wc -l >> ${myfile};
done

find variant_calls/pbsv -type f -name "*INV.sorted.clustered.bed" | while read FILE ; do
	myfile="$(echo ${FILE}  | rev | cut -d '_' -f 2- | rev)".discarded_inversion_stats.txt ;
	echo -n "Total inversion variants: " > ${myfile};
	cat ${FILE} | wc -l >> ${myfile};
	echo -n "Total inversion clusters: " >> ${myfile};
	cat ${FILE} | cut -f 7 | sort -u | wc -l >> ${myfile};
done

# Sniffles
find variant_calls/sniffles -type f -name "*DEL.sorted.clustered.bed" | while read FILE ; do
	myfile="$(echo ${FILE}  | rev | cut -d '_' -f 2- | rev)".discarded_deletion_stats.txt ;
	echo -n "Total predicted deletions: " > ${myfile};
	cat ${FILE} | wc -l >> ${myfile};
	echo -n "Total deletion clusters: " >> ${myfile};
	cat ${FILE} | cut -f 7 | sort -u | wc -l >> ${myfile};
done

find variant_calls/sniffles -type f -name "*DUP.sorted.clustered.bed" | while read FILE ; do
	myfile="$(echo ${FILE}  | rev | cut -d '_' -f 2- | rev)".discarded_duplication_stats.txt ;
	echo -n "Total predicted duplications: " > ${myfile};
	cat ${FILE} | wc -l >> ${myfile};
	echo -n "Total duplication clusters: " >> ${myfile};
	cat ${FILE} | cut -f 7 | sort -u | wc -l >> ${myfile};
done

find variant_calls/sniffles -type f -name "*INV.sorted.clustered.bed" | while read FILE ; do
	myfile="$(echo ${FILE}  | rev | cut -d '_' -f 2- | rev)".discarded_inversion_stats.txt ;
	echo -n "Total inversion variants: " > ${myfile};
	cat ${FILE} | wc -l >> ${myfile};
	echo -n "Total inversion clusters: " >> ${myfile};
	cat ${FILE} | cut -f 7 | sort -u | wc -l >> ${myfile};
done

# SVIM
find variant_calls/svim -type f -name "*DEL.sorted.clustered.bed" | while read FILE ; do
	myfile="$(echo ${FILE}  | rev | cut -d '_' -f 2- | rev)".discarded_deletion_stats.txt ;
	echo -n "Total predicted deletions: " > ${myfile};
	cat ${FILE} | wc -l >> ${myfile};
	echo -n "Total deletion clusters: " >> ${myfile};
	cat ${FILE} | cut -f 7 | sort -u | wc -l >> ${myfile};
done

find variant_calls/svim -type f -name "*DUP.sorted.clustered.bed" | while read FILE ; do
	myfile="$(echo ${FILE}  | rev | cut -d '_' -f 2- | rev)".discarded_duplication_stats.txt ;
	echo -n "Total predicted duplications: " > ${myfile};
	cat ${FILE} | wc -l >> ${myfile};
	echo -n "Total duplication clusters: " >> ${myfile};
	cat ${FILE} | cut -f 7 | sort -u | wc -l >> ${myfile};
done

find variant_calls/svim -type f -name "*INV.sorted.clustered.bed" | while read FILE ; do
	myfile="$(echo ${FILE}  | rev | cut -d '_' -f 2- | rev)".discarded_inversion_stats.txt ;
	echo -n "Total inversion variants: " > ${myfile};
	cat ${FILE} | wc -l >> ${myfile};
	echo -n "Total inversion clusters: " >> ${myfile};
	cat ${FILE} | cut -f 7 | sort -u | wc -l >> ${myfile};
done
