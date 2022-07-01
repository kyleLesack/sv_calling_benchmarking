# Sort beds
find 1_processed_beds -type f -name '*.bed' | while read FILE ; do
	myfile="$(echo ${FILE} | rev | cut -d '.' -f 2- | rev)" ;
	sort -k1,1 -k2,2n ${FILE} > ${myfile}.sorted.bed ;
done


# Cluster beds (SV calles with overlapping coordinates)
find 1_processed_beds -type f -name "*sorted.bed" | while read FILE ; do
	myfile="$(echo ${FILE}  | rev | cut -d '.' -f 2- | rev)" ;
	bedtools cluster -i ${FILE}  > ${myfile}.clustered.bed ;
done
