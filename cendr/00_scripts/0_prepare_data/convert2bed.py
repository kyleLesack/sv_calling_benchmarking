import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("input_vcf", help="vcf file to convert to bed.")
parser.add_argument("sv_caller", help="variant caller used to create vcf file. Use pbsv, sniffles, or svim")
parser.add_argument("--minsize", default=50, type=int, help="minimum variant size in bp")
parser.add_argument("--maxsize", default=500000, type=int, help="maximum variant size in bp")
parser.add_argument("--min_qual_svim", default=5, type=int, help="minimum qual value for svim")
args = parser.parse_args()

# Types of variants to look for
PBSV_SV_TYPES = ["INV","cnv","DEL","DUP"]
sniffles_SV_TYPES = ["INV", "DEL", "DUP", "INVDUP", "INV/INVDUP", "DEL/INV"] # Note: DUP/INS causes problems, as some have END coords that start before the start. DUP/INS is rare, so I can ignore them altogether.
SVIM_SV_TYPES = ["INV", "DEL","DUP:INT", "DUP:TANDEM"]
MUMANDCO_SV_TYPES = ["inversion","contraction", "deletion", "duplication"]
ASSEMBLYTICS_SV_TYPES = ["Deletion", "Repeat_contraction", "Repeat_expansion", "Tandem_contraction", "Tandem_expansion"]
FUSOR_SV_TYPES = ["INV","DEL","DUP"]


from collections import defaultdict

