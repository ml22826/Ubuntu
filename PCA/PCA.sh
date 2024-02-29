#create BED file:
plink --vcf chr1.vcf.gz --make-bed --out PCA

#calculate PC scores for each population:
plink --bfile PCA --pca 3 --out PCA
