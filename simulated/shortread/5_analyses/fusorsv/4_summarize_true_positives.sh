mkdir -p intermediate_results/duplications
mkdir -p intermediate_results/inversions
mkdir -p intermediate_results/deletions

grep "SVSIM_DUP.*1-50bp" intermediate_results/total_duplications-fusor_in_truth.txt  > intermediate_results/duplications/duplications_fusor_true_positives_1-50bp.txt
grep "SVSIM_DUP.*50-1Kbp" intermediate_results/total_duplications-fusor_in_truth.txt  > intermediate_results/duplications/duplications_fusor_true_positives_50-1Kbp.txt
grep "SVSIM_DUP.*1K-10Kbp" intermediate_results/total_duplications-fusor_in_truth.txt  > intermediate_results/duplications/duplications_fusor_true_positives_1K-10Kbp.txt
grep "SVSIM_DUP.*10K-50Kbp" intermediate_results/total_duplications-fusor_in_truth.txt  > intermediate_results/duplications/duplications_fusor_true_positives_10K-50Kbp.txt
grep "SVSIM_DUP.*50K-100Kbp" intermediate_results/total_duplications-fusor_in_truth.txt  > intermediate_results/duplications/duplications_fusor_true_positives_50K-100Kbp.txt
grep "SVSIM_DUP.*100K-250Kbp" intermediate_results/total_duplications-fusor_in_truth.txt  > intermediate_results/duplications/duplications_fusor_true_positives_100K-250Kbp.txt
grep "SVSIM_DUP.*250K-500Kbp" intermediate_results/total_duplications-fusor_in_truth.txt  > intermediate_results/duplications/duplications_fusor_true_positives_250K-500Kbp.txt
grep "SVSIM_DUP.*500K-1Mbp" intermediate_results/total_duplications-fusor_in_truth.txt  > intermediate_results/duplications/duplications_fusor_true_positives_500K-1Mbp.txt

grep "SVSIM_INV.*1-50bp" intermediate_results/total_inversions-fusor_in_truth.txt  > intermediate_results/inversions/inversions_fusor_true_positives_1-50bp.txt
grep "SVSIM_INV.*50-2500bp" intermediate_results/total_inversions-fusor_in_truth.txt  > intermediate_results/inversions/inversions_fusor_true_positives_50-2500bp.txt
grep "SVSIM_INV.*2500-3500bp" intermediate_results/total_inversions-fusor_in_truth.txt  > intermediate_results/inversions/inversions_fusor_true_positives_2500-3500bp.txt
grep "SVSIM_INV.*3500-45Kbp" intermediate_results/total_inversions-fusor_in_truth.txt  > intermediate_results/inversions/inversions_fusor_true_positives_3500-45Kbp.txt
grep "SVSIM_INV.*45K-80Kbp" intermediate_results/total_inversions-fusor_in_truth.txt  > intermediate_results/inversions/inversions_fusor_true_positives_45K-80Kbp.txt
grep "SVSIM_INV.*80K-115Kbp" intermediate_results/total_inversions-fusor_in_truth.txt  > intermediate_results/inversions/inversions_fusor_true_positives_80K-115Kbp.txt
grep "SVSIM_INV.*115K-180Kbp" intermediate_results/total_inversions-fusor_in_truth.txt  > intermediate_results/inversions/inversions_fusor_true_positives_115K-180Kbp.txt
grep "SVSIM_INV.*180K-260Kbp" intermediate_results/total_inversions-fusor_in_truth.txt  > intermediate_results/inversions/inversions_fusor_true_positives_180K-260Kbp.txt
grep "SVSIM_INV.*260K-300Kbp" intermediate_results/total_inversions-fusor_in_truth.txt  > intermediate_results/inversions/inversions_fusor_true_positives_260K-300Kbp.txt
grep "SVSIM_INV.*300K-375Kbp" intermediate_results/total_inversions-fusor_in_truth.txt  > intermediate_results/inversions/inversions_fusor_true_positives_300K-375Kbp.txt
grep "SVSIM_INV.*375K-500Kbp" intermediate_results/total_inversions-fusor_in_truth.txt  > intermediate_results/inversions/inversions_fusor_true_positives_375K-500Kbp.txt
grep "SVSIM_INV.*500K-1Mbp" intermediate_results/total_inversions-fusor_in_truth.txt  > intermediate_results/inversions/inversions_fusor_true_positives_500K-1Mbp.txt

