# BreakDancer
awk '$6 == "-1"' analysis/BreakDancer/total_duplications-truth_in_BreakDancer.txt| grep "SVSIM_DUP.*100-1Kbp"  >  analysis/BreakDancer/duplications/duplications_BreakDancer_false_negatives_100-1Kbp.txt
awk '$6 == "-1"' analysis/BreakDancer/total_duplications-truth_in_BreakDancer.txt| grep "SVSIM_DUP.*1K-10Kbp"  >  analysis/BreakDancer/duplications/duplications_BreakDancer_false_negatives_1K-10Kbp.txt
awk '$6 == "-1"' analysis/BreakDancer/total_duplications-truth_in_BreakDancer.txt| grep "SVSIM_DUP.*10K-50Kbp"  >  analysis/BreakDancer/duplications/duplications_BreakDancer_false_negatives_10K-50Kbp.txt
awk '$6 == "-1"' analysis/BreakDancer/total_duplications-truth_in_BreakDancer.txt| grep "SVSIM_DUP.*50K-100Kbp"  >  analysis/BreakDancer/duplications/duplications_BreakDancer_false_negatives_50K-100Kbp.txt
awk '$6 == "-1"' analysis/BreakDancer/total_duplications-truth_in_BreakDancer.txt| grep "SVSIM_DUP.*100K-250Kbp"  >  analysis/BreakDancer/duplications/duplications_BreakDancer_false_negatives_100K-250Kbp.txt
awk '$6 == "-1"' analysis/BreakDancer/total_duplications-truth_in_BreakDancer.txt| grep "SVSIM_DUP.*250K-500Kbp"  >  analysis/BreakDancer/duplications/duplications_BreakDancer_false_negatives_250K-500Kbp.txt
awk '$6 == "-1"' analysis/BreakDancer/total_duplications-truth_in_BreakDancer.txt| grep "SVSIM_DUP.*500K-1Mbp"  >  analysis/BreakDancer/duplications/duplications_BreakDancer_false_negatives_500K-1Mbp.txt

awk '$6 == "-1"' analysis/BreakDancer/total_inversions-truth_in_BreakDancer.txt | grep "SVSIM_INV.*100-2500bp" >  analysis/BreakDancer/inversions/inversions_BreakDancer_false_negatives_100-2500bp.txt
awk '$6 == "-1"' analysis/BreakDancer/total_inversions-truth_in_BreakDancer.txt | grep "SVSIM_INV.*2500-3500bp" >  analysis/BreakDancer/inversions/inversions_BreakDancer_false_negatives_2500-3500bp.txt
awk '$6 == "-1"' analysis/BreakDancer/total_inversions-truth_in_BreakDancer.txt | grep "SVSIM_INV.*3500-45Kbp" >  analysis/BreakDancer/inversions/inversions_BreakDancer_false_negatives_3500-45Kbp.txt
awk '$6 == "-1"' analysis/BreakDancer/total_inversions-truth_in_BreakDancer.txt | grep "SVSIM_INV.*45K-80Kbp" >  analysis/BreakDancer/inversions/inversions_BreakDancer_false_negatives_45K-80Kbp.txt
awk '$6 == "-1"' analysis/BreakDancer/total_inversions-truth_in_BreakDancer.txt | grep "SVSIM_INV.*80K-115Kbp" >  analysis/BreakDancer/inversions/inversions_BreakDancer_false_negatives_80K-115Kbp.txt
awk '$6 == "-1"' analysis/BreakDancer/total_inversions-truth_in_BreakDancer.txt | grep "SVSIM_INV.*115K-180Kbp" >  analysis/BreakDancer/inversions/inversions_BreakDancer_false_negatives_115K-180Kbp.txt
awk '$6 == "-1"' analysis/BreakDancer/total_inversions-truth_in_BreakDancer.txt | grep "SVSIM_INV.*180K-260Kbp" >  analysis/BreakDancer/inversions/inversions_BreakDancer_false_negatives_180K-260Kbp.txt
awk '$6 == "-1"' analysis/BreakDancer/total_inversions-truth_in_BreakDancer.txt | grep "SVSIM_INV.*260K-300Kbp" >  analysis/BreakDancer/inversions/inversions_BreakDancer_false_negatives_260K-300Kbp.txt
awk '$6 == "-1"' analysis/BreakDancer/total_inversions-truth_in_BreakDancer.txt | grep "SVSIM_INV.*300K-375Kbp" >  analysis/BreakDancer/inversions/inversions_BreakDancer_false_negatives_300K-375Kbp.txt
awk '$6 == "-1"' analysis/BreakDancer/total_inversions-truth_in_BreakDancer.txt | grep "SVSIM_INV.*375K-500Kbp" >  analysis/BreakDancer/inversions/inversions_BreakDancer_false_negatives_375K-500Kbp.txt
awk '$6 == "-1"' analysis/BreakDancer/total_inversions-truth_in_BreakDancer.txt | grep "SVSIM_INV.*500K-1Mbp" >  analysis/BreakDancer/inversions/inversions_BreakDancer_false_negatives_500K-1Mbp.txt

