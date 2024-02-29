import pandas as pd

q_df = pd.read_csv('vcf.bed.5.Q', delim_whitespace=True, header=None)
fam_df = pd.read_csv('vcf.bed.fam', sep=' ', header=None)


#Create column id in the q_df dataframe
id = ["K{}".format(i) for i in range(1, q_df.shape[1]+1)]
#Add column id to the q_df dataframe
q_df.columns = id
#Extract the first two columns from the fam_df dataframe
selecte_id = fam_df.iloc[:, [0, 1]]
selecte_id_str = selecte_id.apply(lambda row: ' '.join(row.values.astype(str)), axis=1)
#Insert the selected id into the q_df dataframe
q_df.insert(0, 'id', selecte_id_str)
q_df.set_index('id', inplace=True)


#Join the id with '_'
q_df.index = q_df.index.str.replace(' ', '_')

pop_df = pd.read_csv('sample_pop.tsv', sep='\t')

#Merge the q_df and pop_df dataframes
q_df = pd.merge(q_df, pop_df, on='id', how='left')

#Change id column that have NaN in the population column
def modify_id(row):
    if pd.isna(row['population']):
        return row['id'].split('_')[0]
    else:
        return row['id']

q_df['id'] = q_df.apply(modify_id, axis=1)

#Create a csv file with the q_df_database dataframe
q_df_database = q_df.drop(columns=['population'])
q_df_database.to_csv('Qfile_table_sample.csv', float_format='%.5f', index=False, header=True)

#Merge the q_df and pop_df dataframes
q_df = pd.merge(q_df, pop_df, on='id', how='left')
q_df
q_df = q_df.drop(columns=['population_x'])
q_df = q_df.rename(columns={"population_y": "population"})

#Create plot for amdixture for each population
average_K_values = q_df.groupby('population')[['K1', 'K2', 'K3', 'K4', 'K5']].mean()
ax = average_K_values.plot(kind='bar', stacked=True, figsize=(25,5), 
                      color=['blue', 'green', 'red', 'purple', 'orange'], 
                      edgecolor='black', linewidth=0.5,
                      title='Ancestry Proportions by Population',
                      xlabel='Population', ylabel='Ancestry Proportion')


#Create plot for amdixture based on selected population
average_K_values = q_df.groupby('population')[['K1', 'K2', 'K3', 'K4', 'K5']].mean()
population = input('Enter the population name: ').split(',')
filtered_df = average_K_values[average_K_values.index.isin(population)]
ax = filtered_df.plot(kind='bar', stacked=True, figsize=(25,5), 
                      color=['blue', 'green', 'red', 'purple', 'orange'], 
                      edgecolor='black', linewidth=0.5,
                      title='Ancestry Proportions by Population',
                      xlabel='Population', ylabel='Ancestry Proportion')