import pandas as pd
import numpy as np
import os

#input CSV file containing allele frequency data
input_csv = '' #path to where the allele_freq.csv file is stored (generated by allele_frq.py)

#chunk size to read the CSV file in chunks (processing file in chunks to prevent the computer from crashing)
chunk_size = 50000  # 50,000 lines 

#iteration over chunks of the CSV file and calculate genotype frequencies based on the Hardy-Weinberg principle
for df_chunk in pd.read_csv(input_csv, chunksize=chunk_size):
    #desired order of columns for the output file
    desired_order = ['SNP', 'CHR', 'POS', 'HOM_ALT', 'HOM_REF', 'HET_REF', 'POP']
    
    #calculation of homozygous alternate genotype frequency
    df_chunk['HOM_ALT'] = df_chunk['ALT_FRQ'] ** 2
    
    #calculation of homozygous reference genotype frequency
    df_chunk['HOM_REF'] = df_chunk['REF_FRQ'] ** 2
    
    #calculation of heterozygous genotype frequency
    df_chunk['HET_REF'] = df_chunk['ALT_FRQ'] * df_chunk['REF_FRQ'] * 2
    
    #drop the original frequency columns
    df_chunk.drop(columns=['ALT_FRQ', 'REF_FRQ'], inplace=True)
    
    #reordering of columns according to desired order
    df_chunk = df_chunk[desired_order]
    
    #appending chunk to the output CSV file, creating the file if it doesn't exist
    df_chunk.to_csv('genotype_freq.csv', mode='a', header=not os.path.exists('genotype_freq.csv'), index=False)