awk '$6 == "-1"' analysis/BreakDancer/total_deletions-truth_in_BreakDancer.txt | grep "SVSIM_DEL.*100-400bp" > analysis/BreakDancer/deletions/deletions_BreakDancer_false_negatives_100-400bp.txt
awk '$6 == "-1"' analysis/BreakDancer/total_deletions-truth_in_BreakDancer.txt | grep "SVSIM_DEL.*400-600bp" > analysis/BreakDancer/deletions/deletions_BreakDancer_false_negatives_400-600bp.txt
awk '$6 == "-1"' analysis/BreakDancer/total_deletions-truth_in_BreakDancer.txt | grep "SVSIM_DEL.*600-950bp" > analysis/BreakDancer/deletions/deletions_BreakDancer_false_negatives_600-950bp.txt
awk '$6 == "-1"' analysis/BreakDancer/total_deletions-truth_in_BreakDancer.txt | grep "SVSIM_DEL.*950-1.2Kbp" > analysis/BreakDancer/deletions/deletions_BreakDancer_false_negatives_950-1.2Kbp.txt
awk '$6 == "-1"' analysis/BreakDancer/total_deletions-truth_in_BreakDancer.txt | grep "SVSIM_DEL.*1.2K-1.5Kbp" > analysis/BreakDancer/deletions/deletions_BreakDancer_false_negatives_1.2K-1.5Kbp.txt
awk '$6 == "-1"' analysis/BreakDancer/total_deletions-truth_in_BreakDancer.txt | grep "SVSIM_DEL.*1.5K-1.9Kbp" > analysis/BreakDancer/deletions/deletions_BreakDancer_false_negatives_1.5K-1.9Kbp.txt
awk '$6 == "-1"' analysis/BreakDancer/total_deletions-truth_in_BreakDancer.txt | grep "SVSIM_DEL.*1.9K-2.2Kbp" > analysis/BreakDancer/deletions/deletions_BreakDancer_false_negatives_1.9K-2.2Kbp.txt
awk '$6 == "-1"' analysis/BreakDancer/total_deletions-truth_in_BreakDancer.txt | grep "SVSIM_DEL.*2.2K-2.9Kbp" > analysis/BreakDancer/deletions/deletions_BreakDancer_false_negatives_2.2K-2.9Kbp.txt
awk '$6 == "-1"' analysis/BreakDancer/total_deletions-truth_in_BreakDancer.txt | grep "SVSIM_DEL.*2.9K-3.6Kbp" > analysis/BreakDancer/deletions/deletions_BreakDancer_false_negatives_2.9K-3.6Kbp.txt
awk '$6 == "-1"' analysis/BreakDancer/total_deletions-truth_in_BreakDancer.txt | grep "SVSIM_DEL.*3.6K-4.8Kbp" > analysis/BreakDancer/deletions/deletions_BreakDancer_false_negatives_3.6K-4.8Kbp.txt
awk '$6 == "-1"' analysis/BreakDancer/total_deletions-truth_in_BreakDancer.txt | grep "SVSIM_DEL.*4.8K-6.1Kbp" > analysis/BreakDancer/deletions/deletions_BreakDancer_false_negatives_4.8K-6.1Kbp.txt
awk '$6 == "-1"' analysis/BreakDancer/total_deletions-truth_in_BreakDancer.txt | grep "SVSIM_DEL.*6.1K-9Kbp" > analysis/BreakDancer/deletions/deletions_BreakDancer_false_negatives_6.1K-9Kbp.txt
awk '$6 == "-1"' analysis/BreakDancer/total_deletions-truth_in_BreakDancer.txt | grep "SVSIM_DEL.*9K-18.5Kbp" > analysis/BreakDancer/deletions/deletions_BreakDancer_false_negatives_9K-18.5Kbp.txt
awk '$6 == "-1"' analysis/BreakDancer/total_deletions-truth_in_BreakDancer.txt | grep "SVSIM_DEL.*18.5K-100Kbp" > analysis/BreakDancer/deletions/deletions_BreakDancer_false_negatives_18.5K-100Kbp.txt
awk '$6 == "-1"' analysis/BreakDancer/total_deletions-truth_in_BreakDancer.txt | grep "SVSIM_DEL.*100K-1Mbp" > analysis/BreakDancer/deletions/deletions_BreakDancer_false_negatives_100K-1Mbp.txt

# cnMOPS
awk '$6 == "-1"' analysis/cnMOPS/total_duplications-truth_in_cnMOPS.txt| grep "SVSIM_DUP.*100-1Kbp"  >  analysis/cnMOPS/duplications/duplications_cnMOPS_false_negatives_100-1Kbp.txt
awk '$6 == "-1"' analysis/cnMOPS/total_duplications-truth_in_cnMOPS.txt| grep "SVSIM_DUP.*1K-10Kbp"  >  analysis/cnMOPS/duplications/duplications_cnMOPS_false_negatives_1K-10Kbp.txt
awk '$6 == "-1"' analysis/cnMOPS/total_duplications-truth_in_cnMOPS.txt| grep "SVSIM_DUP.*10K-50Kbp"  >  analysis/cnMOPS/duplications/duplications_cnMOPS_false_negatives_10K-50Kbp.txt
awk '$6 == "-1"' analysis/cnMOPS/total_duplications-truth_in_cnMOPS.txt| grep "SVSIM_DUP.*50K-100Kbp"  >  analysis/cnMOPS/duplications/duplications_cnMOPS_false_negatives_50K-100Kbp.txt
awk '$6 == "-1"' analysis/cnMOPS/total_duplications-truth_in_cnMOPS.txt| grep "SVSIM_DUP.*100K-250Kbp"  >  analysis/cnMOPS/duplications/duplications_cnMOPS_false_negatives_100K-250Kbp.txt
awk '$6 == "-1"' analysis/cnMOPS/total_duplications-truth_in_cnMOPS.txt| grep "SVSIM_DUP.*250K-500Kbp"  >  analysis/cnMOPS/duplications/duplications_cnMOPS_false_negatives_250K-500Kbp.txt
awk '$6 == "-1"' analysis/cnMOPS/total_duplications-truth_in_cnMOPS.txt| grep "SVSIM_DUP.*500K-1Mbp"  >  analysis/cnMOPS/duplications/duplications_cnMOPS_false_negatives_500K-1Mbp.txt

awk '$6 == "-1"' analysis/cnMOPS/total_inversions-truth_in_cnMOPS.txt | grep "SVSIM_INV.*100-2500bp" >  analysis/cnMOPS/inversions/inversions_cnMOPS_false_negatives_100-2500bp.txt
awk '$6 == "-1"' analysis/cnMOPS/total_inversions-truth_in_cnMOPS.txt | grep "SVSIM_INV.*2500-3500bp" >  analysis/cnMOPS/inversions/inversions_cnMOPS_false_negatives_2500-3500bp.txt
awk '$6 == "-1"' analysis/cnMOPS/total_inversions-truth_in_cnMOPS.txt | grep "SVSIM_INV.*3500-45Kbp" >  analysis/cnMOPS/inversions/inversions_cnMOPS_false_negatives_3500-45Kbp.txt
awk '$6 == "-1"' analysis/cnMOPS/total_inversions-truth_in_cnMOPS.txt | grep "SVSIM_INV.*45K-80Kbp" >  analysis/cnMOPS/inversions/inversions_cnMOPS_false_negatives_45K-80Kbp.txt
awk '$6 == "-1"' analysis/cnMOPS/total_inversions-truth_in_cnMOPS.txt | grep "SVSIM_INV.*80K-115Kbp" >  analysis/cnMOPS/inversions/inversions_cnMOPS_false_negatives_80K-115Kbp.txt
awk '$6 == "-1"' analysis/cnMOPS/total_inversions-truth_in_cnMOPS.txt | grep "SVSIM_INV.*115K-180Kbp" >  analysis/cnMOPS/inversions/inversions_cnMOPS_false_negatives_115K-180Kbp.txt
awk '$6 == "-1"' analysis/cnMOPS/total_inversions-truth_in_cnMOPS.txt | grep "SVSIM_INV.*180K-260Kbp" >  analysis/cnMOPS/inversions/inversions_cnMOPS_false_negatives_180K-260Kbp.txt
awk '$6 == "-1"' analysis/cnMOPS/total_inversions-truth_in_cnMOPS.txt | grep "SVSIM_INV.*260K-300Kbp" >  analysis/cnMOPS/inversions/inversions_cnMOPS_false_negatives_260K-300Kbp.txt
awk '$6 == "-1"' analysis/cnMOPS/total_inversions-truth_in_cnMOPS.txt | grep "SVSIM_INV.*300K-375Kbp" >  analysis/cnMOPS/inversions/inversions_cnMOPS_false_negatives_300K-375Kbp.txt
awk '$6 == "-1"' analysis/cnMOPS/total_inversions-truth_in_cnMOPS.txt | grep "SVSIM_INV.*375K-500Kbp" >  analysis/cnMOPS/inversions/inversions_cnMOPS_false_negatives_375K-500Kbp.txt
awk '$6 == "-1"' analysis/cnMOPS/total_inversions-truth_in_cnMOPS.txt | grep "SVSIM_INV.*500K-1Mbp" >  analysis/cnMOPS/inversions/inversions_cnMOPS_false_negatives_500K-1Mbp.txt

