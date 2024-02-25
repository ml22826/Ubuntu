# Annotation Folder README

## SnpEff

**Description:** SnpEff is used here for annotating the VCF file. The annotation primarily focuses on extracting gene names associated with SNPs.

## Linking VCF SNP IDs to dbSNP IDs

**Description:** This section focuses on the linking of the SNP_IDs of the VCF to their corresponding dbSNP IDs.

## Clinical Implications Annotation

**Description:** This folder looks into the various methodologies which were used to establish links between SNPs and potential clinical implications or traits. Information from GWAS websites and ClinVar is used to explore and find clinical associations.


```mermaid 
flowchart LR
    A("chr1.vcf.gz") -->|Annotation using snpEff| B("annotated38.vcf.gz")
    B --> C("simplified_file38.vcf.gz")
    C --> D("output_file.csv")
    D -->|Linking SNPs to their dbSNP IDs| E("filtered_2_draft.csv")
    E --> F("complete_snp_info.csv")

    B -->|Cleaning up the annotated VCF| C
    D -->|Adding Clinical relevance information to the VCF| E
    E -->|Adding more clinical info and cleaning up file| F
