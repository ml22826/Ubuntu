import plotly.express as px
import pandas as pd

df = pd.DataFrame([
    dict(Task="Data acquisition from VCF file(1)", Start='2024-01-26', Finish='2024-02-01', Resource="Shathavi"),
    dict(Task="Data acquisition from VCF file(2)", Start='2024-01-26', Finish='2024-02-01', Resource="Haotian"),
    dict(Task="Data acquisition for clinical relevance", Start='2024-01-28', Finish='2024-01-31', Resource="Camila"),
    dict(Task="Creation of database schema", Start='2024-01-26', Finish='2024-01-29', Resource="Camila"),
    dict(Task="Create Github page for Ubuntu", Start='2024-01-31', Finish='2024-02-01', Resource="Haotian"),
    dict(Task="Clustering research", Start='2024-01-26', Finish='2024-02-01', Resource="Aiza"),
    dict(Task="Start designing website structure and layout/website content creation", Start='2024-02-01',
         Finish='2024-02-06', Resource="Haotian"),
    dict(Task="Look into admixture analysis", Start='2024-02-01', Finish='2024-02-06', Resource="Camila"),
    dict(Task="Start doing clustering", Start='2024-02-01', Finish='2024-02-06', Resource="Aiza"),
    dict(Task="Adding information into the database/data cleaning and preprocessing", Start='2024-02-01',
         Finish='2024-02-07', Resource="Shathavi"),
    dict(Task="Elaboration github page", Start='2024-02-03', Finish='2024-02-05', Resource="Haotian"),
    dict(Task="Website structure", Start='2024-02-03', Finish='2024-02-07', Resource="Haotian"),
    dict(Task="Add annotation file of the VCF onto the database", Start='2024-02-03', Finish='2024-02-05',
         Resource="Camila"),
    dict(Task="Script for the admixture", Start='2024-02-02', Finish='2024-02-07', Resource="Camila"),
    dict(Task="Script pairwise population", Start='2024-02-08', Finish='2024-02-16', Resource="Shathavi"),
    dict(Task="Working on website visualisation (how to best visualise the results)", Start='2024-02-08',
         Finish='2024-02-16', Resource="Aiza"),
    dict(Task="Implementaiton data visualization tools and ensuring the website is user friendly", Start='2024-02-08',
         Finish='2024-02-16', Resource="Haotian"),
    dict(Task="Finishing off the analysis", Start='2024-02-16', Finish='2024-02-23', Resource="Camila"),
    dict(Task="Fining off project report for github", Start='2024-02-16', Finish='2024-02-23', Resource="Shathavi"),
    dict(Task="Finilizing the wesbite (making sure everything works)", Start='2024-02-16', Finish='2024-02-23',
         Resource="Haotian"),
    dict(Task="Running tests for website", Start='2024-02-23', Finish='2024-02-29', Resource="Haotian"),
    dict(Task="Review and finalize the report", Start='2024-02-23', Finish='2024-02-29', Resource="Shathavi"),
    dict(Task="Change the genotype table to have sample ids in column", Start='2024-02-01', Finish='2024-02-04', Resource="Shathavi"),

])

# Sorting the DataFrame by 'Start' date
df['Start'] = pd.to_datetime(df['Start'])  # Ensure the Start column is in datetime format
df = df.sort_values(by='Start')

fig = px.timeline(df, x_start="Start", x_end="Finish", y="Task", color="Resource")
# fig.update_yaxes
fig.show()
