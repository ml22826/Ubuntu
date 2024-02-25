import pandas as pd
import os 

adjustment_counter = 0
#function used to determine the alternate allele frequency based on the plink minor allele frequency file generated using plink v.1.9
#This is necessary as plink v.1.9 calculates the minor allele frequency which is usually the alternate allele but can sometimes be the reference allele. 
def adjust_maf(row):
    '''Function which determines whether the minor allele is the alternate or reference allele for each SNP.
    Keeps the MAF (Minor Allele Frequency) score as the alternate allele frequency if the minor allele=alternate allele . 
    Changes the alternate allele frequency to 1-MAF if minor allele=reference allele.'''
    global adjustment_counter  #count just in case
    #initialize variable which contains the alternate allele
    alternate_allele = row['ALT']
    
    #check if the alternate allele is the minor allele
    if alternate_allele == row['A1']:
        return row['MAF']  #if it's the same as A1 the score remains the same 
    #if the alternate allele isn't the minor allele check if it's the dominant allele
    elif alternate_allele == row['A2']:
        #counter but don't need this anymore
        adjustment_counter += 1  # 
        return 1 - row['MAF']  #change the score 
    else:
        return row['MAF']  #if neither condition is met (in case score is nan)
    
vcf=pd.read_csv('../ClinVar/final_dbSNP_sep_SNP_INFO.csv',low_memory=False)


allele_dir = 'allele_freq_all_groups'

os.makedirs(allele_dir, exist_ok=True)
# Get the list of files in the current directory
files = os.listdir('.')
adjustment_counter = 0

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

    

