mkdir -p analysis/BreakDancer/deletions
mkdir -p analysis/BreakDancer/duplications
mkdir -p analysis/BreakDancer/inversions

mkdir -p analysis/cnMOPS/deletions
mkdir -p analysis/cnMOPS/duplications
mkdir -p analysis/cnMOPS/inversions

mkdir -p analysis/CNVnator/deletions
mkdir -p analysis/CNVnator/duplications
mkdir -p analysis/CNVnator/inversions

mkdir -p analysis/Delly/deletions
mkdir -p analysis/Delly/duplications
mkdir -p analysis/Delly/inversions

mkdir -p analysis/Hydra/deletions
mkdir -p analysis/Hydra/duplications
mkdir -p analysis/Hydra/inversions

mkdir -p analysis/Lumpy/deletions
mkdir -p analysis/Lumpy/duplications
mkdir -p analysis/Lumpy/inversions

# BreakDancer

grep "SVSIM_DUP.*100-1Kbp" analysis/BreakDancer/total_duplications-BreakDancer_in_truth.txt  > analysis/BreakDancer/duplications/duplications_BreakDancer_true_positives_100-1Kbp.txt
grep "SVSIM_DUP.*1K-10Kbp" analysis/BreakDancer/total_duplications-BreakDancer_in_truth.txt  > analysis/BreakDancer/duplications/duplications_BreakDancer_true_positives_1K-10Kbp.txt
grep "SVSIM_DUP.*10K-50Kbp" analysis/BreakDancer/total_duplications-BreakDancer_in_truth.txt  > analysis/BreakDancer/duplications/duplications_BreakDancer_true_positives_10K-50Kbp.txt
grep "SVSIM_DUP.*50K-100Kbp" analysis/BreakDancer/total_duplications-BreakDancer_in_truth.txt  > analysis/BreakDancer/duplications/duplications_BreakDancer_true_positives_50K-100Kbp.txt
grep "SVSIM_DUP.*100K-250Kbp" analysis/BreakDancer/total_duplications-BreakDancer_in_truth.txt  > analysis/BreakDancer/duplications/duplications_BreakDancer_true_positives_100K-250Kbp.txt
grep "SVSIM_DUP.*250K-500Kbp" analysis/BreakDancer/total_duplications-BreakDancer_in_truth.txt  > analysis/BreakDancer/duplications/duplications_BreakDancer_true_positives_250K-500Kbp.txt
grep "SVSIM_DUP.*500K-1Mbp" analysis/BreakDancer/total_duplications-BreakDancer_in_truth.txt  > analysis/BreakDancer/duplications/duplications_BreakDancer_true_positives_500K-1Mbp.txt

grep "SVSIM_INV.*100-2500bp" analysis/BreakDancer/total_inversions-BreakDancer_in_truth.txt  > analysis/BreakDancer/inversions/inversions_BreakDancer_true_positives_100-2500bp.txt
grep "SVSIM_INV.*2500-3500bp" analysis/BreakDancer/total_inversions-BreakDancer_in_truth.txt  > analysis/BreakDancer/inversions/inversions_BreakDancer_true_positives_2500-3500bp.txt
grep "SVSIM_INV.*3500-45Kbp" analysis/BreakDancer/total_inversions-BreakDancer_in_truth.txt  > analysis/BreakDancer/inversions/inversions_BreakDancer_true_positives_3500-45Kbp.txt
grep "SVSIM_INV.*45K-80Kbp" analysis/BreakDancer/total_inversions-BreakDancer_in_truth.txt  > analysis/BreakDancer/inversions/inversions_BreakDancer_true_positives_45K-80Kbp.txt
grep "SVSIM_INV.*80K-115Kbp" analysis/BreakDancer/total_inversions-BreakDancer_in_truth.txt  > analysis/BreakDancer/inversions/inversions_BreakDancer_true_positives_80K-115Kbp.txt
grep "SVSIM_INV.*115K-180Kbp" analysis/BreakDancer/total_inversions-BreakDancer_in_truth.txt  > analysis/BreakDancer/inversions/inversions_BreakDancer_true_positives_115K-180Kbp.txt
grep "SVSIM_INV.*180K-260Kbp" analysis/BreakDancer/total_inversions-BreakDancer_in_truth.txt  > analysis/BreakDancer/inversions/inversions_BreakDancer_true_positives_180K-260Kbp.txt
grep "SVSIM_INV.*260K-300Kbp" analysis/BreakDancer/total_inversions-BreakDancer_in_truth.txt  > analysis/BreakDancer/inversions/inversions_BreakDancer_true_positives_260K-300Kbp.txt
grep "SVSIM_INV.*300K-375Kbp" analysis/BreakDancer/total_inversions-BreakDancer_in_truth.txt  > analysis/BreakDancer/inversions/inversions_BreakDancer_true_positives_300K-375Kbp.txt
grep "SVSIM_INV.*375K-500Kbp" analysis/BreakDancer/total_inversions-BreakDancer_in_truth.txt  > analysis/BreakDancer/inversions/inversions_BreakDancer_true_positives_375K-500Kbp.txt
grep "SVSIM_INV.*500K-1Mbp" analysis/BreakDancer/total_inversions-BreakDancer_in_truth.txt  > analysis/BreakDancer/inversions/inversions_BreakDancer_true_positives_500K-1Mbp.txt

