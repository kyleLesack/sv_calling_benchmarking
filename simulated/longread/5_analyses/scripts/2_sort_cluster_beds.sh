# Sort beds
find variant_calls -type f -name '*.bed' | while read FILE ; do
	myfile="$(echo ${FILE} | rev | cut -d '.' -f 2- | rev)" ;
	sort -k1,1 -k2,2n ${FILE} > ${myfile}.sorted.bed ;
done

# Cluster beds
find variant_calls -type f -name "*sorted.bed" | while read FILE ; do
	myfile="$(echo ${FILE}  | rev | cut -d '.' -f 2- | rev)" ;
	bedtools cluster -i ${FILE}  > ${myfile}.clustered.bed ;
done

# Remove unneeded files
find variant_calls -type f -name "*S0_*.sorted.clustered.bed" -exec rm {} \;