# Extract variant calls from pbsv
def parse_pbsv(pbsv_variants):
	callerDict = defaultdict(lambda: defaultdict(list)) # Store variants here
	callerDict_exceeds_maximum = defaultdict(lambda: defaultdict(list)) # Keep track of variant calls that exceeded maximum size
	excluded_variant_types = set([]) # Keep track of variant call types that weren't used
	for line in variants:
		if line[0] != "#":
			line_split = line.split()
			chromosome = line_split[0]
			start_coord = line_split[1]
			variant_name = line_split[2]
			filter_line = line_split[6] # Value describes if variant call passed.

			info_line = line_split[7] # VCF info line has required matadata
			info_line_split = info_line.split(";")
			variant_type = info_line_split[0] # Get the variant type

			variant_precision = "PRECISE"
			if variant_type == "IMPRECISE": # pbsv uses different columns for imprecise variant calls
				variant_precision = "IMPRECISE"
				variant_type = info_line_split[1].split("=")[1]

				if variant_type in PBSV_SV_TYPES:
					if variant_type =="cnv": # pbsv classifies some calls as cnv, which provide different metadata in the info column
						copy_number = line_split[9]

						# Check if copy number gain or loss occured and recategorize as DEL or DUP.
						# CN 0 : hom deletion, CN 1 : het deletion, CN 2 : Normal diploid, CN 3+ : duplication
						if int(copy_number) < 2:
							variant_type = "DEL"
						elif int(copy_number) > 2:
							variant_type = "DUP"

						end_coord = info_line_split[2]
						end_coord = end_coord.split("=")[1]
						variant_size = info_line_split[3].split("=")[1]
						abs_variant_size= abs(int(variant_size))

						if variant_type != "cnv":
							if abs_variant_size >= args.minsize and abs_variant_size <= args.maxsize: # Check if variant size is in the range
								bed_line = chromosome + "\t" + start_coord + "\t" + end_coord + "\t" + variant_precision + "\t" + variant_name + "\tCN:" + copy_number
								callerDict[filter_line][variant_type].append(bed_line)
							elif abs_variant_size > args.maxsize:
								bed_line = chromosome + "\t" + start_coord + "\t" + end_coord + "\t" + variant_precision + "\t" + variant_name + "\tCN:" + copy_number
								callerDict_exceeds_maximum[filter_line][variant_type].append(bed_line)
					else:
						format_line = line_split[9]
						ad_value = format_line.split(":")[1] # Read depth per allele
						end_coord = info_line_split[2]
						end_coord = end_coord.split("=")[1]
						variant_size = info_line_split[3].split("=")[1]
						abs_variant_size= abs(int(variant_size))
						if abs_variant_size >= args.minsize and abs_variant_size <= args.maxsize:
							bed_line = chromosome + "\t" + start_coord + "\t" + end_coord + "\t" + variant_precision + "\t" + variant_name + "\tSupport:" + ad_value
							callerDict[filter_line][variant_type].append(bed_line)

						elif abs_variant_size > args.maxsize:
							bed_line = chromosome + "\t" + start_coord + "\t" + end_coord + "\t" + variant_precision + "\t" + variant_name + "\tSupport:" + ad_value
							callerDict_exceeds_maximum[filter_line][variant_type].append(bed_line)

				else:
					excluded_variant_types.add(variant_type)


			else:
				variant_type = variant_type.split("=")[1]
				if variant_type in PBSV_SV_TYPES:
					if variant_type =="cnv": # pbsv classifies some calls as cnv, which provide different metadata in the info column
						copy_number = line_split[9]

						# Check if copy number gain or loss occured and recategorize as DEL or DUP.
						# CN 0 : hom deletion, CN 1 : het deletion, CN 2 : Normal diploid, CN 3+ : duplication
						if int(copy_number) < 2:
							variant_type = "DEL"
						elif int(copy_number) > 2:
							variant_type = "DUP"

						end_coord = info_line_split[1]
						end_coord = end_coord.split("=")[1]
						variant_size = info_line_split[2].split("=")[1]
						abs_variant_size= abs(int(variant_size))

						if variant_type != "cnv":
							if abs_variant_size >= args.minsize and abs_variant_size <= args.maxsize: # Check if variant size is in the range
								bed_line = chromosome + "\t" + start_coord + "\t" + end_coord + "\t" + variant_precision + "\t" + variant_name + "\tCN:" + copy_number
								callerDict[filter_line][variant_type].append(bed_line)
							elif abs_variant_size > args.maxsize:
								bed_line = chromosome + "\t" + start_coord + "\t" + end_coord + "\t" + variant_precision + "\t" + variant_name + "\tCN:" + copy_number
								callerDict_exceeds_maximum[filter_line][variant_type].append(bed_line)
					else:
						format_line = line_split[9]
						ad_value = format_line.split(":")[1] # Read depth per allele
						end_coord = info_line_split[1]
						end_coord = end_coord.split("=")[1]
						variant_size = info_line_split[2].split("=")[1]
						abs_variant_size= abs(int(variant_size))
						if abs_variant_size >= args.minsize and abs_variant_size <= args.maxsize:
							bed_line = chromosome + "\t" + start_coord + "\t" + end_coord + "\t" + variant_precision + "\t" + variant_name + "\tSupport:" + ad_value
							callerDict[filter_line][variant_type].append(bed_line)

						elif abs_variant_size > args.maxsize:
							bed_line = chromosome + "\t" + start_coord + "\t" + end_coord + "\t" + variant_precision + "\t" + variant_name + "\tSupport:" + ad_value
							callerDict_exceeds_maximum[filter_line][variant_type].append(bed_line)

				else:
					excluded_variant_types.add(variant_type)

	print("PBSV variant types excluded: " + str(excluded_variant_types))
	return (callerDict, callerDict_exceeds_maximum)