grep "SVSIM_DEL.*100-400bp" analysis/BreakDancer/total_deletions-BreakDancer_in_truth.txt  > analysis/BreakDancer/deletions/deletions_BreakDancer_true_positives_100-400bp.txt
grep "SVSIM_DEL.*400-600bp" analysis/BreakDancer/total_deletions-BreakDancer_in_truth.txt  > analysis/BreakDancer/deletions/deletions_BreakDancer_true_positives_400-600bp.txt
grep "SVSIM_DEL.*600-950bp" analysis/BreakDancer/total_deletions-BreakDancer_in_truth.txt  > analysis/BreakDancer/deletions/deletions_BreakDancer_true_positives_600-950bp.txt
grep "SVSIM_DEL.*950-1.2Kbp" analysis/BreakDancer/total_deletions-BreakDancer_in_truth.txt  > analysis/BreakDancer/deletions/deletions_BreakDancer_true_positives_950-1.2Kbp.txt
grep "SVSIM_DEL.*1.2K-1.5Kbp" analysis/BreakDancer/total_deletions-BreakDancer_in_truth.txt  > analysis/BreakDancer/deletions/deletions_BreakDancer_true_positives_1.2K-1.5Kbp.txt
grep "SVSIM_DEL.*1.5K-1.9Kbp" analysis/BreakDancer/total_deletions-BreakDancer_in_truth.txt  > analysis/BreakDancer/deletions/deletions_BreakDancer_true_positives_1.5K-1.9Kbp.txt
grep "SVSIM_DEL.*1.9K-2.2Kbp" analysis/BreakDancer/total_deletions-BreakDancer_in_truth.txt  > analysis/BreakDancer/deletions/deletions_BreakDancer_true_positives_1.9K-2.2Kbp.txt
grep "SVSIM_DEL.*2.2K-2.9Kbp" analysis/BreakDancer/total_deletions-BreakDancer_in_truth.txt  > analysis/BreakDancer/deletions/deletions_BreakDancer_true_positives_2.2K-2.9Kbp.txt
grep "SVSIM_DEL.*2.9K-3.6Kbp" analysis/BreakDancer/total_deletions-BreakDancer_in_truth.txt  > analysis/BreakDancer/deletions/deletions_BreakDancer_true_positives_2.9K-3.6Kbp.txt
grep "SVSIM_DEL.*3.6K-4.8Kbp" analysis/BreakDancer/total_deletions-BreakDancer_in_truth.txt  > analysis/BreakDancer/deletions/deletions_BreakDancer_true_positives_3.6K-4.8Kbp.txt
grep "SVSIM_DEL.*4.8K-6.1Kbp" analysis/BreakDancer/total_deletions-BreakDancer_in_truth.txt  > analysis/BreakDancer/deletions/deletions_BreakDancer_true_positives_4.8K-6.1Kbp.txt
grep "SVSIM_DEL.*6.1K-9Kbp" analysis/BreakDancer/total_deletions-BreakDancer_in_truth.txt  > analysis/BreakDancer/deletions/deletions_BreakDancer_true_positives_6.1K-9Kbp.txt
grep "SVSIM_DEL.*9K-18.5Kbp" analysis/BreakDancer/total_deletions-BreakDancer_in_truth.txt  > analysis/BreakDancer/deletions/deletions_BreakDancer_true_positives_9K-18.5Kbp.txt
grep "SVSIM_DEL.*18.5K-100Kbp" analysis/BreakDancer/total_deletions-BreakDancer_in_truth.txt  > analysis/BreakDancer/deletions/deletions_BreakDancer_true_positives_18.5K-100Kbp.txt
grep "SVSIM_DEL.*100K-1Mbp" analysis/BreakDancer/total_deletions-BreakDancer_in_truth.txt  > analysis/BreakDancer/deletions/deletions_BreakDancer_true_positives_100K-1Mbp.txt

# cnMOPS
grep "SVSIM_DUP.*100-1Kbp" analysis/cnMOPS/total_duplications-cnMOPS_in_truth.txt  > analysis/cnMOPS/duplications/duplications_cnMOPS_true_positives_100-1Kbp.txt
grep "SVSIM_DUP.*1K-10Kbp" analysis/cnMOPS/total_duplications-cnMOPS_in_truth.txt  > analysis/cnMOPS/duplications/duplications_cnMOPS_true_positives_1K-10Kbp.txt
grep "SVSIM_DUP.*10K-50Kbp" analysis/cnMOPS/total_duplications-cnMOPS_in_truth.txt  > analysis/cnMOPS/duplications/duplications_cnMOPS_true_positives_10K-50Kbp.txt
grep "SVSIM_DUP.*50K-100Kbp" analysis/cnMOPS/total_duplications-cnMOPS_in_truth.txt  > analysis/cnMOPS/duplications/duplications_cnMOPS_true_positives_50K-100Kbp.txt
grep "SVSIM_DUP.*100K-250Kbp" analysis/cnMOPS/total_duplications-cnMOPS_in_truth.txt  > analysis/cnMOPS/duplications/duplications_cnMOPS_true_positives_100K-250Kbp.txt
grep "SVSIM_DUP.*250K-500Kbp" analysis/cnMOPS/total_duplications-cnMOPS_in_truth.txt  > analysis/cnMOPS/duplications/duplications_cnMOPS_true_positives_250K-500Kbp.txt
grep "SVSIM_DUP.*500K-1Mbp" analysis/cnMOPS/total_duplications-cnMOPS_in_truth.txt  > analysis/cnMOPS/duplications/duplications_cnMOPS_true_positives_500K-1Mbp.txt

