# cnMOPS
find sve_calls/cnMOPS -type d -name '*bedfiles' | while read FILE ; do
	mkdir -p ${FILE}/output;
	bedtools intersect -f 0.50 -r -wao -a ${FILE}/cnMOPS_deletions.sorted.merged.bed -b ${FILE}/truth_deletions.bed > ${FILE}/output/del_cnMOPS_in_truth.txt # TP, FP = cnMOPS predicted wo overlaps;
	bedtools intersect -f 0.50 -r -wao -a ${FILE}/truth_deletions.bed -b ${FILE}/cnMOPS_deletions.sorted.merged.bed > ${FILE}/output/del_truth_in_cnMOPS.txt # TP, FN = in truth but no overlap in cnMOPS;
	bedtools intersect -f 0.50 -r -wao -a ${FILE}/cnMOPS_deletions.sorted.merged.bed -b ${FILE}/cnMOPS_deletions.sorted.merged.bed > ${FILE}/output/del_cnMOPS_summary.txt # Overlap gives total bp predicted in cnMOPS
	bedtools intersect -f 0.50 -r -wao -a ${FILE}/truth_deletions.bed -b ${FILE}/truth_deletions.bed > ${FILE}/output/del_truth_summary.txt # Overlap gives total bp in training;
	bedtools intersect -f 0.50 -r -wao -a ${FILE}/cnMOPS_duplications.sorted.merged.bed -b ${FILE}/truth_duplications.bed > ${FILE}/output/dup_cnMOPS_in_truth.txt # TP, FP = cnMOPS predicted wo overlaps;
	bedtools intersect -f 0.50 -r -wao -a ${FILE}/truth_duplications.bed -b ${FILE}/cnMOPS_duplications.sorted.merged.bed > ${FILE}/output/dup_truth_in_cnMOPS.txt # TP, FN = in truth but no overlap in cnMOPS;
	bedtools intersect -f 0.50 -r -wao -a ${FILE}/cnMOPS_duplications.sorted.merged.bed -b ${FILE}/cnMOPS_duplications.sorted.merged.bed > ${FILE}/output/dup_cnMOPS_summary.txt # Overlap gives total bp predicted in cnMOPS
	bedtools intersect -f 0.50 -r -wao -a ${FILE}/truth_duplications.bed -b ${FILE}/truth_duplications.bed > ${FILE}/output/dup_truth_summary.txt # Overlap gives total bp in training;
	bedtools intersect -f 0.50 -r -wao -a ${FILE}/cnMOPS_inversions.sorted.merged.bed -b ${FILE}/truth_inversions.bed > ${FILE}/output/inv_cnMOPS_in_truth.txt # TP, FP = cnMOPS predicted wo overlaps;
	bedtools intersect -f 0.50 -r -wao -a ${FILE}/truth_inversions.bed -b ${FILE}/cnMOPS_inversions.sorted.merged.bed > ${FILE}/output/inv_truth_in_cnMOPS.txt # TP, FN = in truth but no overlap in cnMOPS;
	bedtools intersect -f 0.50 -r -wao -a ${FILE}/cnMOPS_inversions.sorted.merged.bed -b ${FILE}/cnMOPS_inversions.sorted.merged.bed > ${FILE}/output/inv_cnMOPS_summary.txt # Overlap gives total bp predicted in cnMOPS
	bedtools intersect -f 0.50 -r -wao -a ${FILE}/truth_inversions.bed -b ${FILE}/truth_inversions.bed > ${FILE}/output/inv_truth_summary.txt # Overlap gives total bp in training;
done

# Breakdancer