# Extract variant calls from sniffles
def parse_sniffles(sniffles_variants):
	callerDict = defaultdict(lambda: defaultdict(list)) # Store calls in dictionary
	callerDict_exceeds_maximum = defaultdict(lambda: defaultdict(list)) # Keep track of calls exceededing maximum size
	excluded_variant_types = set([])

	for line in variants:
		if line[0] != "#":
			line_split = line.split()
			chromosome = line_split[0]
			start_coord = line_split[1]
			variant_name = line_split[2]
			filter_line = line_split[6] # Describes if variant call passed.

			info_line = line_split[7]
			info_line_split = info_line.split(";")
			variant_precision = info_line_split[0]
			zmw = info_line_split[4].split("=")[0]

			if zmw == "ZMW": # Check if zmw is in metadata. The N2 sequencing run that I chose didn't include them.
				variant_type = info_line_split[9].split("=")[1]
			else:
				variant_type = info_line_split[8].split("=")[1]

			variant_renamed = "sniffles_" + variant_type + "_" + variant_name

			support_line = line_split[9] # Line that provides read support for the reference allele and sv.
			sv_read_support = support_line.split(":")[2]

			if variant_type in sniffles_SV_TYPES:
				end_coord = info_line_split[3]
				end_coord = end_coord.split("=")[1]
				if zmw == "ZMW":
					variant_size = info_line_split[11].split("=")[1]
				else:
					variant_size = info_line_split[10].split("=")[1]

				abs_variant_size= abs(int(variant_size))

				if abs_variant_size >= args.minsize and abs_variant_size <= args.maxsize: # Filter out variant outside of desired size range
					bed_line = chromosome + "\t" + start_coord + "\t" + end_coord + "\t" + variant_precision + "\t" + variant_renamed + "\tSupport:" + support_line
					callerDict[filter_line][variant_type].append(bed_line)

				elif abs_variant_size > args.maxsize: # Keep track of variants larger than maximum size
					bed_line = chromosome + "\t" + start_coord + "\t" + end_coord + "\t" + variant_precision + "\t" + variant_renamed + "\tSupport:" + support_line
					callerDict_exceeds_maximum[filter_line][variant_type].append(bed_line)
			else:
				excluded_variant_types.add(variant_type)
				if variant_type != 'BND' and variant_type != 'DUP/INS' and variant_type != 'INS':
					print(variant_type)
					print(line)


	print("Sniffles variant types excluded: " + str(excluded_variant_types))
	return (callerDict, callerDict_exceeds_maximum)