grep "SVSIM_INV.*100-2500bp" analysis/cnMOPS/total_inversions-cnMOPS_in_truth.txt  > analysis/cnMOPS/inversions/inversions_cnMOPS_true_positives_100-2500bp.txt
grep "SVSIM_INV.*2500-3500bp" analysis/cnMOPS/total_inversions-cnMOPS_in_truth.txt  > analysis/cnMOPS/inversions/inversions_cnMOPS_true_positives_2500-3500bp.txt
grep "SVSIM_INV.*3500-45Kbp" analysis/cnMOPS/total_inversions-cnMOPS_in_truth.txt  > analysis/cnMOPS/inversions/inversions_cnMOPS_true_positives_3500-45Kbp.txt
grep "SVSIM_INV.*45K-80Kbp" analysis/cnMOPS/total_inversions-cnMOPS_in_truth.txt  > analysis/cnMOPS/inversions/inversions_cnMOPS_true_positives_45K-80Kbp.txt
grep "SVSIM_INV.*80K-115Kbp" analysis/cnMOPS/total_inversions-cnMOPS_in_truth.txt  > analysis/cnMOPS/inversions/inversions_cnMOPS_true_positives_80K-115Kbp.txt
grep "SVSIM_INV.*115K-180Kbp" analysis/cnMOPS/total_inversions-cnMOPS_in_truth.txt  > analysis/cnMOPS/inversions/inversions_cnMOPS_true_positives_115K-180Kbp.txt
grep "SVSIM_INV.*180K-260Kbp" analysis/cnMOPS/total_inversions-cnMOPS_in_truth.txt  > analysis/cnMOPS/inversions/inversions_cnMOPS_true_positives_180K-260Kbp.txt
grep "SVSIM_INV.*260K-300Kbp" analysis/cnMOPS/total_inversions-cnMOPS_in_truth.txt  > analysis/cnMOPS/inversions/inversions_cnMOPS_true_positives_260K-300Kbp.txt
grep "SVSIM_INV.*300K-375Kbp" analysis/cnMOPS/total_inversions-cnMOPS_in_truth.txt  > analysis/cnMOPS/inversions/inversions_cnMOPS_true_positives_300K-375Kbp.txt
grep "SVSIM_INV.*375K-500Kbp" analysis/cnMOPS/total_inversions-cnMOPS_in_truth.txt  > analysis/cnMOPS/inversions/inversions_cnMOPS_true_positives_375K-500Kbp.txt
grep "SVSIM_INV.*500K-1Mbp" analysis/cnMOPS/total_inversions-cnMOPS_in_truth.txt  > analysis/cnMOPS/inversions/inversions_cnMOPS_true_positives_500K-1Mbp.txt

grep "SVSIM_DEL.*100-400bp" analysis/cnMOPS/total_deletions-cnMOPS_in_truth.txt  > analysis/cnMOPS/deletions/deletions_cnMOPS_true_positives_100-400bp.txt
grep "SVSIM_DEL.*400-600bp" analysis/cnMOPS/total_deletions-cnMOPS_in_truth.txt  > analysis/cnMOPS/deletions/deletions_cnMOPS_true_positives_400-600bp.txt
grep "SVSIM_DEL.*600-950bp" analysis/cnMOPS/total_deletions-cnMOPS_in_truth.txt  > analysis/cnMOPS/deletions/deletions_cnMOPS_true_positives_600-950bp.txt
grep "SVSIM_DEL.*950-1.2Kbp" analysis/cnMOPS/total_deletions-cnMOPS_in_truth.txt  > analysis/cnMOPS/deletions/deletions_cnMOPS_true_positives_950-1.2Kbp.txt
grep "SVSIM_DEL.*1.2K-1.5Kbp" analysis/cnMOPS/total_deletions-cnMOPS_in_truth.txt  > analysis/cnMOPS/deletions/deletions_cnMOPS_true_positives_1.2K-1.5Kbp.txt
grep "SVSIM_DEL.*1.5K-1.9Kbp" analysis/cnMOPS/total_deletions-cnMOPS_in_truth.txt  > analysis/cnMOPS/deletions/deletions_cnMOPS_true_positives_1.5K-1.9Kbp.txt
grep "SVSIM_DEL.*1.9K-2.2Kbp" analysis/cnMOPS/total_deletions-cnMOPS_in_truth.txt  > analysis/cnMOPS/deletions/deletions_cnMOPS_true_positives_1.9K-2.2Kbp.txt
grep "SVSIM_DEL.*2.2K-2.9Kbp" analysis/cnMOPS/total_deletions-cnMOPS_in_truth.txt  > analysis/cnMOPS/deletions/deletions_cnMOPS_true_positives_2.2K-2.9Kbp.txt
grep "SVSIM_DEL.*2.9K-3.6Kbp" analysis/cnMOPS/total_deletions-cnMOPS_in_truth.txt  > analysis/cnMOPS/deletions/deletions_cnMOPS_true_positives_2.9K-3.6Kbp.txt
grep "SVSIM_DEL.*3.6K-4.8Kbp" analysis/cnMOPS/total_deletions-cnMOPS_in_truth.txt  > analysis/cnMOPS/deletions/deletions_cnMOPS_true_positives_3.6K-4.8Kbp.txt
grep "SVSIM_DEL.*4.8K-6.1Kbp" analysis/cnMOPS/total_deletions-cnMOPS_in_truth.txt  > analysis/cnMOPS/deletions/deletions_cnMOPS_true_positives_4.8K-6.1Kbp.txt
grep "SVSIM_DEL.*6.1K-9Kbp" analysis/cnMOPS/total_deletions-cnMOPS_in_truth.txt  > analysis/cnMOPS/deletions/deletions_cnMOPS_true_positives_6.1K-9Kbp.txt
grep "SVSIM_DEL.*9K-18.5Kbp" analysis/cnMOPS/total_deletions-cnMOPS_in_truth.txt  > analysis/cnMOPS/deletions/deletions_cnMOPS_true_positives_9K-18.5Kbp.txt
grep "SVSIM_DEL.*18.5K-100Kbp" analysis/cnMOPS/total_deletions-cnMOPS_in_truth.txt  > analysis/cnMOPS/deletions/deletions_cnMOPS_true_positives_18.5K-100Kbp.txt
grep "SVSIM_DEL.*100K-1Mbp" analysis/cnMOPS/total_deletions-cnMOPS_in_truth.txt  > analysis/cnMOPS/deletions/deletions_cnMOPS_true_positives_100K-1Mbp.txt

