mkdir -p intermediate_results
find ./sv_calls/ -name "del_fusor_in_truth.txt" -exec cat {} \; > intermediate_results/total_deletions-fusor_in_truth.txt
find ./sv_calls/ -name "del_truth_in_fusor.txt" -exec cat {} \; > intermediate_results/total_deletions-truth_in_fusor.txt

find ./sv_calls/ -name "dup_fusor_in_truth.txt" -exec cat {} \; > intermediate_results/total_duplications-fusor_in_truth.txt
find ./sv_calls/ -name "dup_truth_in_fusor.txt" -exec cat {} \; > intermediate_results/total_duplications-truth_in_fusor.txt

find ./sv_calls/ -name "inv_fusor_in_truth.txt" -exec cat {} \; > intermediate_results/total_inversions-fusor_in_truth.txt
find ./sv_calls/ -name "inv_truth_in_fusor.txt" -exec cat {} \; > intermediate_results/total_inversions-truth_in_fusor.txt
