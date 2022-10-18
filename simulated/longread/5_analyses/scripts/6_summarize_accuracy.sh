mkdir -p results/pbsv/sum_all_samples
mkdir -p results/sniffles/sum_all_samples
mkdir -p results/svim/sum_all_samples

# pbsv

find variant_calls/pbsv/ -name "DEL_overlap.txt" -exec grep "true positives" {} \; > results/pbsv/pbsv_del_tp.txt
find variant_calls/pbsv/ -name "DEL_overlap.txt" -exec grep "False positives" {} \; > results/pbsv/pbsv_del_fp.txt
find variant_calls/pbsv/ -name "DEL_overlap.txt" -exec grep "False negatives" {} \; > results/pbsv/pbsv_del_fn.txt
echo -n "True positives: " > results/pbsv/sum_all_samples/pbsv_deletion_statistics.txt
awk -F':' '{sum+=$2;}END{print sum;}' results/pbsv/pbsv_del_tp.txt >> results/pbsv/sum_all_samples/pbsv_deletion_statistics.txt
echo -n "False positives: " >> results/pbsv/sum_all_samples/pbsv_deletion_statistics.txt
awk -F':' '{sum+=$2;}END{print sum;}' results/pbsv/pbsv_del_fp.txt >> results/pbsv/sum_all_samples/pbsv_deletion_statistics.txt
echo -n "False negatives: " >> results/pbsv/sum_all_samples/pbsv_deletion_statistics.txt
awk -F':' '{sum+=$2;}END{print sum;}' results/pbsv/pbsv_del_fn.txt >> results/pbsv/sum_all_samples/pbsv_deletion_statistics.txt

find variant_calls/pbsv/ -name "DUP_overlap.txt" -exec grep "False positives" {} \; > results/pbsv/pbsv_dup_fp.txt
find variant_calls/pbsv/ -name "DUP_overlap.txt" -exec grep "False negatives" {} \; > results/pbsv/pbsv_dup_fn.txt
find variant_calls/pbsv/ -name "DUP_overlap.txt" -exec grep "true positives" {} \; > results/pbsv/pbsv_dup_tp.txt
echo -n "True positives: " > results/pbsv/sum_all_samples/pbsv_duplication_statistics.txt
awk -F':' '{sum+=$2;}END{print sum;}' results/pbsv/pbsv_dup_tp.txt >> results/pbsv/sum_all_samples/pbsv_duplication_statistics.txt
echo -n "False positives: " >> results/pbsv/sum_all_samples/pbsv_duplication_statistics.txt
awk -F':' '{sum+=$2;}END{print sum;}' results/pbsv/pbsv_dup_fp.txt >> results/pbsv/sum_all_samples/pbsv_duplication_statistics.txt
echo -n "False negatives: " >> results/pbsv/sum_all_samples/pbsv_duplication_statistics.txt
awk -F':' '{sum+=$2;}END{print sum;}' results/pbsv/pbsv_dup_fn.txt >> results/pbsv/sum_all_samples/pbsv_duplication_statistics.txt

find variant_calls/pbsv/ -name "INV_overlap.txt" -exec grep "False positives" {} \; > results/pbsv/pbsv_inv_fp.txt
find variant_calls/pbsv/ -name "INV_overlap.txt" -exec grep "False negatives" {} \; > results/pbsv/pbsv_inv_fn.txt
find variant_calls/pbsv/ -name "INV_overlap.txt" -exec grep "true positives" {} \; > results/pbsv/pbsv_inv_tp.txt
echo -n "True positives: " > results/pbsv/sum_all_samples/pbsv_inversion_statistics.txt
awk -F':' '{sum+=$2;}END{print sum;}' results/pbsv/pbsv_inv_tp.txt >> results/pbsv/sum_all_samples/pbsv_inversion_statistics.txt
echo -n "False positives: " >> results/pbsv/sum_all_samples/pbsv_inversion_statistics.txt
awk -F':' '{sum+=$2;}END{print sum;}' results/pbsv/pbsv_inv_fp.txt >> results/pbsv/sum_all_samples/pbsv_inversion_statistics.txt
echo -n "False negatives: " >> results/pbsv/sum_all_samples/pbsv_inversion_statistics.txt
awk -F':' '{sum+=$2;}END{print sum;}' results/pbsv/pbsv_inv_fn.txt >> results/pbsv/sum_all_samples/pbsv_inversion_statistics.txt

