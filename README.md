# sv_calling_benchmarking

This repo contains the scripts and vcf file data used to benchmark structural variation (SV) calling in *Caenorhabditis elegans*.

The SVE and FusorSV tools were used for shortread calling in BreakDancer, cnMOPS, CNVnator, Delly, fusorsv, Hydra, and Lumpy.

Longread calling was performed using Assemblytics, MUM&Co, pbsv, Sniffles, and SVIM.


## Simulated Data

The pipeline for simulated shortread data is [here](simulated/shortread/).

The pipeline for simulated longread data is [here](simulated/longread/).

## Real Data

Data from the [CeNDR](https://www.elegansvariation.org/) project were used to compare the agreement between different SV callers.

The pipeline steps are explained [here](real_data/shortread/pipeline_explanation.md).

The longread with FusorSV pipeline is available [here](real_data/longread_fusorsv).

The shortread pipeline is available [here](real_data/shortread).
