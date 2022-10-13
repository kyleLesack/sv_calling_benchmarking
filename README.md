# sv_calling_benchmarking

This repo contains the scripts and vcf file data used to benchmark structural variation (SV) calling in *Caenorhabditis elegans*. The data and pipelines for shortread and longread caller benchmarking are available in the [shortread](shortread/) and [longread](longread/) directories respectively.  The SVE and FusorSV tools were used for shortread calling in BreakDancer, cnMOPS, CNVnator, Delly, fusorsv, Hydra, and Lumpy. 

Longread calling was performed using Assemblytics, MUM&Co, pbsv, Sniffles, and SVIM.

[The pipeline steps are explained here.](shortread/pipeline_explanation.md)

## Real Data

Data from the [CeNDR](https://www.elegansvariation.org/) project were used to compare the agreement between different SV callers.

The longread with FusorSV pipeline is available [here](real_data/longread_fusorsv).

The shorted pipeline is available [here](real_data/shortread).