awk '$6 == "-1"' analysis/cnMOPS/total_deletions-truth_in_cnMOPS.txt | grep "SVSIM_DEL.*100-400bp" > analysis/cnMOPS/deletions/deletions_cnMOPS_false_negatives_100-400bp.txt
awk '$6 == "-1"' analysis/cnMOPS/total_deletions-truth_in_cnMOPS.txt | grep "SVSIM_DEL.*400-600bp" > analysis/cnMOPS/deletions/deletions_cnMOPS_false_negatives_400-600bp.txt
awk '$6 == "-1"' analysis/cnMOPS/total_deletions-truth_in_cnMOPS.txt | grep "SVSIM_DEL.*600-950bp" > analysis/cnMOPS/deletions/deletions_cnMOPS_false_negatives_600-950bp.txt
awk '$6 == "-1"' analysis/cnMOPS/total_deletions-truth_in_cnMOPS.txt | grep "SVSIM_DEL.*950-1.2Kbp" > analysis/cnMOPS/deletions/deletions_cnMOPS_false_negatives_950-1.2Kbp.txt
awk '$6 == "-1"' analysis/cnMOPS/total_deletions-truth_in_cnMOPS.txt | grep "SVSIM_DEL.*1.2K-1.5Kbp" > analysis/cnMOPS/deletions/deletions_cnMOPS_false_negatives_1.2K-1.5Kbp.txt
awk '$6 == "-1"' analysis/cnMOPS/total_deletions-truth_in_cnMOPS.txt | grep "SVSIM_DEL.*1.5K-1.9Kbp" > analysis/cnMOPS/deletions/deletions_cnMOPS_false_negatives_1.5K-1.9Kbp.txt
awk '$6 == "-1"' analysis/cnMOPS/total_deletions-truth_in_cnMOPS.txt | grep "SVSIM_DEL.*1.9K-2.2Kbp" > analysis/cnMOPS/deletions/deletions_cnMOPS_false_negatives_1.9K-2.2Kbp.txt
awk '$6 == "-1"' analysis/cnMOPS/total_deletions-truth_in_cnMOPS.txt | grep "SVSIM_DEL.*2.2K-2.9Kbp" > analysis/cnMOPS/deletions/deletions_cnMOPS_false_negatives_2.2K-2.9Kbp.txt
awk '$6 == "-1"' analysis/cnMOPS/total_deletions-truth_in_cnMOPS.txt | grep "SVSIM_DEL.*2.9K-3.6Kbp" > analysis/cnMOPS/deletions/deletions_cnMOPS_false_negatives_2.9K-3.6Kbp.txt
awk '$6 == "-1"' analysis/cnMOPS/total_deletions-truth_in_cnMOPS.txt | grep "SVSIM_DEL.*3.6K-4.8Kbp" > analysis/cnMOPS/deletions/deletions_cnMOPS_false_negatives_3.6K-4.8Kbp.txt
awk '$6 == "-1"' analysis/cnMOPS/total_deletions-truth_in_cnMOPS.txt | grep "SVSIM_DEL.*4.8K-6.1Kbp" > analysis/cnMOPS/deletions/deletions_cnMOPS_false_negatives_4.8K-6.1Kbp.txt
awk '$6 == "-1"' analysis/cnMOPS/total_deletions-truth_in_cnMOPS.txt | grep "SVSIM_DEL.*6.1K-9Kbp" > analysis/cnMOPS/deletions/deletions_cnMOPS_false_negatives_6.1K-9Kbp.txt
awk '$6 == "-1"' analysis/cnMOPS/total_deletions-truth_in_cnMOPS.txt | grep "SVSIM_DEL.*9K-18.5Kbp" > analysis/cnMOPS/deletions/deletions_cnMOPS_false_negatives_9K-18.5Kbp.txt
awk '$6 == "-1"' analysis/cnMOPS/total_deletions-truth_in_cnMOPS.txt | grep "SVSIM_DEL.*18.5K-100Kbp" > analysis/cnMOPS/deletions/deletions_cnMOPS_false_negatives_18.5K-100Kbp.txt
awk '$6 == "-1"' analysis/cnMOPS/total_deletions-truth_in_cnMOPS.txt | grep "SVSIM_DEL.*100K-1Mbp" > analysis/cnMOPS/deletions/deletions_cnMOPS_false_negatives_100K-1Mbp.txt

# CNVnator
awk '$6 == "-1"' analysis/CNVnator/total_duplications-truth_in_CNVnator.txt| grep "SVSIM_DUP.*100-1Kbp"  >  analysis/CNVnator/duplications/duplications_CNVnator_false_negatives_100-1Kbp.txt
awk '$6 == "-1"' analysis/CNVnator/total_duplications-truth_in_CNVnator.txt| grep "SVSIM_DUP.*1K-10Kbp"  >  analysis/CNVnator/duplications/duplications_CNVnator_false_negatives_1K-10Kbp.txt
awk '$6 == "-1"' analysis/CNVnator/total_duplications-truth_in_CNVnator.txt| grep "SVSIM_DUP.*10K-50Kbp"  >  analysis/CNVnator/duplications/duplications_CNVnator_false_negatives_10K-50Kbp.txt
awk '$6 == "-1"' analysis/CNVnator/total_duplications-truth_in_CNVnator.txt| grep "SVSIM_DUP.*50K-100Kbp"  >  analysis/CNVnator/duplications/duplications_CNVnator_false_negatives_50K-100Kbp.txt
awk '$6 == "-1"' analysis/CNVnator/total_duplications-truth_in_CNVnator.txt| grep "SVSIM_DUP.*100K-250Kbp"  >  analysis/CNVnator/duplications/duplications_CNVnator_false_negatives_100K-250Kbp.txt
awk '$6 == "-1"' analysis/CNVnator/total_duplications-truth_in_CNVnator.txt| grep "SVSIM_DUP.*250K-500Kbp"  >  analysis/CNVnator/duplications/duplications_CNVnator_false_negatives_250K-500Kbp.txt
awk '$6 == "-1"' analysis/CNVnator/total_duplications-truth_in_CNVnator.txt| grep "SVSIM_DUP.*500K-1Mbp"  >  analysis/CNVnator/duplications/duplications_CNVnator_false_negatives_500K-1Mbp.txt