# sniffles
find variant_calls/sniffles/ -name "DEL_overlap.txt" -exec grep "true positives" {} \; > results/sniffles/sniffles_del_tp.txt
find variant_calls/sniffles/ -name "DEL_overlap.txt" -exec grep "False positives" {} \; > results/sniffles/sniffles_del_fp.txt
find variant_calls/sniffles/ -name "DEL_overlap.txt" -exec grep "False negatives" {} \; > results/sniffles/sniffles_del_fn.txt
echo -n "True positives: " > results/sniffles/sum_all_samples/sniffles_deletion_statistics.txt
awk -F':' '{sum+=$2;}END{print sum;}' results/sniffles/sniffles_del_tp.txt >> results/sniffles/sum_all_samples/sniffles_deletion_statistics.txt
echo -n "False positives: " >> results/sniffles/sum_all_samples/sniffles_deletion_statistics.txt
awk -F':' '{sum+=$2;}END{print sum;}' results/sniffles/sniffles_del_fp.txt >> results/sniffles/sum_all_samples/sniffles_deletion_statistics.txt
echo -n "False negatives: " >> results/sniffles/sum_all_samples/sniffles_deletion_statistics.txt
awk -F':' '{sum+=$2;}END{print sum;}' results/sniffles/sniffles_del_fn.txt >> results/sniffles/sum_all_samples/sniffles_deletion_statistics.txt

find variant_calls/sniffles/ -name "DUP_overlap.txt" -exec grep "False positives" {} \; > results/sniffles/sniffles_dup_fp.txt
find variant_calls/sniffles/ -name "DUP_overlap.txt" -exec grep "False negatives" {} \; > results/sniffles/sniffles_dup_fn.txt
find variant_calls/sniffles/ -name "DUP_overlap.txt" -exec grep "true positives" {} \; > results/sniffles/sniffles_dup_tp.txt
echo -n "True positives: " > results/sniffles/sum_all_samples/sniffles_duplication_statistics.txt
awk -F':' '{sum+=$2;}END{print sum;}' results/sniffles/sniffles_dup_tp.txt >> results/sniffles/sum_all_samples/sniffles_duplication_statistics.txt
echo -n "False positives: " >> results/sniffles/sum_all_samples/sniffles_duplication_statistics.txt
awk -F':' '{sum+=$2;}END{print sum;}' results/sniffles/sniffles_dup_fp.txt >> results/sniffles/sum_all_samples/sniffles_duplication_statistics.txt
echo -n "False negatives: " >> results/sniffles/sum_all_samples/sniffles_duplication_statistics.txt
awk -F':' '{sum+=$2;}END{print sum;}' results/sniffles/sniffles_dup_fn.txt >> results/sniffles/sum_all_samples/sniffles_duplication_statistics.txt

find variant_calls/sniffles/ -name "INV_overlap.txt" -exec grep "False positives" {} \; > results/sniffles/sniffles_inv_fp.txt
find variant_calls/sniffles/ -name "INV_overlap.txt" -exec grep "False negatives" {} \; > results/sniffles/sniffles_inv_fn.txt
find variant_calls/sniffles/ -name "INV_overlap.txt" -exec grep "true positives" {} \; > results/sniffles/sniffles_inv_tp.txt
echo -n "True positives: " > results/sniffles/sum_all_samples/sniffles_inversion_statistics.txt
awk -F':' '{sum+=$2;}END{print sum;}' results/sniffles/sniffles_inv_tp.txt >> results/sniffles/sum_all_samples/sniffles_inversion_statistics.txt
echo -n "False positives: " >> results/sniffles/sum_all_samples/sniffles_inversion_statistics.txt
awk -F':' '{sum+=$2;}END{print sum;}' results/sniffles/sniffles_inv_fp.txt >> results/sniffles/sum_all_samples/sniffles_inversion_statistics.txt
echo -n "False negatives: " >> results/sniffles/sum_all_samples/sniffles_inversion_statistics.txt
awk -F':' '{sum+=$2;}END{print sum;}' results/sniffles/sniffles_inv_fn.txt >> results/sniffles/sum_all_samples/sniffles_inversion_statistics.txt