# Extract svim variants
def parse_svim(svim_variants):
	callerDict = defaultdict(lambda: defaultdict(list)) # Store variants in dict
	callerDict_exceeds_maximum = defaultdict(lambda: defaultdict(list)) # Keep track of variants exceededing maximum size
	excluded_variant_types = set([]) # Keep track of excluded variant types

	for line in variants:
		if line[0] != "#":
			line_split = line.split()
			chromosome = line_split[0]
			start_coord = line_split[1]
			variant_name = line_split[2]
			variant_qual = int(line_split[5]) # svim qual score
			filter_line = line_split[6] # Describes if variant call passed. Most calls are designated as PASSED, so I probably can ignore the rest, which are probably low quality anyways.

			info_line = line_split[7] # Get info field metadata
			info_line_split = info_line.split(";")
			variant_type = info_line_split[0].split("=")[1]

			if variant_type in SVIM_SV_TYPES and variant_qual >= args.min_qual_svim:
				if variant_type == "INV":
					start_coord = line_split[1]
					end_coord = info_line_split[1].split("=")[1]
					variant_size = int(end_coord) - int(start_coord)
					abs_variant_size= abs(int(variant_size))
					if abs_variant_size >= args.minsize and abs_variant_size <= args.maxsize: # Only include variants of desired size
						bed_line = chromosome + "\t" + start_coord + "\t" + end_coord + "\t" + variant_name + "\tSupport:" + str(variant_qual)
						callerDict[filter_line][variant_type].append(bed_line)

					elif abs_variant_size > args.maxsize:
						bed_line = chromosome + "\t" + start_coord + "\t" + end_coord + "\t" + variant_name + "\tSupport:" + str(variant_qual)
						callerDict_exceeds_maximum[filter_line][variant_type].append(bed_line)

				elif variant_type != "DUP:INT":
					end_coord = info_line_split[1]
					end_coord = end_coord.split("=")[1]
					variant_size = info_line_split[2].split("=")[1]
					abs_variant_size= abs(int(variant_size))
					if abs_variant_size >= args.minsize and abs_variant_size <= args.maxsize: # Only include variants of desired size
						bed_line = chromosome + "\t" + start_coord + "\t" + end_coord + "\t" + variant_name + "\tSupport:" + str(variant_qual)
						callerDict[filter_line][variant_type].append(bed_line)

					elif abs_variant_size > args.maxsize:
						bed_line = chromosome + "\t" + start_coord + "\t" + end_coord + "\t" + variant_name + "\tSupport:" + str(variant_qual)
						callerDict_exceeds_maximum[filter_line][variant_type].append(bed_line)

				# DUP:INT variants columns are formatted differently
				elif variant_type == "DUP:INT":
					if info_line_split[1] =="CUTPASTE":
						end_coord = info_line_split[2]
						end_coord = end_coord.split("=")[1]
						variant_size = info_line_split[3].split("=")[1]
						abs_variant_size= abs(int(variant_size))
						if abs_variant_size >= args.minsize and abs_variant_size <= args.maxsize:
							bed_line = chromosome + "\t" + start_coord + "\t" + end_coord + "\t" + variant_name + "\tSupport:" + str(variant_qual)
							callerDict[filter_line][variant_type].append(bed_line)

						elif abs_variant_size > args.maxsize:
							bed_line = chromosome + "\t" + start_coord + "\t" + end_coord + "\t" + variant_name + "\tSupport:" + str(variant_qual)
							callerDict_exceeds_maximum[filter_line][variant_type].append(bed_line)

					else:
						end_coord = info_line_split[1]
						end_coord = end_coord.split("=")[1]
						variant_size = info_line_split[2].split("=")[1]
						abs_variant_size= abs(int(variant_size))
						if abs_variant_size >= args.minsize and abs_variant_size <= args.maxsize:
							bed_line = chromosome + "\t" + start_coord + "\t" + end_coord + "\t" + variant_name + "\tSupport:" + str(variant_qual)
							callerDict[filter_line][variant_type].append(bed_line)

						elif  abs_variant_size > args.maxsize:
							bed_line = chromosome + "\t" + start_coord + "\t" + end_coord + "\t" + variant_name + "\tSupport:" + str(variant_qual)
							callerDict_exceeds_maximum[filter_line][variant_type].append(bed_line)
				else:
					print(variant_type)

			else:
				if variant_type not in SVIM_SV_TYPES:
					excluded_variant_types.add(variant_type)

	print("Svim variant types excluded: " + str(excluded_variant_types))
	return (callerDict, callerDict_exceeds_maximum)

# Extract MUM&Co variants
def parse_mumandco(mumandco_variants):
	callerDict = defaultdict(list)
	callerDict_exceeds_maximum = defaultdict(list)
	excluded_variant_types = set([])
	variant_count = 1 # Variant call index used to assign a name to

	for line in variants:
		line_split = line.split()
		chromosome = line_split[0]
		start_coord = line_split[2]
		end_coord = line_split[3]
		variant_size = int(line_split[4])
		abs_variant_size= abs(int(variant_size))
		variant_type = line_split[5]

		if variant_type in MUMANDCO_SV_TYPES:
			if abs_variant_size >= args.minsize and abs_variant_size <= args.maxsize:
				variant_name = variant_type.upper() + "_" + str(variant_count) # Create a name for variant
				bed_line = chromosome + "\t" + start_coord + "\t" + end_coord + "\t" + variant_name
				callerDict[variant_type].append(bed_line)
				variant_count += 1

			elif abs_variant_size > args.maxsize:
				variant_name = variant_type.upper() + "_" + str(variant_count)
				bed_line = chromosome + "\t" + start_coord + "\t" + end_coord + "\t" + variant_name # Create a name for variant
				callerDict_exceeds_maximum[variant_type].append(bed_line)
				variant_count += 1

		else:
			excluded_variant_types.add(variant_type)

	print("MUM&Co variant types excluded: " + str(excluded_variant_types))
	return (callerDict, callerDict_exceeds_maximum)