awk '$6 == "-1"' analysis/CNVnator/total_inversions-truth_in_CNVnator.txt | grep "SVSIM_INV.*100-2500bp" >  analysis/CNVnator/inversions/inversions_CNVnator_false_negatives_100-2500bp.txt
awk '$6 == "-1"' analysis/CNVnator/total_inversions-truth_in_CNVnator.txt | grep "SVSIM_INV.*2500-3500bp" >  analysis/CNVnator/inversions/inversions_CNVnator_false_negatives_2500-3500bp.txt
awk '$6 == "-1"' analysis/CNVnator/total_inversions-truth_in_CNVnator.txt | grep "SVSIM_INV.*3500-45Kbp" >  analysis/CNVnator/inversions/inversions_CNVnator_false_negatives_3500-45Kbp.txt
awk '$6 == "-1"' analysis/CNVnator/total_inversions-truth_in_CNVnator.txt | grep "SVSIM_INV.*45K-80Kbp" >  analysis/CNVnator/inversions/inversions_CNVnator_false_negatives_45K-80Kbp.txt
awk '$6 == "-1"' analysis/CNVnator/total_inversions-truth_in_CNVnator.txt | grep "SVSIM_INV.*80K-115Kbp" >  analysis/CNVnator/inversions/inversions_CNVnator_false_negatives_80K-115Kbp.txt
awk '$6 == "-1"' analysis/CNVnator/total_inversions-truth_in_CNVnator.txt | grep "SVSIM_INV.*115K-180Kbp" >  analysis/CNVnator/inversions/inversions_CNVnator_false_negatives_115K-180Kbp.txt
awk '$6 == "-1"' analysis/CNVnator/total_inversions-truth_in_CNVnator.txt | grep "SVSIM_INV.*180K-260Kbp" >  analysis/CNVnator/inversions/inversions_CNVnator_false_negatives_180K-260Kbp.txt
awk '$6 == "-1"' analysis/CNVnator/total_inversions-truth_in_CNVnator.txt | grep "SVSIM_INV.*260K-300Kbp" >  analysis/CNVnator/inversions/inversions_CNVnator_false_negatives_260K-300Kbp.txt
awk '$6 == "-1"' analysis/CNVnator/total_inversions-truth_in_CNVnator.txt | grep "SVSIM_INV.*300K-375Kbp" >  analysis/CNVnator/inversions/inversions_CNVnator_false_negatives_300K-375Kbp.txt
awk '$6 == "-1"' analysis/CNVnator/total_inversions-truth_in_CNVnator.txt | grep "SVSIM_INV.*375K-500Kbp" >  analysis/CNVnator/inversions/inversions_CNVnator_false_negatives_375K-500Kbp.txt
awk '$6 == "-1"' analysis/CNVnator/total_inversions-truth_in_CNVnator.txt | grep "SVSIM_INV.*500K-1Mbp" >  analysis/CNVnator/inversions/inversions_CNVnator_false_negatives_500K-1Mbp.txt

awk '$6 == "-1"' analysis/CNVnator/total_deletions-truth_in_CNVnator.txt | grep "SVSIM_DEL.*100-400bp" > analysis/CNVnator/deletions/deletions_CNVnator_false_negatives_100-400bp.txt
awk '$6 == "-1"' analysis/CNVnator/total_deletions-truth_in_CNVnator.txt | grep "SVSIM_DEL.*400-600bp" > analysis/CNVnator/deletions/deletions_CNVnator_false_negatives_400-600bp.txt
awk '$6 == "-1"' analysis/CNVnator/total_deletions-truth_in_CNVnator.txt | grep "SVSIM_DEL.*600-950bp" > analysis/CNVnator/deletions/deletions_CNVnator_false_negatives_600-950bp.txt
awk '$6 == "-1"' analysis/CNVnator/total_deletions-truth_in_CNVnator.txt | grep "SVSIM_DEL.*950-1.2Kbp" > analysis/CNVnator/deletions/deletions_CNVnator_false_negatives_950-1.2Kbp.txt
awk '$6 == "-1"' analysis/CNVnator/total_deletions-truth_in_CNVnator.txt | grep "SVSIM_DEL.*1.2K-1.5Kbp" > analysis/CNVnator/deletions/deletions_CNVnator_false_negatives_1.2K-1.5Kbp.txt
awk '$6 == "-1"' analysis/CNVnator/total_deletions-truth_in_CNVnator.txt | grep "SVSIM_DEL.*1.5K-1.9Kbp" > analysis/CNVnator/deletions/deletions_CNVnator_false_negatives_1.5K-1.9Kbp.txt
awk '$6 == "-1"' analysis/CNVnator/total_deletions-truth_in_CNVnator.txt | grep "SVSIM_DEL.*1.9K-2.2Kbp" > analysis/CNVnator/deletions/deletions_CNVnator_false_negatives_1.9K-2.2Kbp.txt
awk '$6 == "-1"' analysis/CNVnator/total_deletions-truth_in_CNVnator.txt | grep "SVSIM_DEL.*2.2K-2.9Kbp" > analysis/CNVnator/deletions/deletions_CNVnator_false_negatives_2.2K-2.9Kbp.txt
awk '$6 == "-1"' analysis/CNVnator/total_deletions-truth_in_CNVnator.txt | grep "SVSIM_DEL.*2.9K-3.6Kbp" > analysis/CNVnator/deletions/deletions_CNVnator_false_negatives_2.9K-3.6Kbp.txt
awk '$6 == "-1"' analysis/CNVnator/total_deletions-truth_in_CNVnator.txt | grep "SVSIM_DEL.*3.6K-4.8Kbp" > analysis/CNVnator/deletions/deletions_CNVnator_false_negatives_3.6K-4.8Kbp.txt
awk '$6 == "-1"' analysis/CNVnator/total_deletions-truth_in_CNVnator.txt | grep "SVSIM_DEL.*4.8K-6.1Kbp" > analysis/CNVnator/deletions/deletions_CNVnator_false_negatives_4.8K-6.1Kbp.txt
awk '$6 == "-1"' analysis/CNVnator/total_deletions-truth_in_CNVnator.txt | grep "SVSIM_DEL.*6.1K-9Kbp" > analysis/CNVnator/deletions/deletions_CNVnator_false_negatives_6.1K-9Kbp.txt
awk '$6 == "-1"' analysis/CNVnator/total_deletions-truth_in_CNVnator.txt | grep "SVSIM_DEL.*9K-18.5Kbp" > analysis/CNVnator/deletions/deletions_CNVnator_false_negatives_9K-18.5Kbp.txt
awk '$6 == "-1"' analysis/CNVnator/total_deletions-truth_in_CNVnator.txt | grep "SVSIM_DEL.*18.5K-100Kbp" > analysis/CNVnator/deletions/deletions_CNVnator_false_negatives_18.5K-100Kbp.txt
awk '$6 == "-1"' analysis/CNVnator/total_deletions-truth_in_CNVnator.txt | grep "SVSIM_DEL.*100K-1Mbp" > analysis/CNVnator/deletions/deletions_CNVnator_false_negatives_100K-1Mbp.txt

