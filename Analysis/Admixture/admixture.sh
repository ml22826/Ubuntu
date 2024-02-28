#!/bin/bash
#$ -cwd
#$ -j y
#$ -pe smp 12
#$ -l h_rt=144:0:0
#$ -l h_vmem=6G


# Run ADMIXTURE on your data file
    ./admixture --cv vcf.bed.bed 5
