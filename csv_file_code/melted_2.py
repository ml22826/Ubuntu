import pandas as pd

chunk_size = 10000

melted_df = pd.DataFrame()

def melt_chunk(chunk):
    for col in chunk.columns[1:]:
        chunk[col] = chunk[col].astype(str).str.replace('O', '0')
        chunk[col] = pd.to_numeric(chunk[col], errors='coerce')
    melt_chunk = chunk.melt(id_vars=chunk.columns[0], var_name='SuperpopulationCode', value_name='AlternateAlleleFrequency')
    melt_chunk['ReferenceAlleleFrequency'] = 1.0 - melt_chunk['AlternateAlleleFrequency']
    return melt_chunk


for chunk in pd.read_csv('AF.tsv', sep='\t', chunksize=chunk_size, dtype=str, header=0):
    melted_chunk = melt_chunk(chunk)
    melted_df = pd.concat([melted_df, melted_chunk], ignore_index=True)

melted_df.to_csv('AF_table.tsv', sep='\t', index=False)