find sve_calls/BreakDancer -type d -name '*bedfiles' | while read FILE ; do
	mkdir -p ${FILE}/output;
	bedtools intersect -f 0.50 -r -wao -a ${FILE}/BreakDancer_deletions.sorted.merged.bed -b ${FILE}/truth_deletions.bed > ${FILE}/output/del_BreakDancer_in_truth.txt # TP, FP = BreakDancer predicted wo overlaps;
	bedtools intersect -f 0.50 -r -wao -a ${FILE}/truth_deletions.bed -b ${FILE}/BreakDancer_deletions.sorted.merged.bed > ${FILE}/output/del_truth_in_BreakDancer.txt # TP, FN = in truth but no overlap in BreakDancer;
	bedtools intersect -f 0.50 -r -wao -a ${FILE}/BreakDancer_deletions.sorted.merged.bed -b ${FILE}/BreakDancer_deletions.sorted.merged.bed > ${FILE}/output/del_BreakDancer_summary.txt # Overlap gives total bp predicted in BreakDancer
	bedtools intersect -f 0.50 -r -wao -a ${FILE}/truth_deletions.bed -b ${FILE}/truth_deletions.bed > ${FILE}/output/del_truth_summary.txt # Overlap gives total bp in training;
	bedtools intersect -f 0.50 -r -wao -a ${FILE}/BreakDancer_duplications.sorted.merged.bed -b ${FILE}/truth_duplications.bed > ${FILE}/output/dup_BreakDancer_in_truth.txt # TP, FP = BreakDancer predicted wo overlaps;
	bedtools intersect -f 0.50 -r -wao -a ${FILE}/truth_duplications.bed -b ${FILE}/BreakDancer_duplications.sorted.merged.bed > ${FILE}/output/dup_truth_in_BreakDancer.txt # TP, FN = in truth but no overlap in BreakDancer;
	bedtools intersect -f 0.50 -r -wao -a ${FILE}/BreakDancer_duplications.sorted.merged.bed -b ${FILE}/BreakDancer_duplications.sorted.merged.bed > ${FILE}/output/dup_BreakDancer_summary.txt # Overlap gives total bp predicted in BreakDancer
	bedtools intersect -f 0.50 -r -wao -a ${FILE}/truth_duplications.bed -b ${FILE}/truth_duplications.bed > ${FILE}/output/dup_truth_summary.txt # Overlap gives total bp in training;
	bedtools intersect -f 0.50 -r -wao -a ${FILE}/BreakDancer_inversions.sorted.merged.bed -b ${FILE}/truth_inversions.bed > ${FILE}/output/inv_BreakDancer_in_truth.txt # TP, FP = BreakDancer predicted wo overlaps;
	bedtools intersect -f 0.50 -r -wao -a ${FILE}/truth_inversions.bed -b ${FILE}/BreakDancer_inversions.sorted.merged.bed > ${FILE}/output/inv_truth_in_BreakDancer.txt # TP, FN = in truth but no overlap in BreakDancer;
	bedtools intersect -f 0.50 -r -wao -a ${FILE}/BreakDancer_inversions.sorted.merged.bed -b ${FILE}/BreakDancer_inversions.sorted.merged.bed > ${FILE}/output/inv_BreakDancer_summary.txt # Overlap gives total bp predicted in BreakDancer
	bedtools intersect -f 0.50 -r -wao -a ${FILE}/truth_inversions.bed -b ${FILE}/truth_inversions.bed > ${FILE}/output/inv_truth_summary.txt # Overlap gives total bp in training;
done

# CNVnator

