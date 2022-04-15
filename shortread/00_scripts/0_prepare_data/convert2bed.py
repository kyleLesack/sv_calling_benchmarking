import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("input_vcf", help="vcf file to convert to bed.")
parser.add_argument("sv_caller", help="variant caller used to create vcf file. Use breakdancer, cnvnator, cnmops, delly, hydra, lumpy, or fusorsv.")
parser.add_argument("--minsize", default=50, type=int, help="minimum variant size in bp")
parser.add_argument("--maxsize", default=500000, type=int, help="maximum variant size in bp")

args = parser.parse_args()

# Types of variants to look for
BREAKDANCER_SV_TYPES = ["INV","DEL","DUP"]
CNVNATOR_SV_TYPES = ["DEL","DUP"]
CNMOPS_SV_TYPES = ["DEL","DUP"]
DELLY_SV_TYPES = ["INV","DEL","DUP"]
HYDRA_SV_TYPES = ["DEL", "DUP:TANDEM", "INV"]
LUMPY_SV_TYPES = ["INV","DEL","DUP"]
FUSOR_SV_TYPES = ["INV","DEL","DUP"]


from collections import defaultdict

# Extract breakdancer variants
def parse_breakdancer(breakdancer_variants):
	callerDict = defaultdict(lambda: defaultdict(list)) # Store variants in dict
	callerDict_exceeds_maximum = defaultdict(lambda: defaultdict(list)) # Keep track of variants exceededing maximum size
	excluded_variant_types = set([]) # Keep track of excluded variant types

	for line in variants:
		if line[0] != "#":
			line_split = line.split()
			chromosome = line_split[0]
			start_coord = line_split[1]
			variant_name = line_split[2]
			variant_type = line_split[4].strip("><")
			variant_qual = int(line_split[5]) # breakdancer qual score
			filter_line = line_split[6] # Describes if variant call passed. Most calls are designated as PASSED, so I probably can ignore the rest, which are probably low quality anyways.

			info_line = line_split[7] # Get info field metadata
			info_line_split = info_line.split(";")

			if variant_type in BREAKDANCER_SV_TYPES:
				start_coord = line_split[1]
				end_coord = info_line_split[0].split("=")[1]
				variant_size = int(end_coord) - int(start_coord)
				abs_variant_size= abs(int(variant_size))
				if abs_variant_size >= args.minsize and abs_variant_size <= args.maxsize: # Only include variants of desired size
					bed_line = chromosome + "\t" + start_coord + "\t" + end_coord + "\t" + variant_name + "\tSupport:" + str(variant_qual)

					if int(end_coord) < int(start_coord): # Check fails in some cases if coords not converted to int first
						print("End coord (" + str(end_coord) + ")is less than start coord (" + str(start_coord) + ") in : " + str(args.input_vcf))
						print("Excluding line:")
						print(line)
					else:
						callerDict[filter_line][variant_type].append(bed_line)

				elif abs_variant_size > args.maxsize:
					bed_line = chromosome + "\t" + start_coord + "\t" + end_coord + "\t" + variant_name + "\tSupport:" + str(variant_qual)
					if int(end_coord) < int(start_coord): # Check fails in some cases if coords not converted to int first
						print("End coord (" + str(end_coord) + ")is less than start coord (" + str(start_coord) + ") in : " + str(args.input_vcf))
						print("Excluding line:")
						print(line)
					else:
						callerDict_exceeds_maximum[filter_line][variant_type].append(bed_line)

			else:
				if variant_type not in BREAKDANCER_SV_TYPES:
					excluded_variant_types.add(variant_type)

	if len(excluded_variant_types) > 0:
		print("breakdancer variant types excluded: " + str(excluded_variant_types))
	return (callerDict, callerDict_exceeds_maximum)