# CNVnator
grep "SVSIM_DUP.*100-1Kbp" analysis/CNVnator/total_duplications-CNVnator_in_truth.txt  > analysis/CNVnator/duplications/duplications_CNVnator_true_positives_100-1Kbp.txt
grep "SVSIM_DUP.*1K-10Kbp" analysis/CNVnator/total_duplications-CNVnator_in_truth.txt  > analysis/CNVnator/duplications/duplications_CNVnator_true_positives_1K-10Kbp.txt
grep "SVSIM_DUP.*10K-50Kbp" analysis/CNVnator/total_duplications-CNVnator_in_truth.txt  > analysis/CNVnator/duplications/duplications_CNVnator_true_positives_10K-50Kbp.txt
grep "SVSIM_DUP.*50K-100Kbp" analysis/CNVnator/total_duplications-CNVnator_in_truth.txt  > analysis/CNVnator/duplications/duplications_CNVnator_true_positives_50K-100Kbp.txt
grep "SVSIM_DUP.*100K-250Kbp" analysis/CNVnator/total_duplications-CNVnator_in_truth.txt  > analysis/CNVnator/duplications/duplications_CNVnator_true_positives_100K-250Kbp.txt
grep "SVSIM_DUP.*250K-500Kbp" analysis/CNVnator/total_duplications-CNVnator_in_truth.txt  > analysis/CNVnator/duplications/duplications_CNVnator_true_positives_250K-500Kbp.txt
grep "SVSIM_DUP.*500K-1Mbp" analysis/CNVnator/total_duplications-CNVnator_in_truth.txt  > analysis/CNVnator/duplications/duplications_CNVnator_true_positives_500K-1Mbp.txt

grep "SVSIM_INV.*100-2500bp" analysis/CNVnator/total_inversions-CNVnator_in_truth.txt  > analysis/CNVnator/inversions/inversions_CNVnator_true_positives_100-2500bp.txt
grep "SVSIM_INV.*2500-3500bp" analysis/CNVnator/total_inversions-CNVnator_in_truth.txt  > analysis/CNVnator/inversions/inversions_CNVnator_true_positives_2500-3500bp.txt
grep "SVSIM_INV.*3500-45Kbp" analysis/CNVnator/total_inversions-CNVnator_in_truth.txt  > analysis/CNVnator/inversions/inversions_CNVnator_true_positives_3500-45Kbp.txt
grep "SVSIM_INV.*45K-80Kbp" analysis/CNVnator/total_inversions-CNVnator_in_truth.txt  > analysis/CNVnator/inversions/inversions_CNVnator_true_positives_45K-80Kbp.txt
grep "SVSIM_INV.*80K-115Kbp" analysis/CNVnator/total_inversions-CNVnator_in_truth.txt  > analysis/CNVnator/inversions/inversions_CNVnator_true_positives_80K-115Kbp.txt
grep "SVSIM_INV.*115K-180Kbp" analysis/CNVnator/total_inversions-CNVnator_in_truth.txt  > analysis/CNVnator/inversions/inversions_CNVnator_true_positives_115K-180Kbp.txt
grep "SVSIM_INV.*180K-260Kbp" analysis/CNVnator/total_inversions-CNVnator_in_truth.txt  > analysis/CNVnator/inversions/inversions_CNVnator_true_positives_180K-260Kbp.txt
grep "SVSIM_INV.*260K-300Kbp" analysis/CNVnator/total_inversions-CNVnator_in_truth.txt  > analysis/CNVnator/inversions/inversions_CNVnator_true_positives_260K-300Kbp.txt
grep "SVSIM_INV.*300K-375Kbp" analysis/CNVnator/total_inversions-CNVnator_in_truth.txt  > analysis/CNVnator/inversions/inversions_CNVnator_true_positives_300K-375Kbp.txt
grep "SVSIM_INV.*375K-500Kbp" analysis/CNVnator/total_inversions-CNVnator_in_truth.txt  > analysis/CNVnator/inversions/inversions_CNVnator_true_positives_375K-500Kbp.txt
grep "SVSIM_INV.*500K-1Mbp" analysis/CNVnator/total_inversions-CNVnator_in_truth.txt  > analysis/CNVnator/inversions/inversions_CNVnator_true_positives_500K-1Mbp.txt

grep "SVSIM_DEL.*100-400bp" analysis/CNVnator/total_deletions-CNVnator_in_truth.txt  > analysis/CNVnator/deletions/deletions_CNVnator_true_positives_100-400bp.txt
grep "SVSIM_DEL.*400-600bp" analysis/CNVnator/total_deletions-CNVnator_in_truth.txt  > analysis/CNVnator/deletions/deletions_CNVnator_true_positives_400-600bp.txt
grep "SVSIM_DEL.*600-950bp" analysis/CNVnator/total_deletions-CNVnator_in_truth.txt  > analysis/CNVnator/deletions/deletions_CNVnator_true_positives_600-950bp.txt
grep "SVSIM_DEL.*950-1.2Kbp" analysis/CNVnator/total_deletions-CNVnator_in_truth.txt  > analysis/CNVnator/deletions/deletions_CNVnator_true_positives_950-1.2Kbp.txt
grep "SVSIM_DEL.*1.2K-1.5Kbp" analysis/CNVnator/total_deletions-CNVnator_in_truth.txt  > analysis/CNVnator/deletions/deletions_CNVnator_true_positives_1.2K-1.5Kbp.txt
grep "SVSIM_DEL.*1.5K-1.9Kbp" analysis/CNVnator/total_deletions-CNVnator_in_truth.txt  > analysis/CNVnator/deletions/deletions_CNVnator_true_positives_1.5K-1.9Kbp.txt
grep "SVSIM_DEL.*1.9K-2.2Kbp" analysis/CNVnator/total_deletions-CNVnator_in_truth.txt  > analysis/CNVnator/deletions/deletions_CNVnator_true_positives_1.9K-2.2Kbp.txt
grep "SVSIM_DEL.*2.2K-2.9Kbp" analysis/CNVnator/total_deletions-CNVnator_in_truth.txt  > analysis/CNVnator/deletions/deletions_CNVnator_true_positives_2.2K-2.9Kbp.txt
grep "SVSIM_DEL.*2.9K-3.6Kbp" analysis/CNVnator/total_deletions-CNVnator_in_truth.txt  > analysis/CNVnator/deletions/deletions_CNVnator_true_positives_2.9K-3.6Kbp.txt
grep "SVSIM_DEL.*3.6K-4.8Kbp" analysis/CNVnator/total_deletions-CNVnator_in_truth.txt  > analysis/CNVnator/deletions/deletions_CNVnator_true_positives_3.6K-4.8Kbp.txt
grep "SVSIM_DEL.*4.8K-6.1Kbp" analysis/CNVnator/total_deletions-CNVnator_in_truth.txt  > analysis/CNVnator/deletions/deletions_CNVnator_true_positives_4.8K-6.1Kbp.txt
grep "SVSIM_DEL.*6.1K-9Kbp" analysis/CNVnator/total_deletions-CNVnator_in_truth.txt  > analysis/CNVnator/deletions/deletions_CNVnator_true_positives_6.1K-9Kbp.txt
grep "SVSIM_DEL.*9K-18.5Kbp" analysis/CNVnator/total_deletions-CNVnator_in_truth.txt  > analysis/CNVnator/deletions/deletions_CNVnator_true_positives_9K-18.5Kbp.txt
grep "SVSIM_DEL.*18.5K-100Kbp" analysis/CNVnator/total_deletions-CNVnator_in_truth.txt  > analysis/CNVnator/deletions/deletions_CNVnator_true_positives_18.5K-100Kbp.txt
grep "SVSIM_DEL.*100K-1Mbp" analysis/CNVnator/total_deletions-CNVnator_in_truth.txt  > analysis/CNVnator/deletions/deletions_CNVnator_true_positives_100K-1Mbp.txt