find sve_calls/CNVnator -type d -name '*bedfiles' | while read FILE ; do
	mkdir -p ${FILE}/output;
	bedtools intersect -f 0.50 -r -wao -a ${FILE}/CNVnator_deletions.sorted.merged.bed -b ${FILE}/truth_deletions.bed > ${FILE}/output/del_CNVnator_in_truth.txt # TP, FP = CNVnator predicted wo overlaps;
	bedtools intersect -f 0.50 -r -wao -a ${FILE}/truth_deletions.bed -b ${FILE}/CNVnator_deletions.sorted.merged.bed > ${FILE}/output/del_truth_in_CNVnator.txt # TP, FN = in truth but no overlap in CNVnator;
	bedtools intersect -f 0.50 -r -wao -a ${FILE}/CNVnator_deletions.sorted.merged.bed -b ${FILE}/CNVnator_deletions.sorted.merged.bed > ${FILE}/output/del_CNVnator_summary.txt # Overlap gives total bp predicted in CNVnator
	bedtools intersect -f 0.50 -r -wao -a ${FILE}/truth_deletions.bed -b ${FILE}/truth_deletions.bed > ${FILE}/output/del_truth_summary.txt # Overlap gives total bp in training;
	bedtools intersect -f 0.50 -r -wao -a ${FILE}/CNVnator_duplications.sorted.merged.bed -b ${FILE}/truth_duplications.bed > ${FILE}/output/dup_CNVnator_in_truth.txt # TP, FP = CNVnator predicted wo overlaps;
	bedtools intersect -f 0.50 -r -wao -a ${FILE}/truth_duplications.bed -b ${FILE}/CNVnator_duplications.sorted.merged.bed > ${FILE}/output/dup_truth_in_CNVnator.txt # TP, FN = in truth but no overlap in CNVnator;
	bedtools intersect -f 0.50 -r -wao -a ${FILE}/CNVnator_duplications.sorted.merged.bed -b ${FILE}/CNVnator_duplications.sorted.merged.bed > ${FILE}/output/dup_CNVnator_summary.txt # Overlap gives total bp predicted in CNVnator
	bedtools intersect -f 0.50 -r -wao -a ${FILE}/truth_duplications.bed -b ${FILE}/truth_duplications.bed > ${FILE}/output/dup_truth_summary.txt # Overlap gives total bp in training;
	bedtools intersect -f 0.50 -r -wao -a ${FILE}/CNVnator_inversions.sorted.merged.bed -b ${FILE}/truth_inversions.bed > ${FILE}/output/inv_CNVnator_in_truth.txt # TP, FP = CNVnator predicted wo overlaps;
	bedtools intersect -f 0.50 -r -wao -a ${FILE}/truth_inversions.bed -b ${FILE}/CNVnator_inversions.sorted.merged.bed > ${FILE}/output/inv_truth_in_CNVnator.txt # TP, FN = in truth but no overlap in CNVnator;
	bedtools intersect -f 0.50 -r -wao -a ${FILE}/CNVnator_inversions.sorted.merged.bed -b ${FILE}/CNVnator_inversions.sorted.merged.bed > ${FILE}/output/inv_CNVnator_summary.txt # Overlap gives total bp predicted in CNVnator
	bedtools intersect -f 0.50 -r -wao -a ${FILE}/truth_inversions.bed -b ${FILE}/truth_inversions.bed > ${FILE}/output/inv_truth_summary.txt # Overlap gives total bp in training;
done

# Delly
find sve_calls/Delly -type d -name '*bedfiles' | while read FILE ; do
	mkdir -p ${FILE}/output;
	bedtools intersect -f 0.50 -r -wao -a ${FILE}/Delly_deletions.sorted.merged.bed -b ${FILE}/truth_deletions.bed > ${FILE}/output/del_Delly_in_truth.txt # TP, FP = Delly predicted wo overlaps;
	bedtools intersect -f 0.50 -r -wao -a ${FILE}/truth_deletions.bed -b ${FILE}/Delly_deletions.sorted.merged.bed > ${FILE}/output/del_truth_in_Delly.txt # TP, FN = in truth but no overlap in Delly;
	bedtools intersect -f 0.50 -r -wao -a ${FILE}/Delly_deletions.sorted.merged.bed -b ${FILE}/Delly_deletions.sorted.merged.bed > ${FILE}/output/del_Delly_summary.txt # Overlap gives total bp predicted in Delly
	bedtools intersect -f 0.50 -r -wao -a ${FILE}/truth_deletions.bed -b ${FILE}/truth_deletions.bed > ${FILE}/output/del_truth_summary.txt # Overlap gives total bp in training;
	bedtools intersect -f 0.50 -r -wao -a ${FILE}/Delly_duplications.sorted.merged.bed -b ${FILE}/truth_duplications.bed > ${FILE}/output/dup_Delly_in_truth.txt # TP, FP = Delly predicted wo overlaps;
	bedtools intersect -f 0.50 -r -wao -a ${FILE}/truth_duplications.bed -b ${FILE}/Delly_duplications.sorted.merged.bed > ${FILE}/output/dup_truth_in_Delly.txt # TP, FN = in truth but no overlap in Delly;
	bedtools intersect -f 0.50 -r -wao -a ${FILE}/Delly_duplications.sorted.merged.bed -b ${FILE}/Delly_duplications.sorted.merged.bed > ${FILE}/output/dup_Delly_summary.txt # Overlap gives total bp predicted in Delly
	bedtools intersect -f 0.50 -r -wao -a ${FILE}/truth_duplications.bed -b ${FILE}/truth_duplications.bed > ${FILE}/output/dup_truth_summary.txt # Overlap gives total bp in training;
	bedtools intersect -f 0.50 -r -wao -a ${FILE}/Delly_inversions.sorted.merged.bed -b ${FILE}/truth_inversions.bed > ${FILE}/output/inv_Delly_in_truth.txt # TP, FP = Delly predicted wo overlaps;
	bedtools intersect -f 0.50 -r -wao -a ${FILE}/truth_inversions.bed -b ${FILE}/Delly_inversions.sorted.merged.bed > ${FILE}/output/inv_truth_in_Delly.txt # TP, FN = in truth but no overlap in Delly;
	bedtools intersect -f 0.50 -r -wao -a ${FILE}/Delly_inversions.sorted.merged.bed -b ${FILE}/Delly_inversions.sorted.merged.bed > ${FILE}/output/inv_Delly_summary.txt # Overlap gives total bp predicted in Delly
	bedtools intersect -f 0.50 -r -wao -a ${FILE}/truth_inversions.bed -b ${FILE}/truth_inversions.bed > ${FILE}/output/inv_truth_summary.txt # Overlap gives total bp in training;
