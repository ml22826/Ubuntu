# Ubuntu

Welcome to the Github repository of the Ubuntu Analysis tool. 

Ubuntu is a fast and user friendly interface deigned to facilitate the analysis of genetic data collected from diverse human populations (at present there are 27 population groups).
This tool allows users to explore the genetic landscape of these population, getting insightful information into population structure and genetic diversity.
What it does: 
- Calculates allele and genotype frequencies of Single Nucleotide Polymorphisms (SNPs) within chromosome 1 across 27 distinct population groups spanning different regions of the world. It also offers the user the ability to compare frequencies between populations through visual representation.
- Provides information on the genetic information of the SNPs and potential clinical impacts.
- Utilizes clustering techniques such as Principal Component Analysis (PCA) and Admixture to examine relatedness at the population and at the superpopulation level, presenting visual representations for enhanced user experience.
  
This project was developed by the 'Ubuntu' student group at Queen Mary University of London as part of a collaborative effort for the Software Development module.

#### Setup


```bash
python3.10 -m venv .venv_project
source .venv_project/bin/activate
pip install -r requirements.txt
```
