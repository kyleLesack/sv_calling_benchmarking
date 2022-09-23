find ./sv_calls/ -type d -name 'D*' | while read FILE ; do
	python3 get_sv_size_bins.py ${FILE}
done