done


# Hydra
find sve_calls/Hydra -type d -name '*bedfiles' | while read FILE ; do
	mkdir -p ${FILE}/output;
	bedtools intersect -f 0.50 -r -wao -a ${FILE}/Hydra_deletions.sorted.merged.bed -b ${FILE}/truth_deletions.bed > ${FILE}/output/del_Hydra_in_truth.txt # TP, FP = Hydra predicted wo overlaps;
	bedtools intersect -f 0.50 -r -wao -a ${FILE}/truth_deletions.bed -b ${FILE}/Hydra_deletions.sorted.merged.bed > ${FILE}/output/del_truth_in_Hydra.txt # TP, FN = in truth but no overlap in Hydra;
	bedtools intersect -f 0.50 -r -wao -a ${FILE}/Hydra_deletions.sorted.merged.bed -b ${FILE}/Hydra_deletions.sorted.merged.bed > ${FILE}/output/del_Hydra_summary.txt # Overlap gives total bp predicted in Hydra
	bedtools intersect -f 0.50 -r -wao -a ${FILE}/truth_deletions.bed -b ${FILE}/truth_deletions.bed > ${FILE}/output/del_truth_summary.txt # Overlap gives total bp in training;
	bedtools intersect -f 0.50 -r -wao -a ${FILE}/Hydra_duplications.sorted.merged.bed -b ${FILE}/truth_duplications.bed > ${FILE}/output/dup_Hydra_in_truth.txt # TP, FP = Hydra predicted wo overlaps;
	bedtools intersect -f 0.50 -r -wao -a ${FILE}/truth_duplications.bed -b ${FILE}/Hydra_duplications.sorted.merged.bed > ${FILE}/output/dup_truth_in_Hydra.txt # TP, FN = in truth but no overlap in Hydra;
	bedtools intersect -f 0.50 -r -wao -a ${FILE}/Hydra_duplications.sorted.merged.bed -b ${FILE}/Hydra_duplications.sorted.merged.bed > ${FILE}/output/dup_Hydra_summary.txt # Overlap gives total bp predicted in Hydra
	bedtools intersect -f 0.50 -r -wao -a ${FILE}/truth_duplications.bed -b ${FILE}/truth_duplications.bed > ${FILE}/output/dup_truth_summary.txt # Overlap gives total bp in training;
	bedtools intersect -f 0.50 -r -wao -a ${FILE}/Hydra_inversions.sorted.merged.bed -b ${FILE}/truth_inversions.bed > ${FILE}/output/inv_Hydra_in_truth.txt # TP, FP = Hydra predicted wo overlaps;
	bedtools intersect -f 0.50 -r -wao -a ${FILE}/truth_inversions.bed -b ${FILE}/Hydra_inversions.sorted.merged.bed > ${FILE}/output/inv_truth_in_Hydra.txt # TP, FN = in truth but no overlap in Hydra;
	bedtools intersect -f 0.50 -r -wao -a ${FILE}/Hydra_inversions.sorted.merged.bed -b ${FILE}/Hydra_inversions.sorted.merged.bed > ${FILE}/output/inv_Hydra_summary.txt # Overlap gives total bp predicted in Hydra
	bedtools intersect -f 0.50 -r -wao -a ${FILE}/truth_inversions.bed -b ${FILE}/truth_inversions.bed > ${FILE}/output/inv_truth_summary.txt # Overlap gives total bp in training;
