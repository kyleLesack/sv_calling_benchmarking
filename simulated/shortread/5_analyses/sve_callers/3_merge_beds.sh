find . -mindepth 2 -type f -name 'Delly_deletions.sorted.bed' | while read FILE ; do
	newdir="$(echo ${FILE}  | rev | cut -d '.' -f 2- | rev)" ;
	bedtools merge -i ${FILE}  > ${newdir}.merged.bed ;
done

find . -mindepth 2 -type f -name 'Delly_duplications.sorted.bed' | while read FILE ; do
	newdir="$(echo ${FILE}  | rev | cut -d '.' -f 2- | rev)" ;
	bedtools merge -i ${FILE}  > ${newdir}.merged.bed ;
done


find . -mindepth 2 -type f -name 'Delly_inversions.sorted.bed' | while read FILE ; do
	newdir="$(echo ${FILE}  | rev | cut -d '.' -f 2- | rev)" ;
	bedtools merge -i ${FILE}  > ${newdir}.merged.bed ;
done

####

find . -mindepth 2 -type f -name 'BreakDancer_deletions.sorted.bed' | while read FILE ; do
	newdir="$(echo ${FILE}  | rev | cut -d '.' -f 2- | rev)" ;
	bedtools merge -i ${FILE}  > ${newdir}.merged.bed ;
done

find . -mindepth 2 -type f -name 'BreakDancer_duplications.sorted.bed' | while read FILE ; do
	newdir="$(echo ${FILE}  | rev | cut -d '.' -f 2- | rev)" ;
	bedtools merge -i ${FILE}  > ${newdir}.merged.bed ;
done


find . -mindepth 2 -type f -name 'BreakDancer_inversions.sorted.bed' | while read FILE ; do
	newdir="$(echo ${FILE}  | rev | cut -d '.' -f 2- | rev)" ;
	bedtools merge -i ${FILE}  > ${newdir}.merged.bed ;
done

####

find . -mindepth 2 -type f -name 'cnMOPS_deletions.sorted.bed' | while read FILE ; do
	newdir="$(echo ${FILE}  | rev | cut -d '.' -f 2- | rev)" ;
	bedtools merge -i ${FILE}  > ${newdir}.merged.bed ;
done

find . -mindepth 2 -type f -name 'cnMOPS_duplications.sorted.bed' | while read FILE ; do
	newdir="$(echo ${FILE}  | rev | cut -d '.' -f 2- | rev)" ;
	bedtools merge -i ${FILE}  > ${newdir}.merged.bed ;
done


find . -mindepth 2 -type f -name 'cnMOPS_inversions.sorted.bed' | while read FILE ; do
	newdir="$(echo ${FILE}  | rev | cut -d '.' -f 2- | rev)" ;
	bedtools merge -i ${FILE}  > ${newdir}.merged.bed ;
done

####

find . -mindepth 2 -type f -name 'CNVnator_deletions.sorted.bed' | while read FILE ; do
	newdir="$(echo ${FILE}  | rev | cut -d '.' -f 2- | rev)" ;
	bedtools merge -i ${FILE}  > ${newdir}.merged.bed ;
done

find . -mindepth 2 -type f -name 'CNVnator_duplications.sorted.bed' | while read FILE ; do
	newdir="$(echo ${FILE}  | rev | cut -d '.' -f 2- | rev)" ;
	bedtools merge -i ${FILE}  > ${newdir}.merged.bed ;
done


find . -mindepth 2 -type f -name 'CNVnator_inversions.sorted.bed' | while read FILE ; do
	newdir="$(echo ${FILE}  | rev | cut -d '.' -f 2- | rev)" ;
	bedtools merge -i ${FILE}  > ${newdir}.merged.bed ;
done

####

find . -mindepth 2 -type f -name 'Hydra_deletions.sorted.bed' | while read FILE ; do
	newdir="$(echo ${FILE}  | rev | cut -d '.' -f 2- | rev)" ;
	bedtools merge -i ${FILE}  > ${newdir}.merged.bed ;
done

find . -mindepth 2 -type f -name 'Hydra_duplications.sorted.bed' | while read FILE ; do
	newdir="$(echo ${FILE}  | rev | cut -d '.' -f 2- | rev)" ;
	bedtools merge -i ${FILE}  > ${newdir}.merged.bed ;
done


find . -mindepth 2 -type f -name 'Hydra_inversions.sorted.bed' | while read FILE ; do
	newdir="$(echo ${FILE}  | rev | cut -d '.' -f 2- | rev)" ;
	bedtools merge -i ${FILE}  > ${newdir}.merged.bed ;
done

####

find . -mindepth 2 -type f -name 'Lumpy_deletions.sorted.bed' | while read FILE ; do
	newdir="$(echo ${FILE}  | rev | cut -d '.' -f 2- | rev)" ;
	bedtools merge -i ${FILE}  > ${newdir}.merged.bed ;
done

find . -mindepth 2 -type f -name 'Lumpy_duplications.sorted.bed' | while read FILE ; do
	newdir="$(echo ${FILE}  | rev | cut -d '.' -f 2- | rev)" ;
	bedtools merge -i ${FILE}  > ${newdir}.merged.bed ;
done


find . -mindepth 2 -type f -name 'Lumpy_inversions.sorted.bed' | while read FILE ; do
	newdir="$(echo ${FILE}  | rev | cut -d '.' -f 2- | rev)" ;
	bedtools merge -i ${FILE}  > ${newdir}.merged.bed ;
done