# Delly
awk '$6 == "-1"' analysis/Delly/total_duplications-truth_in_Delly.txt| grep "SVSIM_DUP.*100-1Kbp"  >  analysis/Delly/duplications/duplications_Delly_false_negatives_100-1Kbp.txt
awk '$6 == "-1"' analysis/Delly/total_duplications-truth_in_Delly.txt| grep "SVSIM_DUP.*1K-10Kbp"  >  analysis/Delly/duplications/duplications_Delly_false_negatives_1K-10Kbp.txt
awk '$6 == "-1"' analysis/Delly/total_duplications-truth_in_Delly.txt| grep "SVSIM_DUP.*10K-50Kbp"  >  analysis/Delly/duplications/duplications_Delly_false_negatives_10K-50Kbp.txt
awk '$6 == "-1"' analysis/Delly/total_duplications-truth_in_Delly.txt| grep "SVSIM_DUP.*50K-100Kbp"  >  analysis/Delly/duplications/duplications_Delly_false_negatives_50K-100Kbp.txt
awk '$6 == "-1"' analysis/Delly/total_duplications-truth_in_Delly.txt| grep "SVSIM_DUP.*100K-250Kbp"  >  analysis/Delly/duplications/duplications_Delly_false_negatives_100K-250Kbp.txt
awk '$6 == "-1"' analysis/Delly/total_duplications-truth_in_Delly.txt| grep "SVSIM_DUP.*250K-500Kbp"  >  analysis/Delly/duplications/duplications_Delly_false_negatives_250K-500Kbp.txt
awk '$6 == "-1"' analysis/Delly/total_duplications-truth_in_Delly.txt| grep "SVSIM_DUP.*500K-1Mbp"  >  analysis/Delly/duplications/duplications_Delly_false_negatives_500K-1Mbp.txt

awk '$6 == "-1"' analysis/Delly/total_inversions-truth_in_Delly.txt | grep "SVSIM_INV.*100-2500bp" >  analysis/Delly/inversions/inversions_Delly_false_negatives_100-2500bp.txt
awk '$6 == "-1"' analysis/Delly/total_inversions-truth_in_Delly.txt | grep "SVSIM_INV.*2500-3500bp" >  analysis/Delly/inversions/inversions_Delly_false_negatives_2500-3500bp.txt
awk '$6 == "-1"' analysis/Delly/total_inversions-truth_in_Delly.txt | grep "SVSIM_INV.*3500-45Kbp" >  analysis/Delly/inversions/inversions_Delly_false_negatives_3500-45Kbp.txt
awk '$6 == "-1"' analysis/Delly/total_inversions-truth_in_Delly.txt | grep "SVSIM_INV.*45K-80Kbp" >  analysis/Delly/inversions/inversions_Delly_false_negatives_45K-80Kbp.txt
awk '$6 == "-1"' analysis/Delly/total_inversions-truth_in_Delly.txt | grep "SVSIM_INV.*80K-115Kbp" >  analysis/Delly/inversions/inversions_Delly_false_negatives_80K-115Kbp.txt
awk '$6 == "-1"' analysis/Delly/total_inversions-truth_in_Delly.txt | grep "SVSIM_INV.*115K-180Kbp" >  analysis/Delly/inversions/inversions_Delly_false_negatives_115K-180Kbp.txt
awk '$6 == "-1"' analysis/Delly/total_inversions-truth_in_Delly.txt | grep "SVSIM_INV.*180K-260Kbp" >  analysis/Delly/inversions/inversions_Delly_false_negatives_180K-260Kbp.txt
awk '$6 == "-1"' analysis/Delly/total_inversions-truth_in_Delly.txt | grep "SVSIM_INV.*260K-300Kbp" >  analysis/Delly/inversions/inversions_Delly_false_negatives_260K-300Kbp.txt
awk '$6 == "-1"' analysis/Delly/total_inversions-truth_in_Delly.txt | grep "SVSIM_INV.*300K-375Kbp" >  analysis/Delly/inversions/inversions_Delly_false_negatives_300K-375Kbp.txt
awk '$6 == "-1"' analysis/Delly/total_inversions-truth_in_Delly.txt | grep "SVSIM_INV.*375K-500Kbp" >  analysis/Delly/inversions/inversions_Delly_false_negatives_375K-500Kbp.txt
awk '$6 == "-1"' analysis/Delly/total_inversions-truth_in_Delly.txt | grep "SVSIM_INV.*500K-1Mbp" >  analysis/Delly/inversions/inversions_Delly_false_negatives_500K-1Mbp.txt

