#important packages
import pandas as pd
import vcf #From the PyVCF python package 

#GWAS clinical relevance information
dfgwas=pd.read_csv('gwas_chr1_asso.csv') #this file was downloaded from the gwas website 

df=pd.read_csv('output_file.csv',sep='\t') #output_file.csv is the vcf which was converted into a  tab delimitted file (called it .csv but it's not comma delimited) containing only the SNP info + gene names + dbSNP_ID 

#initializaing new dataframe which will contain only the SNPs and the disease/trait column from the gwas file 
dfnew=pd.DataFrame(columns=['SNPS','Clinical relevance'])

dfnew['SNPS']=dfgwas['SNPS']
dfnew['Clinical relevance']=dfgwas['DISEASE/TRAIT']

#Merging the converted vcf with dfnew to establish a link between the snps from the vcf and disease/traits
common=pd.merge(df,dfnew,on='SNPS',how='left')

#CLINVAR from reference file 
#Filtering only the SNPS 

# this file comes from the clinvar website using this command on bash "wget https://ftp.ncbi.nlm.nih.gov/pub/clinvar/vcf_GRCh38/clinvar_20240107.vcf.gz"
vcf_reader = vcf.Reader(open('clinvar_1_only.vcf', 'r')) # the file was preprocessed to only contain information about chromosome 1
vcf_writer = vcf.Writer(open('filtered_output_file.vcf', 'w'), vcf_reader)

for record in vcf_reader:
    if record.is_snp:  #only keeping snps 
        #
        vcf_writer.write_record(record)

vcf_writer.close()

#Only keeping the CLNDN (Disease information) in the vcf 

vcf_reader=vcf.Reader(open('filtered_output_file.vcf','r'))
vcf_writer=vcf.Writer(open('filtered2_output.vcf','w'),vcf_reader)

for record in vcf_reader:
    record.INFO={'CLNDN':record.INFO['CLNDN'],} if 'CLNDN' in record.INFO else {}
    vcf_writer.write_record(record)
    
    
vcf_writer.close()

#Make it into a df to be able to merge it with the other data 

vcf_reader = vcf.Reader(open('filtered2_output.vcf','r'))

data=[]

for record in vcf_reader:
    row={
        'CHROM':record.CHROM,
        'POS':record.POS,
        'ID':record.ID,
        'REF':record.REF,
        'ALT':','.join(str(a) for a in record.ALT),
        'CLINICAL IMPLICATIONS':record.INFO
        
    }
    data.append(row)
    

    
df=pd.DataFrame(data)

#Merging here the df created by merging the gwas file and the vcf (common) with this new datafraframe (df)
#this will allow to create a file containing both gwas clinical information and clinvar clinical information
common2=pd.merge(common,df,on=['POS','REF','ALT'],how='left')
common2['Clinical_impact']=list(zip(common2['Clinical relevance'],common2['CLINICAL IMPLICATIONS']))
common2.drop(columns={'CLINICAL IMPLICATIONS','CHROM','ID_y','Clinical relevance'},inplace=True)

common2.to_csv('filtered2_draft.csv')

