# BreakDancer
grep -v "SVSIM_DUP" analysis/BreakDancer/total_duplications-BreakDancer_in_truth.txt  > analysis/BreakDancer/duplications/duplications_BreakDancer_false_positives.bed
grep -v "SVSIM_INV" analysis/BreakDancer/total_inversions-BreakDancer_in_truth.txt  > analysis/BreakDancer/inversions/inversions_BreakDancer_false_positives.bed
grep -v "SVSIM_DEL" analysis/BreakDancer/total_deletions-BreakDancer_in_truth.txt  > analysis/BreakDancer/deletions/deletions_BreakDancer_false_positives.bed
# cnMOPS
grep -v "SVSIM_DUP" analysis/cnMOPS/total_duplications-cnMOPS_in_truth.txt  > analysis/cnMOPS/duplications/duplications_cnMOPS_false_positives.bed
grep -v "SVSIM_INV" analysis/cnMOPS/total_inversions-cnMOPS_in_truth.txt  > analysis/cnMOPS/inversions/inversions_cnMOPS_false_positives.bed
grep -v "SVSIM_DEL" analysis/cnMOPS/total_deletions-cnMOPS_in_truth.txt  > analysis/cnMOPS/deletions/deletions_cnMOPS_false_positives.bed
# CNVnator
grep -v "SVSIM_DUP" analysis/CNVnator/total_duplications-CNVnator_in_truth.txt  > analysis/CNVnator/duplications/duplications_CNVnator_false_positives.bed
grep -v "SVSIM_INV" analysis/CNVnator/total_inversions-CNVnator_in_truth.txt  > analysis/CNVnator/inversions/inversions_CNVnator_false_positives.bed
grep -v "SVSIM_DEL" analysis/CNVnator/total_deletions-CNVnator_in_truth.txt  > analysis/CNVnator/deletions/deletions_CNVnator_false_positives.bed
# Delly
grep -v "SVSIM_DUP" analysis/Delly/total_duplications-Delly_in_truth.txt  > analysis/Delly/duplications/duplications_Delly_false_positives.bed
grep -v "SVSIM_INV" analysis/Delly/total_inversions-Delly_in_truth.txt  > analysis/Delly/inversions/inversions_Delly_false_positives.bed
grep -v "SVSIM_DEL" analysis/Delly/total_deletions-Delly_in_truth.txt  > analysis/Delly/deletions/deletions_Delly_false_positives.bed
# Hydra
grep -v "SVSIM_DUP" analysis/Hydra/total_duplications-Hydra_in_truth.txt  > analysis/Hydra/duplications/duplications_Hydra_false_positives.bed
grep -v "SVSIM_INV" analysis/Hydra/total_inversions-Hydra_in_truth.txt  > analysis/Hydra/inversions/inversions_Hydra_false_positives.bed
grep -v "SVSIM_DEL" analysis/Hydra/total_deletions-Hydra_in_truth.txt  > analysis/Hydra/deletions/deletions_Hydra_false_positives.bed
# Lumpy
grep -v "SVSIM_DUP" analysis/Lumpy/total_duplications-Lumpy_in_truth.txt  > analysis/Lumpy/duplications/duplications_Lumpy_false_positives.bed
grep -v "SVSIM_INV" analysis/Lumpy/total_inversions-Lumpy_in_truth.txt  > analysis/Lumpy/inversions/inversions_Lumpy_false_positives.bed
grep -v "SVSIM_DEL" analysis/Lumpy/total_deletions-Lumpy_in_truth.txt  > analysis/Lumpy/deletions/deletions_Lumpy_false_positives.bed

# Delly
python3 get_bed_bins.py analysis/Delly/deletions/deletions_Delly_false_positives.bed Delly DEL
python3 get_bed_bins.py analysis/Delly/duplications/duplications_Delly_false_positives.bed Delly DUP
python3 get_bed_bins.py analysis/Delly/inversions/inversions_Delly_false_positives.bed Delly INV
# CNVnator
python3 get_bed_bins.py ./analysis/CNVnator/deletions/deletions_CNVnator_false_positives.bed CNVnator DEL
python3 get_bed_bins.py ./analysis/CNVnator/duplications/duplications_CNVnator_false_positives.bed CNVnator DUP
python3 get_bed_bins.py ./analysis/CNVnator/inversions/inversions_CNVnator_false_positives.bed CNVnator INV
# Hydra
python3 get_bed_bins.py ./analysis/Hydra/deletions/deletions_Hydra_false_positives.bed Hydra DEL
python3 get_bed_bins.py ./analysis/Hydra/duplications/duplications_Hydra_false_positives.bed Hydra DUP
python3 get_bed_bins.py ./analysis/Hydra/inversions/inversions_Hydra_false_positives.bed Hydra INV
# BreakDancer
python3 get_bed_bins.py ./analysis/BreakDancer/deletions/deletions_BreakDancer_false_positives.bed BreakDancer DEL
python3 get_bed_bins.py ./analysis/BreakDancer/duplications/duplications_BreakDancer_false_positives.bed BreakDancer DUP
python3 get_bed_bins.py ./analysis/BreakDancer/inversions/inversions_BreakDancer_false_positives.bed BreakDancer INV
# Lumpy
python3 get_bed_bins.py ./analysis/Lumpy/deletions/deletions_Lumpy_false_positives.bed Lumpy DEL
python3 get_bed_bins.py ./analysis/Lumpy/duplications/duplications_Lumpy_false_positives.bed Lumpy DUP
python3 get_bed_bins.py ./analysis/Lumpy/inversions/inversions_Lumpy_false_positives.bed Lumpy INV
# cnMOPS
python3 get_bed_bins.py ./analysis/cnMOPS/deletions/deletions_cnMOPS_false_positives.bed cnMOPS DEL
python3 get_bed_bins.py ./analysis/cnMOPS/duplications/duplications_cnMOPS_false_positives.bed cnMOPS DUP
python3 get_bed_bins.py ./analysis/cnMOPS/inversions/inversions_cnMOPS_false_positives.bed cnMOPS INV