awk '$6 == "-1"' analysis/Delly/total_deletions-truth_in_Delly.txt | grep "SVSIM_DEL.*100-400bp" > analysis/Delly/deletions/deletions_Delly_false_negatives_100-400bp.txt
awk '$6 == "-1"' analysis/Delly/total_deletions-truth_in_Delly.txt | grep "SVSIM_DEL.*400-600bp" > analysis/Delly/deletions/deletions_Delly_false_negatives_400-600bp.txt
awk '$6 == "-1"' analysis/Delly/total_deletions-truth_in_Delly.txt | grep "SVSIM_DEL.*600-950bp" > analysis/Delly/deletions/deletions_Delly_false_negatives_600-950bp.txt
awk '$6 == "-1"' analysis/Delly/total_deletions-truth_in_Delly.txt | grep "SVSIM_DEL.*950-1.2Kbp" > analysis/Delly/deletions/deletions_Delly_false_negatives_950-1.2Kbp.txt
awk '$6 == "-1"' analysis/Delly/total_deletions-truth_in_Delly.txt | grep "SVSIM_DEL.*1.2K-1.5Kbp" > analysis/Delly/deletions/deletions_Delly_false_negatives_1.2K-1.5Kbp.txt
awk '$6 == "-1"' analysis/Delly/total_deletions-truth_in_Delly.txt | grep "SVSIM_DEL.*1.5K-1.9Kbp" > analysis/Delly/deletions/deletions_Delly_false_negatives_1.5K-1.9Kbp.txt
awk '$6 == "-1"' analysis/Delly/total_deletions-truth_in_Delly.txt | grep "SVSIM_DEL.*1.9K-2.2Kbp" > analysis/Delly/deletions/deletions_Delly_false_negatives_1.9K-2.2Kbp.txt
awk '$6 == "-1"' analysis/Delly/total_deletions-truth_in_Delly.txt | grep "SVSIM_DEL.*2.2K-2.9Kbp" > analysis/Delly/deletions/deletions_Delly_false_negatives_2.2K-2.9Kbp.txt
awk '$6 == "-1"' analysis/Delly/total_deletions-truth_in_Delly.txt | grep "SVSIM_DEL.*2.9K-3.6Kbp" > analysis/Delly/deletions/deletions_Delly_false_negatives_2.9K-3.6Kbp.txt
awk '$6 == "-1"' analysis/Delly/total_deletions-truth_in_Delly.txt | grep "SVSIM_DEL.*3.6K-4.8Kbp" > analysis/Delly/deletions/deletions_Delly_false_negatives_3.6K-4.8Kbp.txt
awk '$6 == "-1"' analysis/Delly/total_deletions-truth_in_Delly.txt | grep "SVSIM_DEL.*4.8K-6.1Kbp" > analysis/Delly/deletions/deletions_Delly_false_negatives_4.8K-6.1Kbp.txt
awk '$6 == "-1"' analysis/Delly/total_deletions-truth_in_Delly.txt | grep "SVSIM_DEL.*6.1K-9Kbp" > analysis/Delly/deletions/deletions_Delly_false_negatives_6.1K-9Kbp.txt
awk '$6 == "-1"' analysis/Delly/total_deletions-truth_in_Delly.txt | grep "SVSIM_DEL.*9K-18.5Kbp" > analysis/Delly/deletions/deletions_Delly_false_negatives_9K-18.5Kbp.txt
awk '$6 == "-1"' analysis/Delly/total_deletions-truth_in_Delly.txt | grep "SVSIM_DEL.*18.5K-100Kbp" > analysis/Delly/deletions/deletions_Delly_false_negatives_18.5K-100Kbp.txt
awk '$6 == "-1"' analysis/Delly/total_deletions-truth_in_Delly.txt | grep "SVSIM_DEL.*100K-1Mbp" > analysis/Delly/deletions/deletions_Delly_false_negatives_100K-1Mbp.txt

# Hydra
awk '$6 == "-1"' analysis/Hydra/total_duplications-truth_in_Hydra.txt| grep "SVSIM_DUP.*100-1Kbp"  >  analysis/Hydra/duplications/duplications_Hydra_false_negatives_100-1Kbp.txt
awk '$6 == "-1"' analysis/Hydra/total_duplications-truth_in_Hydra.txt| grep "SVSIM_DUP.*1K-10Kbp"  >  analysis/Hydra/duplications/duplications_Hydra_false_negatives_1K-10Kbp.txt
awk '$6 == "-1"' analysis/Hydra/total_duplications-truth_in_Hydra.txt| grep "SVSIM_DUP.*10K-50Kbp"  >  analysis/Hydra/duplications/duplications_Hydra_false_negatives_10K-50Kbp.txt
awk '$6 == "-1"' analysis/Hydra/total_duplications-truth_in_Hydra.txt| grep "SVSIM_DUP.*50K-100Kbp"  >  analysis/Hydra/duplications/duplications_Hydra_false_negatives_50K-100Kbp.txt
awk '$6 == "-1"' analysis/Hydra/total_duplications-truth_in_Hydra.txt| grep "SVSIM_DUP.*100K-250Kbp"  >  analysis/Hydra/duplications/duplications_Hydra_false_negatives_100K-250Kbp.txt
awk '$6 == "-1"' analysis/Hydra/total_duplications-truth_in_Hydra.txt| grep "SVSIM_DUP.*250K-500Kbp"  >  analysis/Hydra/duplications/duplications_Hydra_false_negatives_250K-500Kbp.txt
awk '$6 == "-1"' analysis/Hydra/total_duplications-truth_in_Hydra.txt| grep "SVSIM_DUP.*500K-1Mbp"  >  analysis/Hydra/duplications/duplications_Hydra_false_negatives_500K-1Mbp.txt

awk '$6 == "-1"' analysis/Hydra/total_inversions-truth_in_Hydra.txt | grep "SVSIM_INV.*100-2500bp" >  analysis/Hydra/inversions/inversions_Hydra_false_negatives_100-2500bp.txt
awk '$6 == "-1"' analysis/Hydra/total_inversions-truth_in_Hydra.txt | grep "SVSIM_INV.*2500-3500bp" >  analysis/Hydra/inversions/inversions_Hydra_false_negatives_2500-3500bp.txt
awk '$6 == "-1"' analysis/Hydra/total_inversions-truth_in_Hydra.txt | grep "SVSIM_INV.*3500-45Kbp" >  analysis/Hydra/inversions/inversions_Hydra_false_negatives_3500-45Kbp.txt
awk '$6 == "-1"' analysis/Hydra/total_inversions-truth_in_Hydra.txt | grep "SVSIM_INV.*45K-80Kbp" >  analysis/Hydra/inversions/inversions_Hydra_false_negatives_45K-80Kbp.txt
awk '$6 == "-1"' analysis/Hydra/total_inversions-truth_in_Hydra.txt | grep "SVSIM_INV.*80K-115Kbp" >  analysis/Hydra/inversions/inversions_Hydra_false_negatives_80K-115Kbp.txt
awk '$6 == "-1"' analysis/Hydra/total_inversions-truth_in_Hydra.txt | grep "SVSIM_INV.*115K-180Kbp" >  analysis/Hydra/inversions/inversions_Hydra_false_negatives_115K-180Kbp.txt
awk '$6 == "-1"' analysis/Hydra/total_inversions-truth_in_Hydra.txt | grep "SVSIM_INV.*180K-260Kbp" >  analysis/Hydra/inversions/inversions_Hydra_false_negatives_180K-260Kbp.txt
awk '$6 == "-1"' analysis/Hydra/total_inversions-truth_in_Hydra.txt | grep "SVSIM_INV.*260K-300Kbp" >  analysis/Hydra/inversions/inversions_Hydra_false_negatives_260K-300Kbp.txt
awk '$6 == "-1"' analysis/Hydra/total_inversions-truth_in_Hydra.txt | grep "SVSIM_INV.*300K-375Kbp" >  analysis/Hydra/inversions/inversions_Hydra_false_negatives_300K-375Kbp.txt
awk '$6 == "-1"' analysis/Hydra/total_inversions-truth_in_Hydra.txt | grep "SVSIM_INV.*375K-500Kbp" >  analysis/Hydra/inversions/inversions_Hydra_false_negatives_375K-500Kbp.txt
awk '$6 == "-1"' analysis/Hydra/total_inversions-truth_in_Hydra.txt | grep "SVSIM_INV.*500K-1Mbp" >  analysis/Hydra/inversions/inversions_Hydra_false_negatives_500K-1Mbp.txt

