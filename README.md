# Ubuntu

Welcome to the Github repository of the Ubuntu Analysis tool. 

Ubuntu is a fast and user friendly interface deigned to facilitate the analysis of genetic data collected from diverse human populations (at present there are 27 population groups).
This tool allows users to explore the genetic landscape of these population, getting insightful information into population structure and genetic diversity.
What it does: 
- Calculates allele and genotype frequencies of Single Nucleotide Polymorphisms (SNPs) within chromosome 1 across 27 distinct population groups spanning different regions of the world. It also offers the user the ability to compare frequencies between populations through visual representation.
- Provides information on the genetic information of the SNPs and potential clinical impacts.
- Utilizes clustering techniques such as Principal Component Analysis (PCA) and Admixture to examine relatedness at the population and at the superpopulation level, presenting visual representations for enhanced user experience.
  
This project was developed by the 'Ubuntu' student group at Queen Mary University of London as part of a collaborative effort for the Software Development module.

## Requirements 

To run the user interface, make sure  you have the following installed and updated: 

Python 3.10

Flask 3.0.2 

Flask_WTF 1.2.1

mysql-connector-python 8.3.0

Pandas 2.2.0

Matplotlib 3.8.2

NumPy 1.26.3

seaborn 0.13.2

beautifulsoup4 4.12.2

This command on the CMD will install all the correct packages 

## Setup


```bash
python3.10 -m venv .venv_project
source .venv_project/bin/activate
pip install -r requirements.txt
```
Download the DB SQL Script (as the DB is large it might take a few hours): [ubuntu.sql](https://qmulprod-my.sharepoint.com/personal/bt23801_qmul_ac_uk/_layouts/15/onedrive.aspx?id=%2Fsites%2FDatabaseforUbuntuproject%2FShared%20Documents&listurl=https%3A%2F%2Fqmulprod%2Esharepoint%2Ecom%2Fsites%2FDatabaseforUbuntuproject%2FShared%20Documents&sharedLibraryCreated=true)


Download the whole Flask app (make sure you have installed the requirements and changed the value of 'user', 'password', 'host', 'database' in the read_config function in the app.py file):

Github link: https://github.com/ml22826/Ubuntu/tree/main/Front%20end

Install MySQL server 8.0 

## MySQL 

Open the MySQL command line and create a database called ubuntu using this command:
```SQL
CREATE DATABASE ubuntu;
```
Import the SQL file into the db (ubuntu.sql file)

Import the file to the DB (don't forget to unzip the script first):
```bash
mysql -u username -p ubuntu < /path/to/your/ubuntu.sql
```


User can also create an identical database from scratch by running the SQL script in the Back_end/Database folder which will create all the tables necessary (including the indexing and paritioning).
In this folder there is also sql scripts of the tables which aren't too large that the user can download. 

## RUNNING THE SOFTWARE (FLASK)

To run the web application, move to Front end directory and execute the commands based on OS:

### Run flask on WINDOWS:

```bash
set FLASK_APP=app.py
set FLASK_DEBUG=1
flask run
```

### Run flask on LINUX:

```bash
export FLASK_APP=app.py
export FLASK_DEBUG=1
flask run
```




