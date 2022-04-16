# Get variants that overlap with protein coding genes
find 1_processed_beds/2_variant_calls_declustered -type f -name "*declustered.bed" | while read FILE ; do
	myfile="$(echo ${FILE}  | rev | cut -d '.' -f 2- | rev)" ;
	bedtools intersect -wo -F 0.5 -a ${FILE} -b 0_data/0_annotations_masks_references/annotations/c_elegans.PRJNA13758.WBPS14.canonical_geneset-genes_only-protein_coding_only.bed | cut -f 1-4,8 > ${myfile}.spans_protein_coding.bed ;
done

# Sort beds
find 1_processed_beds/2_variant_calls_declustered -type f -name '*spans_protein_coding.bed' | while read FILE ; do
	myfile="$(echo ${FILE} | rev | cut -d '.' -f 2- | rev)" ;
	sort -k1,1 -k2,2n ${FILE} > ${myfile}.sorted.bed ;
done

# Cluster beds to find variant calls that overlap multiple genes
find  1_processed_beds/2_variant_calls_declustered -type f -name "*spans_protein_coding.sorted.bed" | while read FILE ; do
	myfile="$(echo ${FILE}  | rev | cut -d '.' -f 2- | rev)" ;
	bedtools cluster -i ${FILE}  > ${myfile}.clustered.bed ;
done

# Decluster beds (last column in the output bed file contains all of the genes overlapped)
find  1_processed_beds/2_variant_calls_declustered -type f -name "*spans_protein_coding.sorted.clustered.bed" | while read FILE ; do
	python3 00_scripts/0_prepare_data/decluster_protein_coding.py ${FILE} ;
done

mkdir -p 2_overlap_analysis
mv 1_processed_beds/3_variant_calls_spanning_genes 2_overlap_analysis/
