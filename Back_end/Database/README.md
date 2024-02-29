# Database Folder README

This folder contains all the information regarding the creation of the database and where the data was sourced from 

## Database schema 

Below is the database schema of our database. 
The dashed lines connecting tables illustrate the various relationships between each table, indicating shared columns or relational connections. 

![Diagram](https://github.com/ml22826/Ubuntu/blob/main/Back_end/Database/Screenshot%20from%202024-02-25%2019-14-58.png)


## Summary of Tables
| Table Name         | Description                                                     | Source                                                                        | Link |
|--------------------|-----------------------------------------------------------------|-------------------------------------------------------------------------------|------|
| SNP_info           | Contains information for each SNP including position, clinical impact, and affected genes. | SNP information sourced from chr1.vcf.gz. Clinical impact data obtained from GWAS and ClinVar. GWAS data can be accessed [here](https://www.ebi.ac.uk/gwas/docs/file-downloads) (All associations v.1). ClinVar clinical information available [here](https://ftp.ncbi.nlm.nih.gov/pub/clinvar/vcf_GRCh38/) (clinvar.vcf.gz). |  |
| Sample             | Identifier for each sample among 3928 individuals and their associated population code. | Internal file (sample_pop.tsv)                                                                  |  |
| Population         | Information about each population code given in the sample_pop.tsv such as population name, superpopulation code and superpopulation name.| Superpopulation information was sourced from the 1000 genomes project                                                               | [Link](https://www.internationalgenome.org/data-portal/population?fbclid=IwAR0Jae3Fd1sjxgbyGcreNx2jLHzMaDihhKSFnY5OGVzZq2NHq8Jkfct1Tkk) to the page were the file was downloaded from (once on the link,click on 'Download the list' button to download the file)  |
| Genes              | Genetic information about genes.                                 | Sourced from the SNP_info table                                   |[Code](https://github.com/ml22826/Ubuntu/blob/main/Back_end/Database/Annotation_VCF/Gene%20table/src/gene_file.py) for getting the genes table from the SNP_info table|
| Allele Frequencies| allele frequencies for each SNP calculated across all the populations |Created using plink v.1.9 and by calculating allele frequency based on minor allele frequency (plink v.1.9 only allowed us to generate the minor allele frequency) |[Allele frequency folder](https://github.com/ml22826/Ubuntu/tree/main/Back_end/Database/Allele%20and%20Genotype%20Frequency)|
| Genotype Frequencies | genotype frequencies for each SNP calculated across all the population | Calculated using the Hardy Weinberg principle                                                               | [Genotype frequency folder](https://github.com/ml22826/Ubuntu/tree/main/Back_end/Database/Allele%20and%20Genotype%20Frequency) |
| PCA Values         | Principal component analysis (PCA) values for each sample.      |                                                     | Analysis folder|
| Admixture          | Information about admixture within the population.          | Created using the ADMIXTURE software | Analysis folder|


This table provides a brief overview of each table included in the dataset, along with their respective sources and links for further reference.

