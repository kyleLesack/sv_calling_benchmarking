mkdir -p analysis/BreakDancer
mkdir -p analysis/cnMOPS
mkdir -p analysis/CNVnator
mkdir -p analysis/Delly
mkdir -p analysis/Hydra
mkdir -p analysis/Lumpy

# BreakDancer
find sve_calls/BreakDancer/ -name "del_BreakDancer_in_truth.txt" -exec cat {} \; > analysis/BreakDancer/total_deletions-BreakDancer_in_truth.txt
find sve_calls/BreakDancer/ -name "del_truth_in_BreakDancer.txt" -exec cat {} \; > analysis/BreakDancer/total_deletions-truth_in_BreakDancer.txt

find sve_calls/BreakDancer/ -name "dup_BreakDancer_in_truth.txt" -exec cat {} \; > analysis/BreakDancer/total_duplications-BreakDancer_in_truth.txt
find sve_calls/BreakDancer/ -name "dup_truth_in_BreakDancer.txt" -exec cat {} \; > analysis/BreakDancer/total_duplications-truth_in_BreakDancer.txt


find sve_calls/BreakDancer/ -name "inv_BreakDancer_in_truth.txt" -exec cat {} \; > analysis/BreakDancer/total_inversions-BreakDancer_in_truth.txt
find sve_calls/BreakDancer/ -name "inv_truth_in_BreakDancer.txt" -exec cat {} \; > analysis/BreakDancer/total_inversions-truth_in_BreakDancer.txt

# cnMOPS
find sve_calls/cnMOPS/ -name "del_cnMOPS_in_truth.txt" -exec cat {} \; > analysis/cnMOPS/total_deletions-cnMOPS_in_truth.txt
find sve_calls/cnMOPS/ -name "del_truth_in_cnMOPS.txt" -exec cat {} \; > analysis/cnMOPS/total_deletions-truth_in_cnMOPS.txt

find sve_calls/cnMOPS/ -name "dup_cnMOPS_in_truth.txt" -exec cat {} \; > analysis/cnMOPS/total_duplications-cnMOPS_in_truth.txt
find sve_calls/cnMOPS/ -name "dup_truth_in_cnMOPS.txt" -exec cat {} \; > analysis/cnMOPS/total_duplications-truth_in_cnMOPS.txt


find sve_calls/cnMOPS/ -name "inv_cnMOPS_in_truth.txt" -exec cat {} \; > analysis/cnMOPS/total_inversions-cnMOPS_in_truth.txt
find sve_calls/cnMOPS/ -name "inv_truth_in_cnMOPS.txt" -exec cat {} \; > analysis/cnMOPS/total_inversions-truth_in_cnMOPS.txt

# CNVnator
find sve_calls/CNVnator/ -name "del_CNVnator_in_truth.txt" -exec cat {} \; > analysis/CNVnator/total_deletions-CNVnator_in_truth.txt
find sve_calls/CNVnator/ -name "del_truth_in_CNVnator.txt" -exec cat {} \; > analysis/CNVnator/total_deletions-truth_in_CNVnator.txt

find sve_calls/CNVnator/ -name "dup_CNVnator_in_truth.txt" -exec cat {} \; > analysis/CNVnator/total_duplications-CNVnator_in_truth.txt
find sve_calls/CNVnator/ -name "dup_truth_in_CNVnator.txt" -exec cat {} \; > analysis/CNVnator/total_duplications-truth_in_CNVnator.txt


find sve_calls/CNVnator/ -name "inv_CNVnator_in_truth.txt" -exec cat {} \; > analysis/CNVnator/total_inversions-CNVnator_in_truth.txt
find sve_calls/CNVnator/ -name "inv_truth_in_CNVnator.txt" -exec cat {} \; > analysis/CNVnator/total_inversions-truth_in_CNVnator.txt

# Delly
find sve_calls/Delly/ -name "del_Delly_in_truth.txt" -exec cat {} \; > analysis/Delly/total_deletions-Delly_in_truth.txt
find sve_calls/Delly/ -name "del_truth_in_Delly.txt" -exec cat {} \; > analysis/Delly/total_deletions-truth_in_Delly.txt

find sve_calls/Delly/ -name "dup_Delly_in_truth.txt" -exec cat {} \; > analysis/Delly/total_duplications-Delly_in_truth.txt
find sve_calls/Delly/ -name "dup_truth_in_Delly.txt" -exec cat {} \; > analysis/Delly/total_duplications-truth_in_Delly.txt


find sve_calls/Delly/ -name "inv_Delly_in_truth.txt" -exec cat {} \; > analysis/Delly/total_inversions-Delly_in_truth.txt
find sve_calls/Delly/ -name "inv_truth_in_Delly.txt" -exec cat {} \; > analysis/Delly/total_inversions-truth_in_Delly.txt

# Hydra
find sve_calls/Hydra/ -name "del_Hydra_in_truth.txt" -exec cat {} \; > analysis/Hydra/total_deletions-Hydra_in_truth.txt
find sve_calls/Hydra/ -name "del_truth_in_Hydra.txt" -exec cat {} \; > analysis/Hydra/total_deletions-truth_in_Hydra.txt

find sve_calls/Hydra/ -name "dup_Hydra_in_truth.txt" -exec cat {} \; > analysis/Hydra/total_duplications-Hydra_in_truth.txt
find sve_calls/Hydra/ -name "dup_truth_in_Hydra.txt" -exec cat {} \; > analysis/Hydra/total_duplications-truth_in_Hydra.txt


find sve_calls/Hydra/ -name "inv_Hydra_in_truth.txt" -exec cat {} \; > analysis/Hydra/total_inversions-Hydra_in_truth.txt
find sve_calls/Hydra/ -name "inv_truth_in_Hydra.txt" -exec cat {} \; > analysis/Hydra/total_inversions-truth_in_Hydra.txt

# Lumpy
find sve_calls/Lumpy/ -name "del_Lumpy_in_truth.txt" -exec cat {} \; > analysis/Lumpy/total_deletions-Lumpy_in_truth.txt
find sve_calls/Lumpy/ -name "del_truth_in_Lumpy.txt" -exec cat {} \; > analysis/Lumpy/total_deletions-truth_in_Lumpy.txt

find sve_calls/Lumpy/ -name "dup_Lumpy_in_truth.txt" -exec cat {} \; > analysis/Lumpy/total_duplications-Lumpy_in_truth.txt
find sve_calls/Lumpy/ -name "dup_truth_in_Lumpy.txt" -exec cat {} \; > analysis/Lumpy/total_duplications-truth_in_Lumpy.txt


find sve_calls/Lumpy/ -name "inv_Lumpy_in_truth.txt" -exec cat {} \; > analysis/Lumpy/total_inversions-Lumpy_in_truth.txt
find sve_calls/Lumpy/ -name "inv_truth_in_Lumpy.txt" -exec cat {} \; > analysis/Lumpy/total_inversions-truth_in_Lumpy.txt