# Extract ASsemblytics variants
def parse_assemblytics(assemblytics_variants):
	callerDict = defaultdict(list) # Store variant calls in dict
	callerDict_exceeds_maximum = defaultdict(list) # Keep track of variants exceeding maximum size
	excluded_variant_types = set([])

	for line in variants:
		line_split = line.split()
		chromosome = line_split[0]
		start_coord = line_split[1]
		end_coord = line_split[2]
		variant_name = line_split[3]
		variant_size = int(line_split[4])
		abs_variant_size= abs(int(variant_size))
		variant_type = line_split[6]

		if variant_type in ASSEMBLYTICS_SV_TYPES: # Check if variant size is in desired range
			if abs_variant_size >= args.minsize and abs_variant_size <= args.maxsize:
				bed_line = chromosome + "\t" + start_coord + "\t" + end_coord + "\t" + variant_name
				callerDict[variant_type].append(bed_line)

			elif abs_variant_size > args.maxsize:
				bed_line = chromosome + "\t" + start_coord + "\t" + end_coord + "\t" + variant_name
				callerDict_exceeds_maximum[variant_type].append(bed_line)

		else:
			excluded_variant_types.add(variant_type)

	print("Assemblytics variant types excluded: " + str(excluded_variant_types))
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

			else: # Right now my dataset only has imprecise calls (need to add an assembler to refine breakpoints of other callers?). I included this to flag any variants that are precise.
				print("Non-imprecise call")
				print(line)
				input("press any key")

	print("FusorSV variant types excluded: " + str(excluded_variant_types))
	return (callerDict, callerDict_exceeds_maximum)

# Write variant calls to disk
def write_bed(bedlines):
	vcf_dir = os.path.dirname(args.input_vcf) # use vcf filename for bedfile
	sample_name = os.path.basename(args.input_vcf).split(".")[0]

	if args.sv_caller.lower() == "mumandco" or args.sv_caller.lower() == "assemblytics": # Write MUM&Co or ASsemblytics variants to disk
		for variant_type, bedlines in bedlines.items():
			bed_dir = vcf_dir + "/bedfiles/"
			bed_dir = bed_dir.replace("0_data/1_variant_calls", "1_processed_beds/1_includes_overlap")
			variant_type = variant_type.replace("/","_") # Sniffles contains DUP/INS variants. Replace the /
			variant_type = variant_type.replace(":","_") # Svim contains DUP:TANDEM and DUP:INT variants. Replace the :

			# Add an "s" to DEL, DUP, and INV variant types. Don't add an "s" to COMBINED calls
			if "COMBINED" in variant_type:
				output_file = bed_dir + sample_name + "_" + variant_type + ".bed"
			else:
				output_file = bed_dir + sample_name + "_" + variant_type + "s.bed"

			bed_dir = os.path.dirname(bed_dir) # Create directory for bedfiles if it doesn't exist
			if not os.path.exists(bed_dir):
				os.makedirs(bed_dir)

			# Check if files exist. If not, write to file.
			if os.path.isfile(output_file):
				print(str(output_file) + " exists. Not overwriting.")
			else:
				with open(output_file, 'w', newline='\n') as f:
						f.writelines("%s\n" % l for l in bedlines)

	else: # Write other caller variants to disk
		for caller_filter, value in bedlines.items():
			for variant_type, bedlines in value.items():
				if args.sv_caller.lower() == "svim":
					bed_dir = vcf_dir + "/bedfiles/QUAL_" + str(args.min_qual_svim) + "/" + caller_filter + "/"
				else:
					bed_dir = vcf_dir + "/bedfiles/" + caller_filter + "/"
				bed_dir = bed_dir.replace("0_data/1_variant_calls", "1_processed_beds/1_includes_overlap")
				variant_type = variant_type.replace("/","_") # Sniffles contains DUP/INS variants. Replace the /
				variant_type = variant_type.replace(":","_") # Svim contains DUP:TANDEM and DUP:INT variants. Replace the :
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

	if args.sv_caller.lower() == "mumandco" or args.sv_caller.lower() == "assemblytics": # Write MUM&Co or ASsemblytics variants to disk
		for variant_type, bedlines in bedlines.items():
			bed_dir = vcf_dir + "/bedfiles/"
			bed_dir = bed_dir.replace("0_data/1_variant_calls", "1_processed_beds/0_exceeded_max_size")
			variant_type = variant_type.replace("/","_") # Sniffles contains DUP/INS variants. Replace the /
			variant_type = variant_type.replace(":","_") # Svim contains DUP:TANDEM and DUP:INT variants. Replace the :

			# Add an "s" to DEL, DUP, and INV variant types. Don't add an "s" to COMBINED calls
			if "COMBINED" in variant_type:
				output_file = bed_dir + sample_name + "_" + variant_type + ".bed"
			else:
				output_file = bed_dir + sample_name + "_" + variant_type + "s.bed"
			bed_dir = os.path.dirname(bed_dir)
			if not os.path.exists(bed_dir):
				os.makedirs(bed_dir)
			# Check if files exist. If not, write to file.
			if os.path.isfile(output_file):
				print(str(output_file) + " exists. Not overwriting.")
			else:
				with open(output_file, 'w', newline='\n') as f:
						f.writelines("%s\n" % l for l in bedlines)

	else: # Write other caller variants to disk
		for caller_filter, value in bedlines.items():
			for variant_type, bedlines in value.items():
				if args.sv_caller.lower() == "svim":
					bed_dir = vcf_dir + "/bedfiles/QUAL_" + str(args.min_qual_svim) + "/" + caller_filter + "/"
				else:
					bed_dir = vcf_dir + "/bedfiles/" + caller_filter + "/"
				bed_dir = bed_dir.replace("0_data/1_variant_calls", "1_processed_beds/0_exceeded_max_size")
				variant_type = variant_type.replace("/","_") # Sniffles contains DUP/INS variants. Replace the /
				variant_type = variant_type.replace(":","_") # Svim contains DUP:TANDEM and DUP:INT variants. Replace the :
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

