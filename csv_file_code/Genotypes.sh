!/bin/bash
#$ -cwd
#$ -j y
#$ -pe smp 16
#$ -l h_rt=24:0:0
#$ -l h_vmem=6G
#$ -m bea

module load bcftools

bcftools query -f '%POS\t%ID\t%REF\t%ALT[\t%GT]\n' ~/2024-1-29-Ubuntu/input/chr1.vcf.gz > ~/2024-1-29-Ubuntu/results/Genotypes.csv 