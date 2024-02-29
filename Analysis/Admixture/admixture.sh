#!/bin/bash
#$ -cwd
#$ -j y
#$ -pe smp 16
#$ -l h_rt=240:0:0
#$ -l h_vmem=8G


# Run ADMIXTURE on your data file for K=3 to K=5
for i in {3..5}
do
    ./admixture --cv vcf.bed.bed $i > log${i}.out
done