# Combine SVIM duplications into single variant type
def recategorize_svim(bedlines):
	recategorized_bedlines = defaultdict(lambda: defaultdict(list))
	for caller_filter, value in bedlines.items():
		for variant_type, variant_bedlines in value.items():
			if variant_type =="DUP:INT" or variant_type == "DUP:TANDEM":
				variant_type = "DUP_COMBINED"
				for bedline in variant_bedlines:
					recategorized_bedlines[caller_filter][variant_type].append(bedline)
	return (recategorized_bedlines)

# Combine complex variants into DEL, DUP, and INV COMBINED variant types
def recategorize_sniffles(bedlines):
	recategorized_bedlines = defaultdict(lambda: defaultdict(list))

	for caller_filter, value in bedlines.items():
		for variant_type, variant_bedlines in value.items():
			if variant_type =="DUP" or variant_type =="INVDUP" or variant_type == "INV/INVDUP" or variant_type == "DUP/INS":
				new_variant_type = "DUP_COMBINED"
				for bedline in variant_bedlines:
					recategorized_bedlines[caller_filter][new_variant_type].append(bedline)

			if variant_type =="INV" or variant_type =="INVDUP" or variant_type == "INV/INVDUP" or variant_type == "DEL/INV":
				new_variant_type = "INV_COMBINED"
				for bedline in variant_bedlines:
					recategorized_bedlines[caller_filter][new_variant_type].append(bedline)

			if variant_type =="DEL" or variant_type =="DEL/INV" :
				new_variant_type = "DEL_COMBINED"
				for bedline in variant_bedlines:
					recategorized_bedlines[caller_filter][new_variant_type].append(bedline)

	return (recategorized_bedlines)