done

# Lumpy
find sve_calls/Lumpy -type d -name '*bedfiles' | while read FILE ; do
	mkdir -p ${FILE}/output;
	bedtools intersect -f 0.50 -r -wao -a ${FILE}/Lumpy_deletions.sorted.merged.bed -b ${FILE}/truth_deletions.bed > ${FILE}/output/del_Lumpy_in_truth.txt # TP, FP = Lumpy predicted wo overlaps;
	bedtools intersect -f 0.50 -r -wao -a ${FILE}/truth_deletions.bed -b ${FILE}/Lumpy_deletions.sorted.merged.bed > ${FILE}/output/del_truth_in_Lumpy.txt # TP, FN = in truth but no overlap in Lumpy;
	bedtools intersect -f 0.50 -r -wao -a ${FILE}/Lumpy_deletions.sorted.merged.bed -b ${FILE}/Lumpy_deletions.sorted.merged.bed > ${FILE}/output/del_Lumpy_summary.txt # Overlap gives total bp predicted in Lumpy
	bedtools intersect -f 0.50 -r -wao -a ${FILE}/truth_deletions.bed -b ${FILE}/truth_deletions.bed > ${FILE}/output/del_truth_summary.txt # Overlap gives total bp in training;
	bedtools intersect -f 0.50 -r -wao -a ${FILE}/Lumpy_duplications.sorted.merged.bed -b ${FILE}/truth_duplications.bed > ${FILE}/output/dup_Lumpy_in_truth.txt # TP, FP = Lumpy predicted wo overlaps;
	bedtools intersect -f 0.50 -r -wao -a ${FILE}/truth_duplications.bed -b ${FILE}/Lumpy_duplications.sorted.merged.bed > ${FILE}/output/dup_truth_in_Lumpy.txt # TP, FN = in truth but no overlap in Lumpy;
	bedtools intersect -f 0.50 -r -wao -a ${FILE}/Lumpy_duplications.sorted.merged.bed -b ${FILE}/Lumpy_duplications.sorted.merged.bed > ${FILE}/output/dup_Lumpy_summary.txt # Overlap gives total bp predicted in Lumpy
	bedtools intersect -f 0.50 -r -wao -a ${FILE}/truth_duplications.bed -b ${FILE}/truth_duplications.bed > ${FILE}/output/dup_truth_summary.txt # Overlap gives total bp in training;
	bedtools intersect -f 0.50 -r -wao -a ${FILE}/Lumpy_inversions.sorted.merged.bed -b ${FILE}/truth_inversions.bed > ${FILE}/output/inv_Lumpy_in_truth.txt # TP, FP = Lumpy predicted wo overlaps;
	bedtools intersect -f 0.50 -r -wao -a ${FILE}/truth_inversions.bed -b ${FILE}/Lumpy_inversions.sorted.merged.bed > ${FILE}/output/inv_truth_in_Lumpy.txt # TP, FN = in truth but no overlap in Lumpy;
	bedtools intersect -f 0.50 -r -wao -a ${FILE}/Lumpy_inversions.sorted.merged.bed -b ${FILE}/Lumpy_inversions.sorted.merged.bed > ${FILE}/output/inv_Lumpy_summary.txt # Overlap gives total bp predicted in Lumpy
	bedtools intersect -f 0.50 -r -wao -a ${FILE}/truth_inversions.bed -b ${FILE}/truth_inversions.bed > ${FILE}/output/inv_truth_summary.txt # Overlap gives total bp in training;
done