# Delly
grep "SVSIM_DUP.*100-1Kbp" analysis/Delly/total_duplications-Delly_in_truth.txt  > analysis/Delly/duplications/duplications_Delly_true_positives_100-1Kbp.txt
grep "SVSIM_DUP.*1K-10Kbp" analysis/Delly/total_duplications-Delly_in_truth.txt  > analysis/Delly/duplications/duplications_Delly_true_positives_1K-10Kbp.txt
grep "SVSIM_DUP.*10K-50Kbp" analysis/Delly/total_duplications-Delly_in_truth.txt  > analysis/Delly/duplications/duplications_Delly_true_positives_10K-50Kbp.txt
grep "SVSIM_DUP.*50K-100Kbp" analysis/Delly/total_duplications-Delly_in_truth.txt  > analysis/Delly/duplications/duplications_Delly_true_positives_50K-100Kbp.txt
grep "SVSIM_DUP.*100K-250Kbp" analysis/Delly/total_duplications-Delly_in_truth.txt  > analysis/Delly/duplications/duplications_Delly_true_positives_100K-250Kbp.txt
grep "SVSIM_DUP.*250K-500Kbp" analysis/Delly/total_duplications-Delly_in_truth.txt  > analysis/Delly/duplications/duplications_Delly_true_positives_250K-500Kbp.txt
grep "SVSIM_DUP.*500K-1Mbp" analysis/Delly/total_duplications-Delly_in_truth.txt  > analysis/Delly/duplications/duplications_Delly_true_positives_500K-1Mbp.txt

grep "SVSIM_INV.*100-2500bp" analysis/Delly/total_inversions-Delly_in_truth.txt  > analysis/Delly/inversions/inversions_Delly_true_positives_100-2500bp.txt
grep "SVSIM_INV.*2500-3500bp" analysis/Delly/total_inversions-Delly_in_truth.txt  > analysis/Delly/inversions/inversions_Delly_true_positives_2500-3500bp.txt
grep "SVSIM_INV.*3500-45Kbp" analysis/Delly/total_inversions-Delly_in_truth.txt  > analysis/Delly/inversions/inversions_Delly_true_positives_3500-45Kbp.txt
grep "SVSIM_INV.*45K-80Kbp" analysis/Delly/total_inversions-Delly_in_truth.txt  > analysis/Delly/inversions/inversions_Delly_true_positives_45K-80Kbp.txt
grep "SVSIM_INV.*80K-115Kbp" analysis/Delly/total_inversions-Delly_in_truth.txt  > analysis/Delly/inversions/inversions_Delly_true_positives_80K-115Kbp.txt
grep "SVSIM_INV.*115K-180Kbp" analysis/Delly/total_inversions-Delly_in_truth.txt  > analysis/Delly/inversions/inversions_Delly_true_positives_115K-180Kbp.txt
grep "SVSIM_INV.*180K-260Kbp" analysis/Delly/total_inversions-Delly_in_truth.txt  > analysis/Delly/inversions/inversions_Delly_true_positives_180K-260Kbp.txt
grep "SVSIM_INV.*260K-300Kbp" analysis/Delly/total_inversions-Delly_in_truth.txt  > analysis/Delly/inversions/inversions_Delly_true_positives_260K-300Kbp.txt
grep "SVSIM_INV.*300K-375Kbp" analysis/Delly/total_inversions-Delly_in_truth.txt  > analysis/Delly/inversions/inversions_Delly_true_positives_300K-375Kbp.txt
grep "SVSIM_INV.*375K-500Kbp" analysis/Delly/total_inversions-Delly_in_truth.txt  > analysis/Delly/inversions/inversions_Delly_true_positives_375K-500Kbp.txt
grep "SVSIM_INV.*500K-1Mbp" analysis/Delly/total_inversions-Delly_in_truth.txt  > analysis/Delly/inversions/inversions_Delly_true_positives_500K-1Mbp.txt

