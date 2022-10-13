find . -mindepth 2 -type d -name 'DE*' | while read FILE ; do
	python3 get_sv_size_bins.py ${FILE}
done