# Extract cnvnator variants
def parse_cnvnator(cnvnator_variants):
	callerDict = defaultdict(lambda: defaultdict(list)) # Store variants in dict
	callerDict_exceeds_maximum = defaultdict(lambda: defaultdict(list)) # Keep track of variants exceededing maximum size
	excluded_variant_types = set([]) # Keep track of excluded variant types

	for line in variants:
		if line[0] != "#":
			line_split = line.split()
			chromosome = line_split[0]
			start_coord = line_split[1]
			variant_name = line_split[2]
			variant_type = line_split[4].strip("><")
			filter_line = line_split[6] # Describes if variant call passed. Most calls are designated as PASSED, so I probably can ignore the rest, which are probably low quality anyways.

			info_line = line_split[7] # Get info field metadata
			info_line_split = info_line.split(";")

			if variant_type in CNVNATOR_SV_TYPES:
				start_coord = line_split[1]
				end_coord = info_line_split[0].split("=")[1]
				variant_size = int(end_coord) - int(start_coord)
				abs_variant_size= abs(int(variant_size))
				variant_qual = info_line_split[5].split("=")[1] # cnvnator e-val by t-test
				if abs_variant_size >= args.minsize and abs_variant_size <= args.maxsize: # Only include variants of desired size
					bed_line = chromosome + "\t" + start_coord + "\t" + end_coord + "\t" + variant_name + "\tSupport:" + str(variant_qual)
					callerDict[filter_line][variant_type].append(bed_line)

				elif abs_variant_size > args.maxsize:
					bed_line = chromosome + "\t" + start_coord + "\t" + end_coord + "\t" + variant_name + "\tSupport:" + str(variant_qual)
					callerDict_exceeds_maximum[filter_line][variant_type].append(bed_line)

			else:
				if variant_type not in CNVNATOR_SV_TYPES:
					excluded_variant_types.add(variant_type)

	if len(excluded_variant_types) > 0:
		print("cnvnator variant types excluded: " + str(excluded_variant_types))
	return (callerDict, callerDict_exceeds_maximum)


# Extract cnmops variants
def parse_cnmops(cnmops_variants):
	callerDict = defaultdict(lambda: defaultdict(list)) # Store variants in dict
	callerDict_exceeds_maximum = defaultdict(lambda: defaultdict(list)) # Keep track of variants exceededing maximum size
	excluded_variant_types = set([]) # Keep track of excluded variant types

	for line in variants:
		if line[0] != "#":
			line_split = line.split()
			chromosome = line_split[0]
			start_coord = line_split[1]
			variant_name = line_split[2]
			variant_type = line_split[4].strip("><")
			filter_line = line_split[6] # Describes if variant call passed. Most calls are designated as PASSED, so I probably can ignore the rest, which are probably low quality anyways.
			info_line = line_split[7] # Get info field metadata
			info_line_split = info_line.split(";")

			if variant_type in CNMOPS_SV_TYPES:
				start_coord = line_split[1]
				end_coord = info_line_split[0].split("=")[1]
				variant_size = int(end_coord) - int(start_coord)
				abs_variant_size= abs(int(variant_size))

				if abs_variant_size >= args.minsize and abs_variant_size <= args.maxsize: # Only include variants of desired size
					bed_line = chromosome + "\t" + start_coord + "\t" + end_coord + "\t" + variant_name + "\tSupport:0"
					callerDict[filter_line][variant_type].append(bed_line)

				elif abs_variant_size > args.maxsize:
					bed_line = chromosome + "\t" + start_coord + "\t" + end_coord + "\t" + variant_name + "\tSupport:0"
					callerDict_exceeds_maximum[filter_line][variant_type].append(bed_line)

			else:
				if variant_type not in CNMOPS_SV_TYPES:
					excluded_variant_types.add(variant_type)

	if len(excluded_variant_types) > 0:
		print("cnmops variant types excluded: " + str(excluded_variant_types))
	return (callerDict, callerDict_exceeds_maximum)


# Extract delly variants
def parse_delly(delly_variants):
	callerDict = defaultdict(lambda: defaultdict(list)) # Store variants in dict
	callerDict_exceeds_maximum = defaultdict(lambda: defaultdict(list)) # Keep track of variants exceededing maximum size
	excluded_variant_types = set([]) # Keep track of excluded variant types

	for line in variants:
		if line[0] != "#":
			line_split = line.split()
			chromosome = line_split[0]
			start_coord = line_split[1]
			variant_name = line_split[2]
			variant_type = line_split[4].strip("><")
			filter_line = line_split[6] # Describes if variant call passed. Most calls are designated as PASSED, so I probably can ignore the rest, which are probably low quality anyways.
			info_line = line_split[7] # Get info field metadata
			info_line_split = info_line.split(";")

			paired_end_support = 0
			split_read_support = 0

			for x in info_line_split:
				if x.split("=")[0] == "END":
					end_coord = x.split("=")[1]
					variant_size = int(end_coord) - int(start_coord)
					abs_variant_size= abs(int(variant_size))
				elif x.split("=")[0] == "PE":
					paired_end_support = int(x.split("=")[1])
				elif x.split("=")[0] == "SR":
					split_read_support = int(x.split("=")[1])
			support_value = max(paired_end_support, split_read_support)

			if variant_type in DELLY_SV_TYPES:
				start_coord = line_split[1]

				if filter_line =="PASS":

					if abs_variant_size >= args.minsize and abs_variant_size <= args.maxsize: # Only include variants of desired size
						bed_line = chromosome + "\t" + start_coord + "\t" + end_coord + "\t" + variant_name + "\tSupport:" + str(support_value)
						callerDict[filter_line][variant_type].append(bed_line)

					elif abs_variant_size > args.maxsize:
						bed_line = chromosome + "\t" + start_coord + "\t" + end_coord + "\t" + variant_name + "\tSupport:" + str(support_value)
						callerDict_exceeds_maximum[filter_line][variant_type].append(bed_line)
				else:
					if abs_variant_size >= args.minsize and abs_variant_size <= args.maxsize: # Only include variants of desired size
						bed_line = chromosome + "\t" + start_coord + "\t" + end_coord + "\t" + variant_name + "\tSupport:" + str(support_value)
						callerDict[filter_line][variant_type].append(bed_line)

					elif abs_variant_size > args.maxsize:
						bed_line = chromosome + "\t" + start_coord + "\t" + end_coord + "\t" + variant_name + "\tSupport:" + str(support_value)
						callerDict_exceeds_maximum[filter_line][variant_type].append(bed_line)

			else:
				if variant_type not in DELLY_SV_TYPES:
					excluded_variant_types.add(variant_type)

	if len(excluded_variant_types) > 0:
		print("delly variant types excluded: " + str(excluded_variant_types))
	return (callerDict, callerDict_exceeds_maximum)



