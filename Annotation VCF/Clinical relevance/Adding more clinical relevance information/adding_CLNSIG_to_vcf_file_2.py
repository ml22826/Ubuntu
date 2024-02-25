import pandas as pd 
import vcf 

#convert the preprocessed vcf file (which is now a csv) into a df 
df=pd.read_csv('filtered2_draft.csv')

#cleaning up the file
df['Clinical_impact'].replace("(nan, {'CLNDN': ['not_provided']})", None, inplace=True)
df['Clinical_impact'].replace("(nan, {'CLNDN': ['not_specified|not_provided']})", None, inplace=True)
df['Clinical_impact'].replace(["('Height', nan)"], 'Height', inplace=True)

vcf_reader = vcf.Reader(open('filtered3_output.vcf','r'))

data=[]

#iteration over each record in the vcf file 
for record in vcf_reader:
    row={
        'CHROM':record.CHROM,
        'POS':record.POS,
        'ID':record.ID,
        'REF':record.REF,
        'ALT':','.join(str(a) for a in record.ALT),
        'CLINICAL IMPLICATIONS':record.INFO
        
    }
    #append each (dictionary) row into data 
    data.append(row)
    

#create a data frame based on the vcf information 
df2=pd.DataFrame(data)

#merge with the preprocessed vcf file 
merged=pd.merge(df,df2 ,on=['POS','REF','ALT'],how='left')

#combining values from the clinical_impact and clinical implications column 
merged['Clinical_impact'] = merged['Clinical_impact'].fillna('')+ merged['CLINICAL IMPLICATIONS'].fillna('').astype(str)

#dropping columns
merged.drop(columns={'CHROM_y','CLINICAL IMPLICATIONS','ID'},inplace=True)

merged.drop_duplicates(inplace=True)

#converting data frame into csv
merged.to_csv('added_clinical_info_final_dbSNP_sep_SNP_INFO.csv')
