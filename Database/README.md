# Database Folder README

This folder contains all the information regarding the creation of the database and where the data was sourced from 

## Database schema 

Below is the database schema of our database. 
The dashed lines connecting tables illustrate the various relationships between each table, indicating shared columns or relational connections. 

![Diagram](https://github.com/ml22826/Ubuntu/blob/main/Database/Screenshot%20from%202024-02-25%2019-14-58.png)


##Table giving brief description of each table 
| Table name | Brief Description | Source | Link | 
|-----------------|-----------------|-----------------|-----------------|
| SNP_info| Processed VCF file, contains information for each SNP such as position, their clinical impact (if any) and genes they affect |info is taken from chr1.vcf.gz. Clinical impact information was taken from GWAS and ClinVAR. The GWAS info can be found [here](https://www.ebi.ac.uk/gwas/docs/file-downloads), the file downloaded was All associations v.1|Row2,|
| Sample | ID of each sample from the 3928 indivudals and their associated population code| file |Rowe|
| Population | Row 2, Column 2| Row 2, Column 3|Rowe|
| genes| Row 2, Column 2| Row 2, Column 3|Rowe|
| Allele_frequencies | Row 2, Column 2| Row 2, Column 3|Rowe|
| Genotype_frequencies | Row 2, Column 2| Row 2, Column 3|Rowe|
| PCA_values | Row 2, Column 2| Row 2, Column 3|Rowe|
| Admixture | Row 2, Column 2| Row 2, Column 3|Rowe|

