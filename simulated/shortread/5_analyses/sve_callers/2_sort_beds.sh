find . -mindepth 2 -type f -name 'Delly_deletions.bed' | while read FILE ; do
	newdir="$(echo ${FILE} | rev | cut -d '.' -f 2- | rev)" ;
	sort -k1,1 -k2,2n ${FILE} > ${newdir}.sorted.bed ;
done

find . -mindepth 2 -type f -name 'Delly_duplications.bed' | while read FILE ; do
	newdir="$(echo ${FILE} | rev | cut -d '.' -f 2- | rev)" ;
	sort -k1,1 -k2,2n ${FILE} > ${newdir}.sorted.bed ;
done


find . -mindepth 2 -type f -name 'Delly_inversions.bed' | while read FILE ; do
	newdir="$(echo ${FILE} | rev | cut -d '.' -f 2- | rev)" ;
	sort -k1,1 -k2,2n ${FILE} > ${newdir}.sorted.bed ;
done

####

find . -mindepth 2 -type f -name 'BreakDancer_deletions.bed' | while read FILE ; do
	newdir="$(echo ${FILE} | rev | cut -d '.' -f 2- | rev)" ;
	sort -k1,1 -k2,2n ${FILE} > ${newdir}.sorted.bed ;
done

find . -mindepth 2 -type f -name 'BreakDancer_duplications.bed' | while read FILE ; do
	newdir="$(echo ${FILE} | rev | cut -d '.' -f 2- | rev)" ;
	sort -k1,1 -k2,2n ${FILE} > ${newdir}.sorted.bed ;
done


find . -mindepth 2 -type f -name 'BreakDancer_inversions.bed' | while read FILE ; do
	newdir="$(echo ${FILE} | rev | cut -d '.' -f 2- | rev)" ;
	sort -k1,1 -k2,2n ${FILE} > ${newdir}.sorted.bed ;
done

####

find . -mindepth 2 -type f -name 'cnMOPS_deletions.bed' | while read FILE ; do
	newdir="$(echo ${FILE} | rev | cut -d '.' -f 2- | rev)" ;
	sort -k1,1 -k2,2n ${FILE} > ${newdir}.sorted.bed ;
done

find . -mindepth 2 -type f -name 'cnMOPS_duplications.bed' | while read FILE ; do
	newdir="$(echo ${FILE} | rev | cut -d '.' -f 2- | rev)" ;
	sort -k1,1 -k2,2n ${FILE} > ${newdir}.sorted.bed ;
done


find . -mindepth 2 -type f -name 'cnMOPS_inversions.bed' | while read FILE ; do
	newdir="$(echo ${FILE} | rev | cut -d '.' -f 2- | rev)" ;
	sort -k1,1 -k2,2n ${FILE} > ${newdir}.sorted.bed ;
done

####

find . -mindepth 2 -type f -name 'CNVnator_deletions.bed' | while read FILE ; do
	newdir="$(echo ${FILE} | rev | cut -d '.' -f 2- | rev)" ;
	sort -k1,1 -k2,2n ${FILE} > ${newdir}.sorted.bed ;
done

find . -mindepth 2 -type f -name 'CNVnator_duplications.bed' | while read FILE ; do
	newdir="$(echo ${FILE} | rev | cut -d '.' -f 2- | rev)" ;
	sort -k1,1 -k2,2n ${FILE} > ${newdir}.sorted.bed ;
done


find . -mindepth 2 -type f -name 'CNVnator_inversions.bed' | while read FILE ; do
	newdir="$(echo ${FILE} | rev | cut -d '.' -f 2- | rev)" ;
	sort -k1,1 -k2,2n ${FILE} > ${newdir}.sorted.bed ;
done

####

find . -mindepth 2 -type f -name 'Hydra_deletions.bed' | while read FILE ; do
	newdir="$(echo ${FILE} | rev | cut -d '.' -f 2- | rev)" ;
	sort -k1,1 -k2,2n ${FILE} > ${newdir}.sorted.bed ;
done

find . -mindepth 2 -type f -name 'Hydra_duplications.bed' | while read FILE ; do
	newdir="$(echo ${FILE} | rev | cut -d '.' -f 2- | rev)" ;
	sort -k1,1 -k2,2n ${FILE} > ${newdir}.sorted.bed ;
done


find . -mindepth 2 -type f -name 'Hydra_inversions.bed' | while read FILE ; do
	newdir="$(echo ${FILE} | rev | cut -d '.' -f 2- | rev)" ;
	sort -k1,1 -k2,2n ${FILE} > ${newdir}.sorted.bed ;
done

####

find . -mindepth 2 -type f -name 'Lumpy_deletions.bed' | while read FILE ; do
	newdir="$(echo ${FILE} | rev | cut -d '.' -f 2- | rev)" ;
	sort -k1,1 -k2,2n ${FILE} > ${newdir}.sorted.bed ;
done

find . -mindepth 2 -type f -name 'Lumpy_duplications.bed' | while read FILE ; do
	newdir="$(echo ${FILE} | rev | cut -d '.' -f 2- | rev)" ;
	sort -k1,1 -k2,2n ${FILE} > ${newdir}.sorted.bed ;
done


find . -mindepth 2 -type f -name 'Lumpy_inversions.bed' | while read FILE ; do
	newdir="$(echo ${FILE} | rev | cut -d '.' -f 2- | rev)" ;
	sort -k1,1 -k2,2n ${FILE} > ${newdir}.sorted.bed ;
done

####

find . -mindepth 2 -type f -name 'Tigra_deletions.bed' | while read FILE ; do
	newdir="$(echo ${FILE} | rev | cut -d '.' -f 2- | rev)" ;
	sort -k1,1 -k2,2n ${FILE} > ${newdir}.sorted.bed ;
done

find . -mindepth 2 -type f -name 'Tigra_duplications.bed' | while read FILE ; do
	newdir="$(echo ${FILE} | rev | cut -d '.' -f 2- | rev)" ;
	sort -k1,1 -k2,2n ${FILE} > ${newdir}.sorted.bed ;
done


find . -mindepth 2 -type f -name 'Tigra_inversions.bed' | while read FILE ; do
	newdir="$(echo ${FILE} | rev | cut -d '.' -f 2- | rev)" ;
	sort -k1,1 -k2,2n ${FILE} > ${newdir}.sorted.bed ;
done


