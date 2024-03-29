#Create a plink file
plink --vcf chr1.vcf.gz --make-bed --out chr1

#extract ids for each induvidual population
#!/bin/bash

populations=("ACB" "ASW" "BEB" "CDX" "CEU" "CHB" "CHS" "CLM" "ESN" "FIN" "GBR" "GIH" "GWD" "IBS" "ITU" "JPT" "KHV" "LWK" "MSL" "MXL" "PEL" "PJL" "PUR" "SIB" "STU" "TSI" "YRI")

for pop in "${populations[@]}"; do
    awk -v pop="$pop" 'BEGIN{OFS="\t"} $2 == pop {print $1, $1}' sample_pop.tsv > "${pop}_keep.txt"
done

#calculate allele frequency
#!/bin/bash

populations=("ACB" "ASW" "BEB" "CDX" "CEU" "CHB" "CHS" "CLM" "ESN" "FIN" "GBR" "GIH" "GWD" "IBS" "ITU" "JPT" "KHV" "LWK" "MSL" "MXL" "PEL" "PJL" "PUR" "SIB" "STU" "TSI" "YRI")

for pop in "${populations[@]}"; do
    plink --bfile example --keep "${pop}_keep.txt" --freq --out "${pop}_freq.txt"
done
