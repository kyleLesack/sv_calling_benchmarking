# sv_calling_benchmarking

This repo contains the scripts and vcf file data used to benchmark structural variation calling in *Caenorhabditis elegans*. The data and pipelines for shortread and longread caller benchmarking are available in the [shortread](shortread/) and [longread](longread/) directories respectively.  The SVE and FusorSV tools were used for shortread calling in BreakDancer, cnMOPS, CNVnator, Delly, fusorsv, Hydra, and Lumpy. 

Longread calling was performed using Assemblytics, MUM&Co, pbsv, Sniffles, and SVIM.

To compare calling variants using a shortread data with longread data, the longread pipeline with FusorSV is available [here](fusorsv_longread).

## Real Data

To compare the results from [CeNDR](https://www.elegansvariation.org/) data, the longread with FusorSV pipeline is available [here](real_data/longread_fusorsv).

[The pipeline steps are explained here.](shortread/pipeline_explanation.md)