grep "SVSIM_DEL.*1-50bp" intermediate_results/total_deletions-fusor_in_truth.txt  > intermediate_results/deletions/deletions_fusor_true_positives_1-50bp.txt
grep "SVSIM_DEL.*50-100bp" intermediate_results/total_deletions-fusor_in_truth.txt  > intermediate_results/deletions/deletions_fusor_true_positives_50-100bp.txt
grep "SVSIM_DEL.*100-400bp" intermediate_results/total_deletions-fusor_in_truth.txt  > intermediate_results/deletions/deletions_fusor_true_positives_100-400bp.txt
grep "SVSIM_DEL.*400-600bp" intermediate_results/total_deletions-fusor_in_truth.txt  > intermediate_results/deletions/deletions_fusor_true_positives_400-600bp.txt
grep "SVSIM_DEL.*600-950bp" intermediate_results/total_deletions-fusor_in_truth.txt  > intermediate_results/deletions/deletions_fusor_true_positives_600-950bp.txt
grep "SVSIM_DEL.*950-1.2Kbp" intermediate_results/total_deletions-fusor_in_truth.txt  > intermediate_results/deletions/deletions_fusor_true_positives_950-1.2Kbp.txt
grep "SVSIM_DEL.*1.2K-1.5Kbp" intermediate_results/total_deletions-fusor_in_truth.txt  > intermediate_results/deletions/deletions_fusor_true_positives_1.2K-1.5Kbp.txt
grep "SVSIM_DEL.*1.5K-1.9Kbp" intermediate_results/total_deletions-fusor_in_truth.txt  > intermediate_results/deletions/deletions_fusor_true_positives_1.5K-1.9Kbp.txt
grep "SVSIM_DEL.*1.9K-2.2Kbp" intermediate_results/total_deletions-fusor_in_truth.txt  > intermediate_results/deletions/deletions_fusor_true_positives_1.9K-2.2Kbp.txt
grep "SVSIM_DEL.*2.2K-2.9Kbp" intermediate_results/total_deletions-fusor_in_truth.txt  > intermediate_results/deletions/deletions_fusor_true_positives_2.2K-2.9Kbp.txt
grep "SVSIM_DEL.*2.9K-3.6Kbp" intermediate_results/total_deletions-fusor_in_truth.txt  > intermediate_results/deletions/deletions_fusor_true_positives_2.9K-3.6Kbp.txt
grep "SVSIM_DEL.*3.6K-4.8Kbp" intermediate_results/total_deletions-fusor_in_truth.txt  > intermediate_results/deletions/deletions_fusor_true_positives_3.6K-4.8Kbp.txt
grep "SVSIM_DEL.*4.8K-6.1Kbp" intermediate_results/total_deletions-fusor_in_truth.txt  > intermediate_results/deletions/deletions_fusor_true_positives_4.8K-6.1Kbp.txt
grep "SVSIM_DEL.*6.1K-9Kbp" intermediate_results/total_deletions-fusor_in_truth.txt  > intermediate_results/deletions/deletions_fusor_true_positives_6.1K-9Kbp.txt
grep "SVSIM_DEL.*9K-18.5Kbp" intermediate_results/total_deletions-fusor_in_truth.txt  > intermediate_results/deletions/deletions_fusor_true_positives_9K-18.5Kbp.txt
grep "SVSIM_DEL.*18.5K-100Kbp" intermediate_results/total_deletions-fusor_in_truth.txt  > intermediate_results/deletions/deletions_fusor_true_positives_18.5K-100Kbp.txt
grep "SVSIM_DEL.*100K-1Mbp" intermediate_results/total_deletions-fusor_in_truth.txt  > intermediate_results/deletions/deletions_fusor_true_positives_100K-1Mbp.txt
