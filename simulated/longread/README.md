# Requirements:

* SimLoRD (tested  with v1.0.4)
* The WS263 C. elegans reference genome was used. It is available in the ../shortread/0_reference/c_elegans.PRJNA13758.WS263.genomic.fa directory.
* NGMLR (tested with v0.2.7)
* SAMtools (tested with v1.9)
	* NOTE: Later versions of SAMtools may be [incompatible with NGMLR](https://github.com/philres/ngmlr/issues/86)
* pbsv and pbmm2 (tested with v2.6.2)
* Sniffles (tested with v1.0.12a)
* SVIM (tested with v2.0.0)

# Steps

Due to size limitations, the following commands describe how to simulate simulated PacBio data for a single run at 5X sequencing read depth. They can be adapted to create other genomes with larger sequencing depths.

## 1. Create simulated PacBio reads

See the [shortread documentation](../shortread/README.md) for how the mock genome was created.

The SimLoRD -sf parameter is used to designate a FASTQ that the read lengths are derived from. A PacBio run from the CeNDR project was used to derive the read lengths from, but is not included in the repo due to the large size. It may obtained from the SRA [here](https://trace.ncbi.nlm.nih.gov/Traces/?run=SRR13448208). The READLEN_RUN.fastq placeholder is used below to designate this file.

```
simlord  --read-reference ../shortread/1_create_training_data/bbtools/mock_genomes/DEL_M-DUP_M-INV_L-A/DEL_M-DUP_M-INV_L-A.fa -sf READLEN_RUN.fastq --coverage 5 --no-sam DEL_M-DUP_M-INV_L-A
```

## 2. Align reads

Align the SimLoRD reads with NGMLR. The SIMLORDPATH refers to the directory containing the SimLoRD results from the previous step. SAMtools is used to sort the results and convert to BAM format.

```
ngmlr -t 8 -r ../shortread/0_reference/c_elegans.PRJNA13758.WS263.genomic.fa -q SIMLORDPATH/DEL_M-DUP_M-INV_L-A.fastq -o 1_alignments/ngmlr/5X/DEL_M-DUP_M-INV_L-A/DEL_M-DUP_M-INV_L-A.sam
samtools view -S -b 1_alignments/ngmlr/5X/DEL_M-DUP_M-INV_L-A/DEL_M-DUP_M-INV_L-A.sam > 1_alignments/ngmlr/5X/DEL_M-DUP_M-INV_L-A/DEL_M-DUP_M-INV_L-A_sorted.bam
samtools sort -o 1_alignments/ngmlr/5X/DEL_M-DUP_M-INV_L-A/DEL_M-DUP_M-INV_L-A_sorted.bam 1_alignments/ngmlr/5X/DEL_M-DUP_M-INV_L-A/DEL_M-DUP_M-INV_L-A.bam
```

Align the SimLoRD reads with pbmm2.

pbmm2 align -j 8 ../shortread/0_reference/c_elegans.PRJNA13758.WS263.genomic.fa SIMLORDPATH/DEL_M-DUP_M-INV_L-A.fastqs DEL_M-DUP_M-INV_L-A_all_reads.bam --sort --median-filter --sample DEL_M-DUP_M-INV_L-A  --rg '@RG\tID:myid\tSM:DEL_M-DUP_M-INV_L-A'

## 3. Variant calling

Call SVs in pbsv. Uses repeat annotation file as recommended to improve sensitivity and recall. PBMM2PATH describes where the pbmm2 alignment is located

```
pbsv discover -b 0_masks/c_elegans.PRJNA13758.WS277.genomic_masked.bed PBMM2PATH/DEL_M-DUP_M-INV_L-A_all_reads.bam DEL_M-DUP_M-INV_L-A_all_reads.svsig.gz

pbsv call ../shortread/0_reference/c_elegans.PRJNA13758.WS263.genomic.fa DEL_M-DUP_M-INV_L-A_all_reads.svsig.gz DEL_M-DUP_M-INV_L-A_all_reads.vcf
```

Call SVs in Sniffles.

```
sniffles 1_alignments/ngmlr/5X/DEL_M-DUP_M-INV_L-A/DEL_M-DUP_M-INV_L-A_sorted.bam -v ./DEL_M-DUP_M-INV_L-A_sorted_sniffles.vcf
```

Call SVs in SVIM

```
svim alignment output/DEL_M-DUP_M-INV_L-A/ 1_alignments/ngmlr/5X/DEL_M-DUP_M-INV_L-A/DEL_M-DUP_M-INV_L-A_sorted.bam ../shortread/0_reference/c_elegans.PRJNA13758.WS263.genomic.fa
```

## 5. Analyses

The performance of each caller were quantified using precision, recall, F1 score and Jaccard similarity.

Scripts for quantifying the performance of pbsv, Sniffles, and SVIM are [located here](5_analyses)