grep "SVSIM_DEL.*100-400bp" analysis/Delly/total_deletions-Delly_in_truth.txt  > analysis/Delly/deletions/deletions_Delly_true_positives_100-400bp.txt
grep "SVSIM_DEL.*400-600bp" analysis/Delly/total_deletions-Delly_in_truth.txt  > analysis/Delly/deletions/deletions_Delly_true_positives_400-600bp.txt
grep "SVSIM_DEL.*600-950bp" analysis/Delly/total_deletions-Delly_in_truth.txt  > analysis/Delly/deletions/deletions_Delly_true_positives_600-950bp.txt
grep "SVSIM_DEL.*950-1.2Kbp" analysis/Delly/total_deletions-Delly_in_truth.txt  > analysis/Delly/deletions/deletions_Delly_true_positives_950-1.2Kbp.txt
grep "SVSIM_DEL.*1.2K-1.5Kbp" analysis/Delly/total_deletions-Delly_in_truth.txt  > analysis/Delly/deletions/deletions_Delly_true_positives_1.2K-1.5Kbp.txt
grep "SVSIM_DEL.*1.5K-1.9Kbp" analysis/Delly/total_deletions-Delly_in_truth.txt  > analysis/Delly/deletions/deletions_Delly_true_positives_1.5K-1.9Kbp.txt
grep "SVSIM_DEL.*1.9K-2.2Kbp" analysis/Delly/total_deletions-Delly_in_truth.txt  > analysis/Delly/deletions/deletions_Delly_true_positives_1.9K-2.2Kbp.txt
grep "SVSIM_DEL.*2.2K-2.9Kbp" analysis/Delly/total_deletions-Delly_in_truth.txt  > analysis/Delly/deletions/deletions_Delly_true_positives_2.2K-2.9Kbp.txt
grep "SVSIM_DEL.*2.9K-3.6Kbp" analysis/Delly/total_deletions-Delly_in_truth.txt  > analysis/Delly/deletions/deletions_Delly_true_positives_2.9K-3.6Kbp.txt
grep "SVSIM_DEL.*3.6K-4.8Kbp" analysis/Delly/total_deletions-Delly_in_truth.txt  > analysis/Delly/deletions/deletions_Delly_true_positives_3.6K-4.8Kbp.txt
grep "SVSIM_DEL.*4.8K-6.1Kbp" analysis/Delly/total_deletions-Delly_in_truth.txt  > analysis/Delly/deletions/deletions_Delly_true_positives_4.8K-6.1Kbp.txt
grep "SVSIM_DEL.*6.1K-9Kbp" analysis/Delly/total_deletions-Delly_in_truth.txt  > analysis/Delly/deletions/deletions_Delly_true_positives_6.1K-9Kbp.txt
grep "SVSIM_DEL.*9K-18.5Kbp" analysis/Delly/total_deletions-Delly_in_truth.txt  > analysis/Delly/deletions/deletions_Delly_true_positives_9K-18.5Kbp.txt
grep "SVSIM_DEL.*18.5K-100Kbp" analysis/Delly/total_deletions-Delly_in_truth.txt  > analysis/Delly/deletions/deletions_Delly_true_positives_18.5K-100Kbp.txt
grep "SVSIM_DEL.*100K-1Mbp" analysis/Delly/total_deletions-Delly_in_truth.txt  > analysis/Delly/deletions/deletions_Delly_true_positives_100K-1Mbp.txt

# Hydra
grep "SVSIM_DUP.*100-1Kbp" analysis/Hydra/total_duplications-Hydra_in_truth.txt  > analysis/Hydra/duplications/duplications_Hydra_true_positives_100-1Kbp.txt
grep "SVSIM_DUP.*1K-10Kbp" analysis/Hydra/total_duplications-Hydra_in_truth.txt  > analysis/Hydra/duplications/duplications_Hydra_true_positives_1K-10Kbp.txt
grep "SVSIM_DUP.*10K-50Kbp" analysis/Hydra/total_duplications-Hydra_in_truth.txt  > analysis/Hydra/duplications/duplications_Hydra_true_positives_10K-50Kbp.txt
grep "SVSIM_DUP.*50K-100Kbp" analysis/Hydra/total_duplications-Hydra_in_truth.txt  > analysis/Hydra/duplications/duplications_Hydra_true_positives_50K-100Kbp.txt
grep "SVSIM_DUP.*100K-250Kbp" analysis/Hydra/total_duplications-Hydra_in_truth.txt  > analysis/Hydra/duplications/duplications_Hydra_true_positives_100K-250Kbp.txt
grep "SVSIM_DUP.*250K-500Kbp" analysis/Hydra/total_duplications-Hydra_in_truth.txt  > analysis/Hydra/duplications/duplications_Hydra_true_positives_250K-500Kbp.txt
grep "SVSIM_DUP.*500K-1Mbp" analysis/Hydra/total_duplications-Hydra_in_truth.txt  > analysis/Hydra/duplications/duplications_Hydra_true_positives_500K-1Mbp.txt

grep "SVSIM_INV.*100-2500bp" analysis/Hydra/total_inversions-Hydra_in_truth.txt  > analysis/Hydra/inversions/inversions_Hydra_true_positives_100-2500bp.txt
grep "SVSIM_INV.*2500-3500bp" analysis/Hydra/total_inversions-Hydra_in_truth.txt  > analysis/Hydra/inversions/inversions_Hydra_true_positives_2500-3500bp.txt
grep "SVSIM_INV.*3500-45Kbp" analysis/Hydra/total_inversions-Hydra_in_truth.txt  > analysis/Hydra/inversions/inversions_Hydra_true_positives_3500-45Kbp.txt
grep "SVSIM_INV.*45K-80Kbp" analysis/Hydra/total_inversions-Hydra_in_truth.txt  > analysis/Hydra/inversions/inversions_Hydra_true_positives_45K-80Kbp.txt
grep "SVSIM_INV.*80K-115Kbp" analysis/Hydra/total_inversions-Hydra_in_truth.txt  > analysis/Hydra/inversions/inversions_Hydra_true_positives_80K-115Kbp.txt
grep "SVSIM_INV.*115K-180Kbp" analysis/Hydra/total_inversions-Hydra_in_truth.txt  > analysis/Hydra/inversions/inversions_Hydra_true_positives_115K-180Kbp.txt
grep "SVSIM_INV.*180K-260Kbp" analysis/Hydra/total_inversions-Hydra_in_truth.txt  > analysis/Hydra/inversions/inversions_Hydra_true_positives_180K-260Kbp.txt
grep "SVSIM_INV.*260K-300Kbp" analysis/Hydra/total_inversions-Hydra_in_truth.txt  > analysis/Hydra/inversions/inversions_Hydra_true_positives_260K-300Kbp.txt
grep "SVSIM_INV.*300K-375Kbp" analysis/Hydra/total_inversions-Hydra_in_truth.txt  > analysis/Hydra/inversions/inversions_Hydra_true_positives_300K-375Kbp.txt
grep "SVSIM_INV.*375K-500Kbp" analysis/Hydra/total_inversions-Hydra_in_truth.txt  > analysis/Hydra/inversions/inversions_Hydra_true_positives_375K-500Kbp.txt
grep "SVSIM_INV.*500K-1Mbp" analysis/Hydra/total_inversions-Hydra_in_truth.txt  > analysis/Hydra/inversions/inversions_Hydra_true_positives_500K-1Mbp.txt

