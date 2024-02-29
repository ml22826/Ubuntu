# Annotation Folder README

This folder contains all the files and folders required to annotate our VCF file. 
The final annotated VCF file was in the form of a CSV and contained information about gene names, clinical relevance and dbSNPs for the SNPs in the original VCF 

## SnpEff

**Description:** SnpEff is used here for annotating the VCF file. The annotation primarily focuses on extracting gene names associated with SNPs.

## Linking VCF SNP IDs to dbSNP IDs

**Description:** This section focuses on the linking of the SNP_IDs of the VCF to their corresponding dbSNP IDs.

## Clinical Implications Annotation

**Description:** This folder looks into the various methodologies which were used to establish links between SNPs and potential clinical implications or traits. Information from GWAS websites and ClinVar is used to explore and find clinical associations.

## Gene table
**Description:** Created a table for each gene affected by the SNPs from the VCF.This table includes the start and end positions of the chromosome where the SNPs associated with those genes are located.

## Extraction from annotation
**Description:** This folder holds the code used to extract the gene names  from the annotated vcf. It was used to simplify the VCF. 

## Flowchart



Below, is a  flowchart illustrating the sequential steps undertaken to annotate the VCF file. This flowchart also includes snippets of the first few lines of each file. While hyperlinking isn't directly supported on GitHub for this flowchart, below the diagram includes all the necessary links for users to navigate through the folder, providing information into the steps involved in annotating the file with gene names, clinical information, and dbSNP IDs. The final file (complete_snp_info.csv) is that data which was inputed in our 'snp_info' table in our database.

![Diagram](https://github.com/camilaballenghien/cballenghien.github.io/blob/master/images/flowchart.drawio.png)


[SnpEff Annotation code](https://github.com/ml22826/Ubuntu/blob/main/Back_end/Database/Annotation_VCF/SnpEff/code.sh)

[Cleaning up the annotated VCF code](https://github.com/ml22826/Ubuntu/blob/main/Back_end/Database/Annotation_VCF/Extraction%20from%20annotation/gene_name_extraction.sh)

[Linking SNPs to their dbSNP_IDs](https://github.com/ml22826/Ubuntu/blob/main/Back_end/Database/Annotation_VCF/Linking%20SNP%20to%20their%20dbSNP%20ids/src/code.sh)

[Adding Clinical relevance information to the VCF](https://github.com/ml22826/Ubuntu/blob/main/Back_end/Database/Annotation_VCF/Clinical%20relevance/src/Adding_clinvar(1).py)

[Adding more clinical info](https://github.com/ml22826/Ubuntu/tree/main/Back_end/Database/Annotation_VCF/Clinical%20relevance/Adding%20more%20clinical%20relevance%20information)

[Cleaning up the file(final cleanup)](https://github.com/ml22826/Ubuntu/blob/main/Back_end/Database/Annotation_VCF/Clinical%20relevance/Adding%20more%20clinical%20relevance%20information/cleaning_final_file_3.py)



