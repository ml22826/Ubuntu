import pandas as pd



df = pd.read_csv('added_clinical_info_final_dbSNP_sep_SNP_INFO.csv',low_memory=False)


#cleaning file (initially tried to clean using the 're' package using a loop, however the code didn't seem to work therefore this repetitive for cleaning was used
df['Clinical_impact'] = df['Clinical_impact'].astype(str)
df['Clinical_impact'] = df['Clinical_impact'].apply(lambda x: x.replace('(nan,', ''),)
df['Clinical_impact'] = df['Clinical_impact'].apply(lambda x: x.replace(', nan)', ''),)
df['Clinical_impact'] = df['Clinical_impact'].apply(lambda x: x.replace('(', ''),)
df['Clinical_impact'] = df['Clinical_impact'].apply(lambda x: x.replace(')', ''),)
df['Clinical_impact'] = df['Clinical_impact'].apply(lambda x: x.replace('[', ''),)
df['Clinical_impact'] = df['Clinical_impact'].apply(lambda x: x.replace(']', ''),)
df['Clinical_impact'] = df['Clinical_impact'].apply(lambda x: x.replace('|not_provided', ''),)
df['Clinical_impact'] = df['Clinical_impact'].apply(lambda x: x.replace('not_provided|', ''),)
df['Clinical_impact'] = df['Clinical_impact'].apply(lambda x: x.replace('|not_specified', ''),)
df['Clinical_impact'] = df['Clinical_impact'].apply(lambda x: x.replace('not_specified|', ''),)
df['Clinical_impact'] = df['Clinical_impact'].apply(lambda x: x.replace('}{', '}, {'),)
df['Clinical_impact'] = df['Clinical_impact'].apply(lambda x: x.replace('CLNSIG', 'Clinical Significance'),)
df['Clinical_impact'] = df['Clinical_impact'].apply(lambda x: x.replace('CLNDN', 'Disease info (ClinVar)'),)
df['Clinical_impact'] = df['Clinical_impact'].apply(lambda x: x.replace('}', ''),)
df['Clinical_impact'] = df['Clinical_impact'].apply(lambda x: x.replace('{', ''),)
df['Clinical_impact'] = df['Clinical_impact'].apply(lambda x: x.replace("'",''),)
df['Clinical_impact'] = df['Clinical_impact'].apply(lambda x: x.replace("_",' '),)

#converting df into final csv 
df.to_csv('complete_snp_info.csv',index=False)