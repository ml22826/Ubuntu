import pandas as pd 
import os 
from src.src.adjust_maf import adjust_maf


vcf=pd.read_csv('',low_memory=False) #path where the vcf is stored 



files = os.listdir('.') #make sure all the necessary files are in the same directory (all the frq.tsv files are in the working directory)


#iterates over all the allele frequency file which were generated using plink v.1.9 
for file in files:
    #Check if the item is a file and ends with .frq
    if os.path.isfile(file) and  file.endswith('frq.tsv'):
        
        #setting an order for the columns for each file
        desired_order = ['SNP','CHR','POS','ALT_FRQ','REF_FRQ','POP']
        
        #pop code at the beginning of the file name will become the population title
        pop_title = file[:3]
        
        #converting plink output file into a df 
        df=pd.read_csv(file,sep='\t') #change here according to the file format (if file is tsv add the sep='\t')
        
        #merging with the vcf file to know in each case if A1 represents the ALT allele or the REF allele
        merged_df = pd.merge(df, vcf[['SNP_ID', 'REF', 'ALT']], left_on='SNP', right_on='SNP_ID', how='left')
        
        #drop the 'SNP_ID' column from the merged DataFrame as it's no longer needed
        merged_df.drop('SNP_ID', axis=1, inplace=True)
        
        #Apply the adjust_maf to a new column called alternate allele frequency
        merged_df['ALT_FRQ'] = merged_df.apply(adjust_maf, axis=1)
        
        #New column to have the population name
        merged_df['POP']=pop_title
        
        #Getting the reference allele frequency
        merged_df['REF_FRQ']=1-merged_df['ALT_FRQ']
        
        merged_df.drop_duplicates(inplace=True)
        merged_df=merged_df[desired_order]
        
        #for the first file in the loop this command will create a new csv file, but for the subsequent files it will just append the results into the csv
        merged_df.to_csv('allele_freq.csv',  mode='a', header=not os.path.exists('allele_freq.csv'), index=False)