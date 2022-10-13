# Requirements:

* Python 3 (tested with v3.9.12)
	* [Numpy](https://numpy.org/) (tested with v1.23.1) used
* [SVsim](https://github.com/GregoryFaust/SVsim) (tested using v0.1.1)
* [BBTools](sourceforge.net/projects/bbmap/) randomreads.sh (tested with v38.79)
* [bedtools](https://bedtools.readthedocs.io/en/latest/index.html) (tested with v2.30.0)
* [Structural Variation Engine](https://github.com/timothyjamesbecker/SVE) and [FusorSV](https://github.com/timothyjamesbecker/FusorSV)
	* Available as Docker images.
		* For HPC clusters running Singularity, the images may be converted to Singularity images using [docker2singularity](https://github.com/singularityhub/docker2singularity)
			* The Singularity commands below were tested with Singularity v2.6 and v3.5.3.
			* Note: The Singularity bind paths may need to be changed to absolute paths to work properly. Relative paths were used to reflect their locations in this repo.
* The WS263 C. elegans reference genome was used. It is available in the 0_reference/c_elegans.PRJNA13758.WS263.genomic.fa directory.

# Steps

Due to size limitations, the following commands describe how to create a single mock genome at 5X sequencing read depth. They can be adapted to create other genomes with larger sequencing depths.

## 1. Create mock genome and simulated Illumina reads

Create a mock genome in SVsim containing a simulated deletion, duplication, and inversion (specified in the DEL_M-DUP_M-INV_L-A.txt profile file):

```
SVsim -i 1_create_training_data/svsim/profiles/DEL_M-DUP_M-INV_L-A.txt -r 0_reference/c_elegans.PRJNA13758.WS263.genomic.fa -o 1_create_training_data/svsim/mock_genomes/DEL_M-DUP_M-INV_L-A/ -W -n 1 -d -s 8601
```

Create the truth vcf for the mock genome:

```
cd ./1_create_training_data/svsim/make_S0_vcf/
python3 svsim2vcf.py ../mock_genomes/DEL_M-DUP_M-INV_L-A/DEL_M-DUP_M-INV_L-A.bedpe DEL_M-DUP_M-INV_L-A  > ../mock_genomes/DEL_M-DUP_M-INV_L-A/DEL_M-DUP_M-INV_L-A_S0.vcf
```
Create simulated Illumina reads with the BBTools randomreads.sh command:

```
cd 1_create_training_data/bbtools/mock_genomes/DEL_M-DUP_M-INV_L-A

randomreads.sh ref=../../../svsim/mock_genomes/DEL_M-DUP_M-INV_L-A/DEL_M-DUP_M-INV_L-A.fa out1=DEL_M-DUP_M-INV_L-A_1.fq out2=DEL_M-DUP_M-INV_L-A_2.fq length=100 coverage=5 paired=t illuminanames=t addslash=t mininsert=275 maxinsert=325 gaussian=t adderrors=t
```


## 2. Align reads

Align reads with SVE in Singularity.

```
singularity exec -B 0_reference:/reference,1_create_training_data/bbtools/mock_genomes/DEL_M-DUP_M-INV_L-A:/input,/2_align_reads/DEL_M-DUP_M-INV_L-A/:/output timothyjamesbecker_sve-2018-06-20-e4eea1027b9d.simg \
/software/SVE/scripts/prepare_bam.py \
-r /reference/c_elegans.PRJNA13758.WS263.genomic.fa \
-f /input/DEL_M-DUP_M-INV_L-A_1.fq,/input/DEL_M-DUP_M-INV_L-A_2.fq \
-o /output/ \
-P 8 -T 1 -M 8 -a speed_seq
```

## 3. Call SVs

Call SVs with SVE in Singularity.

```
singularity exec -B 0_reference:/reference,2_align_reads/DEL_M-DUP_M-INV_L-A:/input,3_call_svs/sv_calls:/output timothyjamesbecker_sve-2018-06-20-e4eea1027b9d.simg \
/software/SVE/scripts/variant_processor.py \
-r /reference/c_elegans.PRJNA13758.WS263.genomic.fa \
-b /input/DEL_M-DUP_M-INV_L-A.bam \
-o /output/ \
-s breakdancer,cnmops,cnvnator,delly,hydra,lumpy \
-D 5 -L 100
```

## 4. Call FusorSV

Call SVs using FusorSV in Singularity. The FusorSV model used is provided in the 4_fusor_sv/models directory. A new model may be created using mock genomes created as demonstrated here by omitting the -f parameter below.

```
singularity exec -B 0_reference:/reference,3_call_svs/sv_calls/:/input,/4_fusor_sv/results/:/output,4_fusor_sv/models/:/model timothyjamesbecker_fusorsv-2018-06-20-4d90a14d25e5.simg \
FusorSV.py \
-c I,II,III,IV,V,X,MtDNA \
-r /reference/c_elegans.PRJNA13758.WS263.genomic.fa \
-i /input/ \
-f /model/c_elegans.PRJNA13758.WS263.genomic.input-1835552633213864425.pickle.gz \
-o /output/ \
-p 8
```

## 5. Analyses

The performance of each caller and FusorSV were quantified using precision, recall, F1 score and Jaccard simularity.

Scripts for quantifying the performance of the individual callers in the SVE pipeline (BreakDancer, cnMOPS, CNVnator, Delly, Hydra, and Lumpy) are [located here](5_analyses/sve_callers)

Scripts for quantifying the performance of FusorSV are [located here](5_analyses/fusorsv)
