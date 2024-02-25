

```mermaid 
graph LR
    A("chr1.vcf.gz") -->|Annotation| B("annotated38.vcf.gz")
    B --> C("simplified_file38.vcf.gz")
    C --> D("output_file.csv")
    D -->|Linking SNPs to their dbSNP IDs| E("filtered_2_draft.csv")
    E --> F("complete_snp_info.csv")

    B -->|Cleaning up the annotated VCF| C
    D -->|Adding Clinical relevance information to the VCF| E
    E -->|Adding more clinical info and cleaning up file| F