awk '$6 == "-1"' analysis/Hydra/total_deletions-truth_in_Hydra.txt | grep "SVSIM_DEL.*100-400bp" > analysis/Hydra/deletions/deletions_Hydra_false_negatives_100-400bp.txt
awk '$6 == "-1"' analysis/Hydra/total_deletions-truth_in_Hydra.txt | grep "SVSIM_DEL.*400-600bp" > analysis/Hydra/deletions/deletions_Hydra_false_negatives_400-600bp.txt
awk '$6 == "-1"' analysis/Hydra/total_deletions-truth_in_Hydra.txt | grep "SVSIM_DEL.*600-950bp" > analysis/Hydra/deletions/deletions_Hydra_false_negatives_600-950bp.txt
awk '$6 == "-1"' analysis/Hydra/total_deletions-truth_in_Hydra.txt | grep "SVSIM_DEL.*950-1.2Kbp" > analysis/Hydra/deletions/deletions_Hydra_false_negatives_950-1.2Kbp.txt
awk '$6 == "-1"' analysis/Hydra/total_deletions-truth_in_Hydra.txt | grep "SVSIM_DEL.*1.2K-1.5Kbp" > analysis/Hydra/deletions/deletions_Hydra_false_negatives_1.2K-1.5Kbp.txt
awk '$6 == "-1"' analysis/Hydra/total_deletions-truth_in_Hydra.txt | grep "SVSIM_DEL.*1.5K-1.9Kbp" > analysis/Hydra/deletions/deletions_Hydra_false_negatives_1.5K-1.9Kbp.txt
awk '$6 == "-1"' analysis/Hydra/total_deletions-truth_in_Hydra.txt | grep "SVSIM_DEL.*1.9K-2.2Kbp" > analysis/Hydra/deletions/deletions_Hydra_false_negatives_1.9K-2.2Kbp.txt
awk '$6 == "-1"' analysis/Hydra/total_deletions-truth_in_Hydra.txt | grep "SVSIM_DEL.*2.2K-2.9Kbp" > analysis/Hydra/deletions/deletions_Hydra_false_negatives_2.2K-2.9Kbp.txt
awk '$6 == "-1"' analysis/Hydra/total_deletions-truth_in_Hydra.txt | grep "SVSIM_DEL.*2.9K-3.6Kbp" > analysis/Hydra/deletions/deletions_Hydra_false_negatives_2.9K-3.6Kbp.txt
awk '$6 == "-1"' analysis/Hydra/total_deletions-truth_in_Hydra.txt | grep "SVSIM_DEL.*3.6K-4.8Kbp" > analysis/Hydra/deletions/deletions_Hydra_false_negatives_3.6K-4.8Kbp.txt
awk '$6 == "-1"' analysis/Hydra/total_deletions-truth_in_Hydra.txt | grep "SVSIM_DEL.*4.8K-6.1Kbp" > analysis/Hydra/deletions/deletions_Hydra_false_negatives_4.8K-6.1Kbp.txt
awk '$6 == "-1"' analysis/Hydra/total_deletions-truth_in_Hydra.txt | grep "SVSIM_DEL.*6.1K-9Kbp" > analysis/Hydra/deletions/deletions_Hydra_false_negatives_6.1K-9Kbp.txt
awk '$6 == "-1"' analysis/Hydra/total_deletions-truth_in_Hydra.txt | grep "SVSIM_DEL.*9K-18.5Kbp" > analysis/Hydra/deletions/deletions_Hydra_false_negatives_9K-18.5Kbp.txt
awk '$6 == "-1"' analysis/Hydra/total_deletions-truth_in_Hydra.txt | grep "SVSIM_DEL.*18.5K-100Kbp" > analysis/Hydra/deletions/deletions_Hydra_false_negatives_18.5K-100Kbp.txt
awk '$6 == "-1"' analysis/Hydra/total_deletions-truth_in_Hydra.txt | grep "SVSIM_DEL.*100K-1Mbp" > analysis/Hydra/deletions/deletions_Hydra_false_negatives_100K-1Mbp.txt

# Lumpy
awk '$6 == "-1"' analysis/Lumpy/total_duplications-truth_in_Lumpy.txt| grep "SVSIM_DUP.*100-1Kbp"  >  analysis/Lumpy/duplications/duplications_Lumpy_false_negatives_100-1Kbp.txt
awk '$6 == "-1"' analysis/Lumpy/total_duplications-truth_in_Lumpy.txt| grep "SVSIM_DUP.*1K-10Kbp"  >  analysis/Lumpy/duplications/duplications_Lumpy_false_negatives_1K-10Kbp.txt
awk '$6 == "-1"' analysis/Lumpy/total_duplications-truth_in_Lumpy.txt| grep "SVSIM_DUP.*10K-50Kbp"  >  analysis/Lumpy/duplications/duplications_Lumpy_false_negatives_10K-50Kbp.txt
awk '$6 == "-1"' analysis/Lumpy/total_duplications-truth_in_Lumpy.txt| grep "SVSIM_DUP.*50K-100Kbp"  >  analysis/Lumpy/duplications/duplications_Lumpy_false_negatives_50K-100Kbp.txt
awk '$6 == "-1"' analysis/Lumpy/total_duplications-truth_in_Lumpy.txt| grep "SVSIM_DUP.*100K-250Kbp"  >  analysis/Lumpy/duplications/duplications_Lumpy_false_negatives_100K-250Kbp.txt
awk '$6 == "-1"' analysis/Lumpy/total_duplications-truth_in_Lumpy.txt| grep "SVSIM_DUP.*250K-500Kbp"  >  analysis/Lumpy/duplications/duplications_Lumpy_false_negatives_250K-500Kbp.txt
awk '$6 == "-1"' analysis/Lumpy/total_duplications-truth_in_Lumpy.txt| grep "SVSIM_DUP.*500K-1Mbp"  >  analysis/Lumpy/duplications/duplications_Lumpy_false_negatives_500K-1Mbp.txt