grep "SVSIM_DEL.*100-400bp" analysis/Hydra/total_deletions-Hydra_in_truth.txt  > analysis/Hydra/deletions/deletions_Hydra_true_positives_100-400bp.txt
grep "SVSIM_DEL.*400-600bp" analysis/Hydra/total_deletions-Hydra_in_truth.txt  > analysis/Hydra/deletions/deletions_Hydra_true_positives_400-600bp.txt
grep "SVSIM_DEL.*600-950bp" analysis/Hydra/total_deletions-Hydra_in_truth.txt  > analysis/Hydra/deletions/deletions_Hydra_true_positives_600-950bp.txt
grep "SVSIM_DEL.*950-1.2Kbp" analysis/Hydra/total_deletions-Hydra_in_truth.txt  > analysis/Hydra/deletions/deletions_Hydra_true_positives_950-1.2Kbp.txt
grep "SVSIM_DEL.*1.2K-1.5Kbp" analysis/Hydra/total_deletions-Hydra_in_truth.txt  > analysis/Hydra/deletions/deletions_Hydra_true_positives_1.2K-1.5Kbp.txt
grep "SVSIM_DEL.*1.5K-1.9Kbp" analysis/Hydra/total_deletions-Hydra_in_truth.txt  > analysis/Hydra/deletions/deletions_Hydra_true_positives_1.5K-1.9Kbp.txt
grep "SVSIM_DEL.*1.9K-2.2Kbp" analysis/Hydra/total_deletions-Hydra_in_truth.txt  > analysis/Hydra/deletions/deletions_Hydra_true_positives_1.9K-2.2Kbp.txt
grep "SVSIM_DEL.*2.2K-2.9Kbp" analysis/Hydra/total_deletions-Hydra_in_truth.txt  > analysis/Hydra/deletions/deletions_Hydra_true_positives_2.2K-2.9Kbp.txt
grep "SVSIM_DEL.*2.9K-3.6Kbp" analysis/Hydra/total_deletions-Hydra_in_truth.txt  > analysis/Hydra/deletions/deletions_Hydra_true_positives_2.9K-3.6Kbp.txt
grep "SVSIM_DEL.*3.6K-4.8Kbp" analysis/Hydra/total_deletions-Hydra_in_truth.txt  > analysis/Hydra/deletions/deletions_Hydra_true_positives_3.6K-4.8Kbp.txt
grep "SVSIM_DEL.*4.8K-6.1Kbp" analysis/Hydra/total_deletions-Hydra_in_truth.txt  > analysis/Hydra/deletions/deletions_Hydra_true_positives_4.8K-6.1Kbp.txt
grep "SVSIM_DEL.*6.1K-9Kbp" analysis/Hydra/total_deletions-Hydra_in_truth.txt  > analysis/Hydra/deletions/deletions_Hydra_true_positives_6.1K-9Kbp.txt
grep "SVSIM_DEL.*9K-18.5Kbp" analysis/Hydra/total_deletions-Hydra_in_truth.txt  > analysis/Hydra/deletions/deletions_Hydra_true_positives_9K-18.5Kbp.txt
grep "SVSIM_DEL.*18.5K-100Kbp" analysis/Hydra/total_deletions-Hydra_in_truth.txt  > analysis/Hydra/deletions/deletions_Hydra_true_positives_18.5K-100Kbp.txt
grep "SVSIM_DEL.*100K-1Mbp" analysis/Hydra/total_deletions-Hydra_in_truth.txt  > analysis/Hydra/deletions/deletions_Hydra_true_positives_100K-1Mbp.txt

# Lumpy
grep "SVSIM_DUP.*100-1Kbp" analysis/Lumpy/total_duplications-Lumpy_in_truth.txt  > analysis/Lumpy/duplications/duplications_Lumpy_true_positives_100-1Kbp.txt
grep "SVSIM_DUP.*1K-10Kbp" analysis/Lumpy/total_duplications-Lumpy_in_truth.txt  > analysis/Lumpy/duplications/duplications_Lumpy_true_positives_1K-10Kbp.txt
grep "SVSIM_DUP.*10K-50Kbp" analysis/Lumpy/total_duplications-Lumpy_in_truth.txt  > analysis/Lumpy/duplications/duplications_Lumpy_true_positives_10K-50Kbp.txt
grep "SVSIM_DUP.*50K-100Kbp" analysis/Lumpy/total_duplications-Lumpy_in_truth.txt  > analysis/Lumpy/duplications/duplications_Lumpy_true_positives_50K-100Kbp.txt
grep "SVSIM_DUP.*100K-250Kbp" analysis/Lumpy/total_duplications-Lumpy_in_truth.txt  > analysis/Lumpy/duplications/duplications_Lumpy_true_positives_100K-250Kbp.txt
grep "SVSIM_DUP.*250K-500Kbp" analysis/Lumpy/total_duplications-Lumpy_in_truth.txt  > analysis/Lumpy/duplications/duplications_Lumpy_true_positives_250K-500Kbp.txt
grep "SVSIM_DUP.*500K-1Mbp" analysis/Lumpy/total_duplications-Lumpy_in_truth.txt  > analysis/Lumpy/duplications/duplications_Lumpy_true_positives_500K-1Mbp.txt

