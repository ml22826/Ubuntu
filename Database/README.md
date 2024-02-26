# Database Folder README

This folder contains all the information regarding the creation of the database and where the data was sourced from 

## Database schema 

Below is the database schema of our database. 
The dashed lines connecting tables illustrate the various relationships between each table, indicating shared columns or relational connections. 

![Diagram](https://github.com/ml22826/Ubuntu/blob/main/Database/Screenshot%20from%202024-02-25%2019-14-58.png)


## Summary of Tables
| Table Name         | Description                                                     | Source                                                                        | Link |
|--------------------|-----------------------------------------------------------------|-------------------------------------------------------------------------------|------|
| SNP_info           | Contains information for each SNP including position, clinical impact, and affected genes. | SNP information sourced from chr1.vcf.gz. Clinical impact data obtained from GWAS and ClinVar. GWAS data can be accessed [here](https://www.ebi.ac.uk/gwas/docs/file-downloads) (All associations v.1). ClinVar clinical information available [here](https://ftp.ncbi.nlm.nih.gov/pub/clinvar/vcf_GRCh38/) (clinvar.vcf.gz). |  |
| Sample             | Identifier for each sample among 3928 individuals and their associated population code. | Internal file (sample_pop.tsv)                                                                  | [Link](Rowe) |
| Population         | Information about populations.                                   | Row 2, Column 2                                                                | Row 2, Column 3 |
| Genes              | Genetic information about genes.                                 | Row 2, Column 2                                                                | Row 2, Column 3 |
| Allele Frequencies| Frequencies of alleles within the population.                   | Row 2, Column 2                                                                | Row 2, Column 3 |
| Genotype Frequencies | Frequencies of genotypes within the population.                | Row 2, Column 2                                                                | Row 2, Column 3 |
| PCA Values         | Principal component analysis (PCA) values for each sample.      | Row 2, Column 2                                                                | Row 2, Column 3 |
| Admixture          | Information about admixture within the population.              | Row 2, Column 2                                                                | Row 2, Column 3 |

This table provides a brief overview of each table included in the dataset, along with their respective sources and links for further reference.