# Combine Assemblytics deletions and duplications into single types
def recategorize_assemblytics_mumandco(bedlines):
	recategorized_bedlines = defaultdict(list)
	for variant_type, variant_calls in bedlines.items():
		if variant_type == "Deletion" or variant_type == "deletion" or variant_type == "Repeat_contraction" or variant_type == "Tandem_contraction" or variant_type == "contraction":
			recategorized_variant_type = "DEL_COMBINED"
			for line in variant_calls:
				recategorized_bedlines[recategorized_variant_type].append(line)
		elif variant_type == "Repeat_expansion" or variant_type == "Tandem_expansion":
			recategorized_variant_type = "DUP_COMBINED"
			for line in variant_calls:
				recategorized_bedlines[recategorized_variant_type].append(line)

	return (recategorized_bedlines)

# Remove filters from variant dicts. To be used if calls with FILTER column values other than PASS are to be included.
def remove_filters(bedlines):
	unfiltered_bedlines =  defaultdict(lambda: defaultdict(list))

	for caller_filter, value in bedlines.items():
		new_filter = "UNFILTERED"
		for variant_type, variant_bedlines in value.items():
			for bedline in variant_bedlines:
				unfiltered_bedlines[new_filter][variant_type].append(bedline)

	return (unfiltered_bedlines)


# Parse the sv call files for a caller. The unfiltered code needs to be added, as shown below.
# unfiltered_sniffles = remove_filters(sniffles_bedlines)
# unfiltered_recategorized_sniffles = remove_filters(recategorized_sniffles)
# write_bed(unfiltered_sniffles)
# if len(unfiltered_recategorized_sniffles) > 0:
# write_bed(unfiltered_recategorized_sniffles)

if args.sv_caller.lower() == "pbsv":
	with open(args.input_vcf) as f:
		variants = f.readlines()
	pbsv_bedlines = parse_pbsv(variants)
	write_bed(pbsv_bedlines[0])
	write_bed_exceeds_max_size(pbsv_bedlines[1])

elif args.sv_caller.lower() == "sniffles":
	with open(args.input_vcf) as f:
		variants = f.readlines()
	sniffles_bedlines = parse_sniffles(variants)
	recategorized_sniffles = recategorize_sniffles(sniffles_bedlines[0])

	write_bed(sniffles_bedlines[0])
	write_bed_exceeds_max_size(sniffles_bedlines[1])

	if len(recategorized_sniffles) > 0:
		write_bed(recategorized_sniffles)

elif args.sv_caller.lower() == "svim":
	with open(args.input_vcf) as f:
		variants = f.readlines()
	svim_bedlines = parse_svim(variants)
	recategorized_svim = recategorize_svim(svim_bedlines[0])
	write_bed(svim_bedlines[0])
	write_bed_exceeds_max_size(svim_bedlines[1])
	if len(recategorized_svim) > 0:
		write_bed(recategorized_svim)

elif args.sv_caller.lower() == "mumandco":
	with open(args.input_vcf) as f:
		variants = f.readlines()[1:] # read variants from file, skip header
	mumandco_bedlines = parse_mumandco(variants)
	recategorized_mumandco = recategorize_assemblytics_mumandco(mumandco_bedlines[0])
	write_bed(mumandco_bedlines[0])
	write_bed_exceeds_max_size(mumandco_bedlines[1])
	write_bed(recategorized_mumandco)

elif args.sv_caller.lower() == "assemblytics":
	with open(args.input_vcf) as f:
		variants = f.readlines()[1:] # read variants from file, skip header
	assemblytics_bedlines = parse_assemblytics(variants)
	recategorized_assemblytics = recategorize_assemblytics_mumandco(assemblytics_bedlines[0])
	write_bed(assemblytics_bedlines[0])
	write_bed_exceeds_max_size(assemblytics_bedlines[1])
	write_bed(recategorized_assemblytics)

elif args.sv_caller.lower() == "fusorsv":
	with open(args.input_vcf) as f:
		variants = f.readlines()[1:] # read variants from file, skip header
	fusorsv_bedlines = parse_fusorsv(variants)
	write_bed(fusorsv_bedlines[0])
	write_bed_exceeds_max_size(fusorsv_bedlines[1])

else:
	print("Caller not supported for: " + args.sv_caller)