grep "SVSIM_INV.*100-2500bp" analysis/Lumpy/total_inversions-Lumpy_in_truth.txt  > analysis/Lumpy/inversions/inversions_Lumpy_true_positives_100-2500bp.txt
grep "SVSIM_INV.*2500-3500bp" analysis/Lumpy/total_inversions-Lumpy_in_truth.txt  > analysis/Lumpy/inversions/inversions_Lumpy_true_positives_2500-3500bp.txt
grep "SVSIM_INV.*3500-45Kbp" analysis/Lumpy/total_inversions-Lumpy_in_truth.txt  > analysis/Lumpy/inversions/inversions_Lumpy_true_positives_3500-45Kbp.txt
grep "SVSIM_INV.*45K-80Kbp" analysis/Lumpy/total_inversions-Lumpy_in_truth.txt  > analysis/Lumpy/inversions/inversions_Lumpy_true_positives_45K-80Kbp.txt
grep "SVSIM_INV.*80K-115Kbp" analysis/Lumpy/total_inversions-Lumpy_in_truth.txt  > analysis/Lumpy/inversions/inversions_Lumpy_true_positives_80K-115Kbp.txt
grep "SVSIM_INV.*115K-180Kbp" analysis/Lumpy/total_inversions-Lumpy_in_truth.txt  > analysis/Lumpy/inversions/inversions_Lumpy_true_positives_115K-180Kbp.txt
grep "SVSIM_INV.*180K-260Kbp" analysis/Lumpy/total_inversions-Lumpy_in_truth.txt  > analysis/Lumpy/inversions/inversions_Lumpy_true_positives_180K-260Kbp.txt
grep "SVSIM_INV.*260K-300Kbp" analysis/Lumpy/total_inversions-Lumpy_in_truth.txt  > analysis/Lumpy/inversions/inversions_Lumpy_true_positives_260K-300Kbp.txt
grep "SVSIM_INV.*300K-375Kbp" analysis/Lumpy/total_inversions-Lumpy_in_truth.txt  > analysis/Lumpy/inversions/inversions_Lumpy_true_positives_300K-375Kbp.txt
grep "SVSIM_INV.*375K-500Kbp" analysis/Lumpy/total_inversions-Lumpy_in_truth.txt  > analysis/Lumpy/inversions/inversions_Lumpy_true_positives_375K-500Kbp.txt
grep "SVSIM_INV.*500K-1Mbp" analysis/Lumpy/total_inversions-Lumpy_in_truth.txt  > analysis/Lumpy/inversions/inversions_Lumpy_true_positives_500K-1Mbp.txt

grep "SVSIM_DEL.*100-400bp" analysis/Lumpy/total_deletions-Lumpy_in_truth.txt  > analysis/Lumpy/deletions/deletions_Lumpy_true_positives_100-400bp.txt
grep "SVSIM_DEL.*400-600bp" analysis/Lumpy/total_deletions-Lumpy_in_truth.txt  > analysis/Lumpy/deletions/deletions_Lumpy_true_positives_400-600bp.txt
grep "SVSIM_DEL.*600-950bp" analysis/Lumpy/total_deletions-Lumpy_in_truth.txt  > analysis/Lumpy/deletions/deletions_Lumpy_true_positives_600-950bp.txt
grep "SVSIM_DEL.*950-1.2Kbp" analysis/Lumpy/total_deletions-Lumpy_in_truth.txt  > analysis/Lumpy/deletions/deletions_Lumpy_true_positives_950-1.2Kbp.txt
grep "SVSIM_DEL.*1.2K-1.5Kbp" analysis/Lumpy/total_deletions-Lumpy_in_truth.txt  > analysis/Lumpy/deletions/deletions_Lumpy_true_positives_1.2K-1.5Kbp.txt
grep "SVSIM_DEL.*1.5K-1.9Kbp" analysis/Lumpy/total_deletions-Lumpy_in_truth.txt  > analysis/Lumpy/deletions/deletions_Lumpy_true_positives_1.5K-1.9Kbp.txt
grep "SVSIM_DEL.*1.9K-2.2Kbp" analysis/Lumpy/total_deletions-Lumpy_in_truth.txt  > analysis/Lumpy/deletions/deletions_Lumpy_true_positives_1.9K-2.2Kbp.txt
grep "SVSIM_DEL.*2.2K-2.9Kbp" analysis/Lumpy/total_deletions-Lumpy_in_truth.txt  > analysis/Lumpy/deletions/deletions_Lumpy_true_positives_2.2K-2.9Kbp.txt
grep "SVSIM_DEL.*2.9K-3.6Kbp" analysis/Lumpy/total_deletions-Lumpy_in_truth.txt  > analysis/Lumpy/deletions/deletions_Lumpy_true_positives_2.9K-3.6Kbp.txt
grep "SVSIM_DEL.*3.6K-4.8Kbp" analysis/Lumpy/total_deletions-Lumpy_in_truth.txt  > analysis/Lumpy/deletions/deletions_Lumpy_true_positives_3.6K-4.8Kbp.txt
grep "SVSIM_DEL.*4.8K-6.1Kbp" analysis/Lumpy/total_deletions-Lumpy_in_truth.txt  > analysis/Lumpy/deletions/deletions_Lumpy_true_positives_4.8K-6.1Kbp.txt
grep "SVSIM_DEL.*6.1K-9Kbp" analysis/Lumpy/total_deletions-Lumpy_in_truth.txt  > analysis/Lumpy/deletions/deletions_Lumpy_true_positives_6.1K-9Kbp.txt
grep "SVSIM_DEL.*9K-18.5Kbp" analysis/Lumpy/total_deletions-Lumpy_in_truth.txt  > analysis/Lumpy/deletions/deletions_Lumpy_true_positives_9K-18.5Kbp.txt
grep "SVSIM_DEL.*18.5K-100Kbp" analysis/Lumpy/total_deletions-Lumpy_in_truth.txt  > analysis/Lumpy/deletions/deletions_Lumpy_true_positives_18.5K-100Kbp.txt
grep "SVSIM_DEL.*100K-1Mbp" analysis/Lumpy/total_deletions-Lumpy_in_truth.txt  > analysis/Lumpy/deletions/deletions_Lumpy_true_positives_100K-1Mbp.txt
