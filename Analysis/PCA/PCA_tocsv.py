import pandas as pd

PCA_df = pd.read_csv('PCA__pca.eigenvec', sep= ' ', header=None)

#Create column names for PCA_df
column_names = ['id', 'Sub_ID', 'PC_1', 'PC_2', 'PC_3']
#Add column names to PCA_df
PCA_df.columns = column_names

#Connect id and Sub_ID columns with '_', drop Sub_ID column
PCA_df['id'] = PCA_df['id'].astype(str)
PCA_df['Sub_ID'] = PCA_df['Sub_ID'].astype(str)
PCA_df['id'] = PCA_df[['id', 'Sub_ID']].apply(lambda x: '_'.join(x), axis=1)
PCA_df = PCA_df.drop('Sub_ID', axis=1)

pop_df = pd.read_csv('sample_pop.tsv', sep= '\t')


#Merge PCA_df and pop_df to create a new dataframe
pop_PC_df = pd.merge(PCA_df, pop_df, on='id', how='left')



#Modify id colunm of those with  'NAN' population
def modify_id(row):
    if pd.isna(row['population']):
        return row['id'].split('_')[0]
    else:
        return row['id']

pop_PC_df['id'] = pop_PC_df.apply(modify_id, axis=1)


#Merge pop_PC_df and pop_df
pop_PC_df = pd.merge(pop_PC_df, pop_df, on='id', how='left')
pop_PC_df = pop_PC_df.drop('population_x', axis=1)
pop_PC_df = pop_PC_df.rename(columns={'population_y': 'population'})


#Create new dataframe without population column for databse table
pop_PC_df_database = pop_PC_df.drop('population', axis=1)
pop_PC_df_database = pop_PC_df_database.to_csv('PCA_pop.csv', index=False)


import matplotlib.pyplot as plt
#Make a list of all population
populations = pop_PC_df['population'].unique()
plt.figure(figsize=(10, 8))
#For eahc population plot induviduals in that population, create a scatter plot
for population_y in populations:
    subset = pop_PC_df[pop_PC_df['population'] == population_y]
    plt.scatter(subset['PC_1'], subset['PC_2'], label=population_y)
plt.title('PCA of Samples')
plt.xlabel('PC_1')
plt.ylabel('PC_2')
plt.legend()
plt.show()