# Extract hydra variants
def parse_hydra(hydra_variants):
	callerDict = defaultdict(lambda: defaultdict(list)) # Store variants in dict
	callerDict_exceeds_maximum = defaultdict(lambda: defaultdict(list)) # Keep track of variants exceededing maximum size
	excluded_variant_types = set([]) # Keep track of excluded variant types

	for line in variants:
		if line[0] != "#":
			line_split = line.split()
			chromosome = line_split[0]
			start_coord = line_split[1]
			variant_name = line_split[2]
			variant_type = line_split[4].strip("><")

			filter_line = line_split[6] # Describes if variant call passed. Most calls are designated as PASSED, so I probably can ignore the rest, which are probably low quality anyways.
			info_line = line_split[7] # Get info field metadata
			info_line_split = info_line.split(";")

			for x in info_line_split:
				if x.split("=")[0] == "END":
					end_coord = x.split("=")[1]
					variant_size = int(end_coord) - int(start_coord)
					abs_variant_size= abs(int(variant_size))
			if "SVTYPE=BND" in line:
				variant_type = "BND"
			if variant_type in HYDRA_SV_TYPES:
				if variant_type == "DUP:TANDEM":
					variant_type = "DUP"
				start_coord = line_split[1]

				if filter_line =="PASS":
					if abs_variant_size >= args.minsize and abs_variant_size <= args.maxsize: # Only include variants of desired size
						bed_line = chromosome + "\t" + start_coord + "\t" + end_coord + "\t" + variant_name
						callerDict[filter_line][variant_type].append(bed_line)

					elif abs_variant_size > args.maxsize:
						bed_line = chromosome + "\t" + start_coord + "\t" + end_coord + "\t" + variant_name
						callerDict_exceeds_maximum[filter_line][variant_type].append(bed_line)
				else:
					if abs_variant_size >= args.minsize and abs_variant_size <= args.maxsize: # Only include variants of desired size
						bed_line = chromosome + "\t" + start_coord + "\t" + end_coord + "\t" + variant_name
						callerDict[filter_line][variant_type].append(bed_line)

					elif abs_variant_size > args.maxsize:
						bed_line = chromosome + "\t" + start_coord + "\t" + end_coord + "\t" + variant_name
						callerDict_exceeds_maximum[filter_line][variant_type].append(bed_line)
			else:
				if variant_type not in HYDRA_SV_TYPES:
					excluded_variant_types.add(variant_type)

	if len(excluded_variant_types) > 0:
		print("hydra variant types excluded: " + str(excluded_variant_types))
	return (callerDict, callerDict_exceeds_maximum)


