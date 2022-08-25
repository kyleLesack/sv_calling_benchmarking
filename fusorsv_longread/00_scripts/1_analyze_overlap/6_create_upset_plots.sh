# Specify the maximum number of combinations to plot using --max_combos
# To plot all combinations, don't use the --max_combos parameter. Note: This dataset has too many combinations to plot all of them.
python3 00_scripts/2_make_plots/create_upset_plots.py 00_scripts/2_make_plots/config_files/deletion_high_confidence-cnv.conf 50k deletion --max_combos 20
python3 00_scripts/2_make_plots/create_upset_plots.py 00_scripts/2_make_plots/config_files/duplication_high_confidence-cnv.conf 50k duplication --max_combos 20
python3 00_scripts/2_make_plots/create_upset_plots.py 00_scripts/2_make_plots/config_files/inversion_high_confidence-cnv.conf 50k inversion

#python3 00_scripts/2_make_plots/create_upset_plots.py 00_scripts/2_make_plots/config_files/deletion_high_confidence-cnv.conf 50k deletion # Note: Gives 127 combos!
#python3 00_scripts/2_make_plots/create_upset_plots.py 00_scripts/2_make_plots/config_files/duplication_high_confidence-cnv.conf 50k duplication
