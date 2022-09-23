
find ./sv_calls -type d -name '*bedfiles' | while read FILE ; do
	mkdir -p ${FILE}/output;
	bedtools intersect -wao -a ${FILE}/fusor_deletions.bed -b ${FILE}/truth_deletions.bed > ${FILE}/output/del_fusor_in_truth.txt # TP, FP = fusor predicted wo overlaps;
	bedtools intersect -wao -a ${FILE}/truth_deletions.bed -b ${FILE}/fusor_deletions.bed > ${FILE}/output/del_truth_in_fusor.txt # TP, FN = in truth but no overlap in fusor;
	bedtools intersect -wao -a ${FILE}/fusor_deletions.bed -b ${FILE}/fusor_deletions.bed > ${FILE}/output/del_fusor_summary.txt # Overlap gives total bp predicted in fusor
	bedtools intersect -wao -a ${FILE}/truth_deletions.bed -b ${FILE}/truth_deletions.bed > ${FILE}/output/del_truth_summary.txt # Overlap gives total bp in training;
	bedtools intersect -wao -a ${FILE}/fusor_duplications.bed -b ${FILE}/truth_duplications.bed > ${FILE}/output/dup_fusor_in_truth.txt # TP, FP = fusor predicted wo overlaps;
	bedtools intersect -wao -a ${FILE}/truth_duplications.bed -b ${FILE}/fusor_duplications.bed > ${FILE}/output/dup_truth_in_fusor.txt # TP, FN = in truth but no overlap in fusor;
	bedtools intersect -wao -a ${FILE}/fusor_duplications.bed -b ${FILE}/fusor_duplications.bed > ${FILE}/output/dup_fusor_summary.txt # Overlap gives total bp predicted in fusor
	bedtools intersect -wao -a ${FILE}/truth_duplications.bed -b ${FILE}/truth_duplications.bed > ${FILE}/output/dup_truth_summary.txt # Overlap gives total bp in training;
	bedtools intersect -wao -a ${FILE}/fusor_inversions.bed -b ${FILE}/truth_inversions.bed > ${FILE}/output/inv_fusor_in_truth.txt # TP, FP = fusor predicted wo overlaps;
	bedtools intersect -wao -a ${FILE}/truth_inversions.bed -b ${FILE}/fusor_inversions.bed > ${FILE}/output/inv_truth_in_fusor.txt # TP, FN = in truth but no overlap in fusor;
	bedtools intersect -wao -a ${FILE}/fusor_inversions.bed -b ${FILE}/fusor_inversions.bed > ${FILE}/output/inv_fusor_summary.txt # Overlap gives total bp predicted in fusor
	bedtools intersect -wao -a ${FILE}/truth_inversions.bed -b ${FILE}/truth_inversions.bed > ${FILE}/output/inv_truth_summary.txt # Overlap gives total bp in training;
done