awk '$6 == "-1"' analysis/Lumpy/total_inversions-truth_in_Lumpy.txt | grep "SVSIM_INV.*100-2500bp" >  analysis/Lumpy/inversions/inversions_Lumpy_false_negatives_100-2500bp.txt
awk '$6 == "-1"' analysis/Lumpy/total_inversions-truth_in_Lumpy.txt | grep "SVSIM_INV.*2500-3500bp" >  analysis/Lumpy/inversions/inversions_Lumpy_false_negatives_2500-3500bp.txt
awk '$6 == "-1"' analysis/Lumpy/total_inversions-truth_in_Lumpy.txt | grep "SVSIM_INV.*3500-45Kbp" >  analysis/Lumpy/inversions/inversions_Lumpy_false_negatives_3500-45Kbp.txt
awk '$6 == "-1"' analysis/Lumpy/total_inversions-truth_in_Lumpy.txt | grep "SVSIM_INV.*45K-80Kbp" >  analysis/Lumpy/inversions/inversions_Lumpy_false_negatives_45K-80Kbp.txt
awk '$6 == "-1"' analysis/Lumpy/total_inversions-truth_in_Lumpy.txt | grep "SVSIM_INV.*80K-115Kbp" >  analysis/Lumpy/inversions/inversions_Lumpy_false_negatives_80K-115Kbp.txt
awk '$6 == "-1"' analysis/Lumpy/total_inversions-truth_in_Lumpy.txt | grep "SVSIM_INV.*115K-180Kbp" >  analysis/Lumpy/inversions/inversions_Lumpy_false_negatives_115K-180Kbp.txt
awk '$6 == "-1"' analysis/Lumpy/total_inversions-truth_in_Lumpy.txt | grep "SVSIM_INV.*180K-260Kbp" >  analysis/Lumpy/inversions/inversions_Lumpy_false_negatives_180K-260Kbp.txt
awk '$6 == "-1"' analysis/Lumpy/total_inversions-truth_in_Lumpy.txt | grep "SVSIM_INV.*260K-300Kbp" >  analysis/Lumpy/inversions/inversions_Lumpy_false_negatives_260K-300Kbp.txt
awk '$6 == "-1"' analysis/Lumpy/total_inversions-truth_in_Lumpy.txt | grep "SVSIM_INV.*300K-375Kbp" >  analysis/Lumpy/inversions/inversions_Lumpy_false_negatives_300K-375Kbp.txt
awk '$6 == "-1"' analysis/Lumpy/total_inversions-truth_in_Lumpy.txt | grep "SVSIM_INV.*375K-500Kbp" >  analysis/Lumpy/inversions/inversions_Lumpy_false_negatives_375K-500Kbp.txt
awk '$6 == "-1"' analysis/Lumpy/total_inversions-truth_in_Lumpy.txt | grep "SVSIM_INV.*500K-1Mbp" >  analysis/Lumpy/inversions/inversions_Lumpy_false_negatives_500K-1Mbp.txt

awk '$6 == "-1"' analysis/Lumpy/total_deletions-truth_in_Lumpy.txt | grep "SVSIM_DEL.*100-400bp" > analysis/Lumpy/deletions/deletions_Lumpy_false_negatives_100-400bp.txt
awk '$6 == "-1"' analysis/Lumpy/total_deletions-truth_in_Lumpy.txt | grep "SVSIM_DEL.*400-600bp" > analysis/Lumpy/deletions/deletions_Lumpy_false_negatives_400-600bp.txt
awk '$6 == "-1"' analysis/Lumpy/total_deletions-truth_in_Lumpy.txt | grep "SVSIM_DEL.*600-950bp" > analysis/Lumpy/deletions/deletions_Lumpy_false_negatives_600-950bp.txt
awk '$6 == "-1"' analysis/Lumpy/total_deletions-truth_in_Lumpy.txt | grep "SVSIM_DEL.*950-1.2Kbp" > analysis/Lumpy/deletions/deletions_Lumpy_false_negatives_950-1.2Kbp.txt
awk '$6 == "-1"' analysis/Lumpy/total_deletions-truth_in_Lumpy.txt | grep "SVSIM_DEL.*1.2K-1.5Kbp" > analysis/Lumpy/deletions/deletions_Lumpy_false_negatives_1.2K-1.5Kbp.txt
awk '$6 == "-1"' analysis/Lumpy/total_deletions-truth_in_Lumpy.txt | grep "SVSIM_DEL.*1.5K-1.9Kbp" > analysis/Lumpy/deletions/deletions_Lumpy_false_negatives_1.5K-1.9Kbp.txt
awk '$6 == "-1"' analysis/Lumpy/total_deletions-truth_in_Lumpy.txt | grep "SVSIM_DEL.*1.9K-2.2Kbp" > analysis/Lumpy/deletions/deletions_Lumpy_false_negatives_1.9K-2.2Kbp.txt
awk '$6 == "-1"' analysis/Lumpy/total_deletions-truth_in_Lumpy.txt | grep "SVSIM_DEL.*2.2K-2.9Kbp" > analysis/Lumpy/deletions/deletions_Lumpy_false_negatives_2.2K-2.9Kbp.txt
awk '$6 == "-1"' analysis/Lumpy/total_deletions-truth_in_Lumpy.txt | grep "SVSIM_DEL.*2.9K-3.6Kbp" > analysis/Lumpy/deletions/deletions_Lumpy_false_negatives_2.9K-3.6Kbp.txt
awk '$6 == "-1"' analysis/Lumpy/total_deletions-truth_in_Lumpy.txt | grep "SVSIM_DEL.*3.6K-4.8Kbp" > analysis/Lumpy/deletions/deletions_Lumpy_false_negatives_3.6K-4.8Kbp.txt
awk '$6 == "-1"' analysis/Lumpy/total_deletions-truth_in_Lumpy.txt | grep "SVSIM_DEL.*4.8K-6.1Kbp" > analysis/Lumpy/deletions/deletions_Lumpy_false_negatives_4.8K-6.1Kbp.txt
awk '$6 == "-1"' analysis/Lumpy/total_deletions-truth_in_Lumpy.txt | grep "SVSIM_DEL.*6.1K-9Kbp" > analysis/Lumpy/deletions/deletions_Lumpy_false_negatives_6.1K-9Kbp.txt
awk '$6 == "-1"' analysis/Lumpy/total_deletions-truth_in_Lumpy.txt | grep "SVSIM_DEL.*9K-18.5Kbp" > analysis/Lumpy/deletions/deletions_Lumpy_false_negatives_9K-18.5Kbp.txt
awk '$6 == "-1"' analysis/Lumpy/total_deletions-truth_in_Lumpy.txt | grep "SVSIM_DEL.*18.5K-100Kbp" > analysis/Lumpy/deletions/deletions_Lumpy_false_negatives_18.5K-100Kbp.txt
awk '$6 == "-1"' analysis/Lumpy/total_deletions-truth_in_Lumpy.txt | grep "SVSIM_DEL.*100K-1Mbp" > analysis/Lumpy/deletions/deletions_Lumpy_false_negatives_100K-1Mbp.txt
