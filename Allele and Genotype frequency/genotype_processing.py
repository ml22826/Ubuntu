import pandas as pd
import numpy as np
import os

#allele frequency file
input_csv='allele_freq.csv'

#chunk size to go over the file
chunk_size = 50000  # 50 000 lines 
#read the CSV file in chunks and calculate genotype frequency based on the hardy weinburg principle
for df_chunk in pd.read_csv(input_csv, chunksize=chunk_size):
    desired_order=['SNP','CHR','POS','HOM_ALT','HOM_REF','HET_REF','POP']
    df_chunk['HOM_ALT']=df_chunk['ALT_FRQ']**2
    df_chunk['HOM_REF']=df_chunk['REF_FRQ']**2
    df_chunk['HET_REF']=df_chunk['ALT_FRQ']*df_chunk['REF_FRQ']*2
    df_chunk.drop(columns=['ALT_FRQ','REF_FRQ'],inplace=True)
    df_chunk=df_chunk[desired_order]
    df_chunk.to_csv('genotype_freq.csv',  mode='a', header=not os.path.exists('genotype_freq.csv'), index=False)
    
    