# svim

find variant_calls/svim/ -name "DEL_overlap.txt" -exec grep "true positives" {} \; > results/svim/svim_del_tp.txt
find variant_calls/svim/ -name "DEL_overlap.txt" -exec grep "False positives" {} \; > results/svim/svim_del_fp.txt
find variant_calls/svim/ -name "DEL_overlap.txt" -exec grep "False negatives" {} \; > results/svim/svim_del_fn.txt
echo -n "True positives: " > results/svim/sum_all_samples/svim_deletion_statistics.txt
awk -F':' '{sum+=$2;}END{print sum;}' results/svim/svim_del_tp.txt >> results/svim/sum_all_samples/svim_deletion_statistics.txt
echo -n "False positives: " >> results/svim/sum_all_samples/svim_deletion_statistics.txt
awk -F':' '{sum+=$2;}END{print sum;}' results/svim/svim_del_fp.txt >> results/svim/sum_all_samples/svim_deletion_statistics.txt
echo -n "False negatives: " >> results/svim/sum_all_samples/svim_deletion_statistics.txt
awk -F':' '{sum+=$2;}END{print sum;}' results/svim/svim_del_fn.txt >> results/svim/sum_all_samples/svim_deletion_statistics.txt

find variant_calls/svim/ -name "DUP_overlap.txt" -exec grep "False positives" {} \; > results/svim/svim_dup_fp.txt
find variant_calls/svim/ -name "DUP_overlap.txt" -exec grep "False negatives" {} \; > results/svim/svim_dup_fn.txt
find variant_calls/svim/ -name "DUP_overlap.txt" -exec grep "true positives" {} \; > results/svim/svim_dup_tp.txt
echo -n "True positives: " > results/svim/sum_all_samples/svim_duplication_statistics.txt
awk -F':' '{sum+=$2;}END{print sum;}' results/svim/svim_dup_tp.txt >> results/svim/sum_all_samples/svim_duplication_statistics.txt
echo -n "False positives: " >> results/svim/sum_all_samples/svim_duplication_statistics.txt
awk -F':' '{sum+=$2;}END{print sum;}' results/svim/svim_dup_fp.txt >> results/svim/sum_all_samples/svim_duplication_statistics.txt
echo -n "False negatives: " >> results/svim/sum_all_samples/svim_duplication_statistics.txt
awk -F':' '{sum+=$2;}END{print sum;}' results/svim/svim_dup_fn.txt >> results/svim/sum_all_samples/svim_duplication_statistics.txt

find variant_calls/svim/ -name "INV_overlap.txt" -exec grep "False positives" {} \; > results/svim/svim_inv_fp.txt
find variant_calls/svim/ -name "INV_overlap.txt" -exec grep "False negatives" {} \; > results/svim/svim_inv_fn.txt
find variant_calls/svim/ -name "INV_overlap.txt" -exec grep "true positives" {} \; > results/svim/svim_inv_tp.txt
echo -n "True positives: " > results/svim/sum_all_samples/svim_inversion_statistics.txt
awk -F':' '{sum+=$2;}END{print sum;}' results/svim/svim_inv_tp.txt >> results/svim/sum_all_samples/svim_inversion_statistics.txt
echo -n "False positives: " >> results/svim/sum_all_samples/svim_inversion_statistics.txt
awk -F':' '{sum+=$2;}END{print sum;}' results/svim/svim_inv_fp.txt >> results/svim/sum_all_samples/svim_inversion_statistics.txt
echo -n "False negatives: " >> results/svim/sum_all_samples/svim_inversion_statistics.txt
awk -F':' '{sum+=$2;}END{print sum;}' results/svim/svim_inv_fn.txt >> results/svim/sum_all_samples/svim_inversion_statistics.txt

# Summarize accuracy for each BedTool

python3 scripts/get_accuracy.py scripts/config/accuracy_result_files.conf
