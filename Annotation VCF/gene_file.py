#Code to have a table for genes 

import pandas as pd

#Read the file 
file_path = 'output_file.csv' 
tryout = pd.read_csv(file_path,sep='\t')

#There are instances where multiple genes are affected in a SNP
tryout_expanded = tryout.assign(GENE_NAMES=tryout['GENE_NAMES'].str.split(',')).explode('GENE_NAMES') #explode functions allows to separate each gene 

#Grouping by gene names and finding the first position where that gene name appears and the last position where it appears 
new_df = tryout_expanded.groupby('GENE_NAMES').agg(
    POS_START=('POS', 'min'),
    POS_END=('POS', 'max')
).reset_index()

#Renaming
new_df.rename(columns={'GENE_NAMES': 'GENE'}, inplace=True)

#output
output_file_path = 'processed_genes.csv'  
new_df.to_csv(output_file_path, index=False)