# Extract lumpy variants
def parse_lumpy(lumpy_variants):
	callerDict = defaultdict(lambda: defaultdict(list)) # Store variants in dict
	callerDict_exceeds_maximum = defaultdict(lambda: defaultdict(list)) # Keep track of variants exceededing maximum size
	excluded_variant_types = set([]) # Keep track of excluded variant types

	for line in variants:
		if line[0] != "#":
			line_split = line.split()
			chromosome = line_split[0]
			start_coord = line_split[1]
			variant_name = "LUMPY" + str(line_split[2])
			variant_type = line_split[4].strip("><")

			filter_line = "PASS" # Lumpy doesn't use the filter field, so set to pass
			info_line = line_split[7] # Get info field metadata
			info_line_split = info_line.split(";")

			for x in info_line_split:
				if x.split("=")[0] == "END":
					end_coord = x.split("=")[1]
					variant_size = int(end_coord) - int(start_coord)
					abs_variant_size= abs(int(variant_size))
				elif x.split("=")[0] == "SU":
					support_value = x.split("=")[1]

			if "SVTYPE=BND" in line:
				variant_type = "BND"
			if variant_type in LUMPY_SV_TYPES:
				start_coord = line_split[1]
				if filter_line =="PASS":

					if abs_variant_size >= args.minsize and abs_variant_size <= args.maxsize: # Only include variants of desired size
						bed_line = chromosome + "\t" + start_coord + "\t" + end_coord + "\t" + variant_name + "\tSupport:" + str(support_value)
						callerDict[filter_line][variant_type].append(bed_line)

					elif abs_variant_size > args.maxsize:
						bed_line = chromosome + "\t" + start_coord + "\t" + end_coord + "\t" + variant_name + "\tSupport:" + str(support_value)
						callerDict_exceeds_maximum[filter_line][variant_type].append(bed_line)
				else:
					if abs_variant_size >= args.minsize and abs_variant_size <= args.maxsize: # Only include variants of desired size
						bed_line = chromosome + "\t" + start_coord + "\t" + end_coord + "\t" + variant_name + "\tSupport:" + str(support_value)
						callerDict[filter_line][variant_type].append(bed_line)

					elif abs_variant_size > args.maxsize:
						bed_line = chromosome + "\t" + start_coord + "\t" + end_coord + "\t" + variant_name + "\tSupport:" + str(support_value)
						callerDict_exceeds_maximum[filter_line][variant_type].append(bed_line)

			else:
				if variant_type not in LUMPY_SV_TYPES:
					excluded_variant_types.add(variant_type)

	if len(excluded_variant_types) > 0:
		print("lumpy variant types excluded: " + str(excluded_variant_types))
	return (callerDict, callerDict_exceeds_maximum)

# Extract FusorSV variant calls
def parse_fusorsv(fusorsv_variants):
	callerDict = defaultdict(lambda: defaultdict(list)) # Store variant calls in dict
	callerDict_exceeds_maximum = defaultdict(lambda: defaultdict(list)) # Keep track of variant calls that exceeded the maximum size
	excluded_variant_types = set([])

	for line in variants:
		if line[0] != "#":
			line_split = line.split()
			chromosome = line_split[0]
			start_coord = line_split[1]
			variant_name = line_split[2]
			info_line = line_split[7]
			info_line_split = info_line.split(";")
			variant_type = info_line_split[0]
			variant_type = variant_type.split("=")[1]
			variant_size = info_line_split[1]
			variant_size = int(variant_size.split("=")[1])
			abs_variant_size= abs(int(variant_size))
			end_coord = info_line_split[2]
			end_coord = end_coord.split("=")[1]
			precision = info_line_split[4]

			if precision == "IMPRECISE":
				if variant_type in FUSOR_SV_TYPES:
					if abs_variant_size >= args.minsize and abs_variant_size <= args.maxsize:
						bed_line = chromosome + "\t" + start_coord + "\t" + end_coord + "\t" + variant_name
						callerDict["IMPRECISE"][variant_type].append(bed_line)

					elif abs_variant_size > args.maxsize:
						bed_line = chromosome + "\t" + start_coord + "\t" + end_coord + "\t" + variant_name
						callerDict_exceeds_maximum["IMPRECISE"][variant_type].append(bed_line)

				else:
					excluded_variant_types.add(variant_type)

			elif precision == "PRECISE":
				if variant_type in FUSOR_SV_TYPES:
					if abs_variant_size >= args.minsize and abs_variant_size <= args.maxsize:
						bed_line = chromosome + "\t" + start_coord + "\t" + end_coord + "\t" + variant_name
						callerDict["PRECISE"][variant_type].append(bed_line)

					elif abs_variant_size > args.maxsize:
						bed_line = chromosome + "\t" + start_coord + "\t" + end_coord + "\t" + variant_name
						callerDict_exceeds_maximum["PRECISE"][variant_type].append(bed_line)

				else:
					excluded_variant_types.add(variant_type)

	if len(excluded_variant_types) > 0:
		print("FusorSV variant types excluded: " + str(excluded_variant_types))
	return (callerDict, callerDict_exceeds_maximum)

# Write variant calls to disk
def write_bed(bedlines):
	vcf_dir = os.path.dirname(args.input_vcf) # use vcf filename for bedfile
	sample_name = os.path.basename(args.input_vcf).split(".")[0]

	for caller_filter, value in bedlines.items():
		for variant_type, bedlines in value.items():
			bed_dir = vcf_dir + "/bedfiles/" + caller_filter + "/"
			bed_dir = bed_dir.replace("0_data/1_variant_calls", "1_processed_beds/1_includes_overlap")
			output_file = bed_dir + sample_name + "_" + variant_type + ".bed"

			# Check if output directories exist.
			bed_dir = os.path.dirname(bed_dir)
			if not os.path.exists(bed_dir):
				os.makedirs(bed_dir)
			# Check if files exist. If not, write to file.
			if os.path.isfile(output_file):
				print(str(output_file) + " exists. Not overwriting.")
			else:
				with open(output_file, 'w', newline='\n') as f:
						f.writelines("%s\n" % l for l in bedlines)

# Write the variant calls that exceeded the maximum size to disk
def write_bed_exceeds_max_size(bedlines):
	vcf_dir = os.path.dirname(args.input_vcf)
	sample_name = os.path.basename(args.input_vcf).split(".")[0]

	for caller_filter, value in bedlines.items():
		for variant_type, bedlines in value.items():
			bed_dir = vcf_dir + "/bedfiles/" + caller_filter + "/"
			bed_dir = bed_dir.replace("0_data/1_variant_calls", "1_processed_beds/0_exceeded_max_size")
			output_file = bed_dir + sample_name + "_" + variant_type + ".bed"

			# Check if output directories exist.
			bed_dir = os.path.dirname(bed_dir)
			if not os.path.exists(bed_dir):
				os.makedirs(bed_dir)
			# Check if files exist. If not, write to file.
			if os.path.isfile(output_file):
				print(str(output_file) + " exists. Not overwriting.")
			else:
				with open(output_file, 'w', newline='\n') as f:
						f.writelines("%s\n" % l for l in bedlines)

# Remove filters from variant dicts. To be used if calls with FILTER column values other than PASS are to be included.
def remove_filters(bedlines):
	unfiltered_bedlines =  defaultdict(lambda: defaultdict(list))
	for caller_filter, value in bedlines.items():
		new_filter = "UNFILTERED"
		for variant_type, variant_bedlines in value.items():
			for bedline in variant_bedlines:
				unfiltered_bedlines[new_filter][variant_type].append(bedline)

	return (unfiltered_bedlines)

if args.sv_caller.lower() == "breakdancer":
	with open(args.input_vcf) as f:
		variants = f.readlines()
	breakdancer_bedlines = parse_breakdancer(variants)
	write_bed(breakdancer_bedlines[0])
	write_bed_exceeds_max_size(breakdancer_bedlines[1])

elif args.sv_caller.lower() == "cnvnator":
	with open(args.input_vcf) as f:
		variants = f.readlines()
	cnvnator_bedlines = parse_cnvnator(variants)
	write_bed(cnvnator_bedlines[0])
	write_bed_exceeds_max_size(cnvnator_bedlines[1])

elif args.sv_caller.lower() == "cnmops":
	with open(args.input_vcf) as f:
		variants = f.readlines()
	cnmops_bedlines = parse_cnmops(variants)
	write_bed(cnmops_bedlines[0])
	write_bed_exceeds_max_size(cnmops_bedlines[1])

elif args.sv_caller.lower() == "delly":
	with open(args.input_vcf) as f:
		variants = f.readlines()
	delly_bedlines = parse_delly(variants)
	write_bed(delly_bedlines[0])
	write_bed_exceeds_max_size(delly_bedlines[1])

elif args.sv_caller.lower() == "hydra":
	with open(args.input_vcf) as f:
		variants = f.readlines()
	hydra_bedlines = parse_hydra(variants)
	write_bed(hydra_bedlines[0])
	write_bed_exceeds_max_size(hydra_bedlines[1])

elif args.sv_caller.lower() == "lumpy":
	with open(args.input_vcf) as f:
		variants = f.readlines()
	lumpy_bedlines = parse_lumpy(variants)
	write_bed(lumpy_bedlines[0])
	write_bed_exceeds_max_size(lumpy_bedlines[1])

elif args.sv_caller.lower() == "fusorsv":
	with open(args.input_vcf) as f:
		variants = f.readlines()[1:] # read variants from file, skip header
	fusorsv_bedlines = parse_fusorsv(variants)
	write_bed(fusorsv_bedlines[0])
	write_bed_exceeds_max_size(fusorsv_bedlines[1])

else:
	print("Caller not supported for: " + args.sv_caller)
