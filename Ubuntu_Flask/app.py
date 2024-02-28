# Ubuntu flask code for website

# Import all packages used in this programme
from flask import Flask, render_template, url_for, redirect, request, session, Response
import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt
import re
import io
import os
import tempfile
import json
import base64
import numpy as np
import seaborn as sns
from bs4 import BeautifulSoup
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, SubmitField
from wtforms.validators import Optional

# Create a flask application
app = Flask(__name__)

# Set the secret key for the Flask application to database
app.config['SECRET_KEY'] = 'ubuntu'

# Define all the BooleanField, StringField and Submit buttons used in this programme 
class QueryForm(FlaskForm):
    ACB = BooleanField('ACB', default=False)
    ASW = BooleanField('ASW', default=False)
    ESN = BooleanField('ESN', default=False)
    GWD = BooleanField('GWD', default=False)
    LWK = BooleanField('LWK', default=False)
    MSL = BooleanField('MSL', default=False)
    YRI = BooleanField('YRI', default=False)
    
    CLM = BooleanField('CLM', default=False)
    MXL = BooleanField('MXL', default=False)
    PEL = BooleanField('PEL', default=False)
    PUR = BooleanField('PUR', default=False)

    CDX = BooleanField('CDX', default=False)
    CHB = BooleanField('CHB', default=False)
    CHS = BooleanField('CHS', default=False)
    JPT = BooleanField('JPT', default=False)
    KHV = BooleanField('KHV', default=False)

    CEU = BooleanField('CEU', default=False)
    FIN = BooleanField('FIN', default=False)
    GBR = BooleanField('GBR', default=False)
    IBS = BooleanField('IBS', default=False)
    TSI = BooleanField('TSI', default=False)

    BEB = BooleanField('BEB', default=False)
    GIH = BooleanField('GIH', default=False)
    ITU = BooleanField('ITU', default=False)
    PJL = BooleanField('PJL', default=False)
    STU = BooleanField('STU', default=False)

    SIB = BooleanField('SIB', default=False)

    AFR = BooleanField('AFR', default=False)
    AMR = BooleanField('AMR', default=False)
    EAS = BooleanField('EAS', default=False)
    EUR = BooleanField('EUR', default=False)
    SAS = BooleanField('SAS', default=False)

    id = StringField('Enter valid ID', validators=[Optional()])
    
    chr = StringField('Enter a valid region: Chromosome', validators=[Optional()])
    start = IntegerField('Start Position', validators=[Optional()])
    end = IntegerField('End Position', validators=[Optional()])

    gene_name = StringField('Enter valid gene names:', validators=[Optional()])
    
    search_pop = SubmitField('Create the plot at the population level')
    search_superpop = SubmitField('Create the plot at the superpopulation level')
    search_gene = SubmitField('Search by Gene Name')
    search_region = SubmitField('Search by Region')
    search_id = SubmitField('Search by ID')

# Define all the functions used in this programme
def read_config():
    # Database connection parameters
    config = {
        'user': 'root',
        'password': 'ubuntu123',  
        'host': 'localhost',
        'database': 'ubuntu',
    }
    return config

def pca_scores(pop):
    
    config = read_config()  # Read config

    try:
        # Create connection to the database
        db = mysql.connector.connect(**config)
        cursor = db.cursor(dictionary=True) 
        # Read and select data from the pca_values and population tables in the database
        cursor.execute('''
                       SELECT pca_values.PC_1, pca_values.PC_2, pca_values.Population, population.SuperpopulationCode
                       FROM pca_values 
                       JOIN population ON pca_values.Population = population.PopulationCode
                       WHERE Population = %s
                       ''', (pop,))
        # Get all rows returned by the SQL command
        pca_scores = cursor.fetchall()
    
    except mysql.connector.Error as err:
        print(f"Something went wrong: {err}")
    
    finally:
        if cursor:
            cursor.close()
        if db and db.is_connected():
            db.close()

    return pca_scores

def read_admixture_data(pop):
    
    config = read_config()

    try:
        db = mysql.connector.connect(**config)
        cursor = db.cursor(dictionary=True)
        # Read and select data from the admixture, population and sample tables in the database
        cursor.execute('''
                       SELECT sample.population, population.SuperpopulationCode, admixture.K1, admixture.K2, admixture.K3, admixture.K4, admixture.K5
                       FROM admixture 
                       JOIN sample ON admixture.sample_id = sample.id
                       JOIN population ON sample.population = population.PopulationCode
                       WHERE Population = %s
                       ''', (pop,))
        admixture_data = cursor.fetchall()
    
    except mysql.connector.Error as err:
        print(f"Something went wrong: {err}")
    
    finally:
        if cursor:
            cursor.close()
        if db and db.is_connected():
            db.close()

    return admixture_data

def snp_id(snp_ids, pop):
    
    config = read_config()
    SNP_data = []
    pops = []
    pops.append(pop)
    try:
        db = mysql.connector.connect(**config)
        cursor = db.cursor()

        # Create placeholders for the query
        ids_placeholders = ', '.join(['%s'] * len(snp_ids))
        pop_placeholders1 = ', '.join(['%s'] * len(pops))
        pop_placeholders2 = ', '.join(['%s'] * len(pops))
        
        # Put all parameters in one tuple for the execute method
        params = tuple(snp_ids + pops + pops)
        
        # Read and select SNP data from the snp_info, allele_frequencies and genotype_frequencies tables in the database by snp_ids and pops
        query = f"""
        SELECT DISTINCT sni.*, af.ALT_FRQ, af.REF_FRQ, gf.HOM_ALT, gf.HOM_REF, gf.HET, gf.POP
        FROM snp_info AS sni
        JOIN allele_frequencies AS af ON af.SNP = sni.SNP_ID
        JOIN genotype_frequencies AS gf ON gf.SNP = sni.SNP_ID 
        WHERE sni.SNP_ID IN ({ids_placeholders}) AND af.POP IN ({pop_placeholders1}) AND gf.POP IN ({pop_placeholders2});
        """
        print(query)
        
        cursor.execute(query, params)
        SNP_data = cursor.fetchall()
    
    except mysql.connector.Error as err:
        return f"Something went wrong: {err}", 500
    
    finally:
        if cursor:
            cursor.close()
        if db and db.is_connected():
            db.close()
    
    return SNP_data

def position(chr, start, end, pop):
    
    config = read_config()
    SNP_data = []

    try:
        db = mysql.connector.connect(**config)
        cursor = db.cursor()

        # Read and select SNP data from the snp_info, allele_frequencies and genotype_frequencies tables in the database by region and pop
        query = """
           SELECT sni.*, af.ALT_FRQ, af.REF_FRQ, gf.HOM_ALT, gf.HOM_REF, gf.HET, gf.POP
            FROM snp_info 
	            AS sni
            JOIN allele_frequencies 
	            AS af 
	            ON af.SNP=sni.SNP_ID
            JOIN genotype_frequencies 
	            AS gf 
	            ON gf.SNP=sni.SNP_ID
            WHERE sni.CHROM=%s AND af.POP=%s AND gf.POP=%s AND sni.POS BETWEEN %s AND %s;
        """
        cursor.execute(query, (chr, pop, pop, start, end))
        SNP_data = cursor.fetchall()

    except mysql.connector.Error as err:
        print(f"Something went wrong: {err}")
    
    finally:
        if cursor:
            cursor.close()
        if db and db.is_connected():
            db.close()

    return SNP_data

def query_genes(gene_names):

    config = read_config()
    
    try:
        db = mysql.connector.connect(**config)
        cursor = db.cursor()
        
        # Create the gene_info table
        cursor.execute(""" CREATE TABLE gene_info
                        (CHROM VARCHAR(50),
                        POS INT,
                        SNP_ID VARCHAR(500),
                        REF VARCHAR(50),
                        ALT VARCHAR(50),
                        GENES VARCHAR (1000),
                        dbSNP_ID VARCHAR(1000),
                        Clinical_impact TEXT); """)

        # Read and select SNP data from snp_info in database by gene name and insert into gene_info table
        for gene in gene_names:
            gene=gene.upper()
            query="""INSERT INTO gene_info(CHROM, POS, SNP_ID, REF, ALT, GENES, dbSNP_ID, Clinical_impact)
                SELECT DISTINCT si.CHROM, si.POS, si.SNP_ID, si.REF, si.ALT, si.GENES, si.dbSNP_ID, si.Clinical_impact
                FROM snp_info si
                JOIN genes g ON si.POS BETWEEN g.POS_START AND g.POS_END
                WHERE g.GENE = %s ;
                """

            cursor.execute(query,(gene,))
            db.commit()

    except mysql.connector.Error as err:
        print(f"Something went wrong: {err}")

    
    finally:
        if cursor is not None:
            cursor.close()
        if db is not None and db.is_connected():
            db.close()

def select_pops(pops):
    SNP_data = []
    config = read_config()
    try:
        db = mysql.connector.connect(**config)
        cursor = db.cursor()

        # Read and select allele and genotype frequencies data from the allele_frequencies and genotype_frequencies tables in the database by pops
        for pop in pops:
            query = '''
            SELECT gi.*, af.ALT_FRQ, af.REF_FRQ, gf.HOM_ALT, gf.HOM_REF, gf.HET, gf.POP
            FROM gene_info gi
            INNER JOIN allele_frequencies af ON af.SNP = gi.SNP_ID
            INNER JOIN genotype_frequencies gf ON gf.SNP = gi.SNP_ID
            WHERE af.POP = %s AND gf.POP = %s;
            '''
            cursor.execute(query, (pop, pop))
            rows = cursor.fetchall()
            
            if rows:
                for row in rows:
                    SNP_data.append(row)
            else:
                print(f"No results found")

        cursor.execute("DROP TABLE IF EXISTS gene_info")
        
    except mysql.connector.Error as err:
        print(f"Something went wrong: {err}")

    finally:
        if cursor is not None:
            cursor.close()
        if db is not None and db.is_connected():
            db.close()

    return SNP_data

def create_temp_file(results):
    # Create a temporary file to store the result
    temp_file = tempfile.NamedTemporaryFile(delete=False, mode='w+t')
    json.dump(results, temp_file)
    temp_file.close()
    return temp_file.name

def calculate_fst(pop1_freq, pop2_freq):
    # Calculate Fst
    HS = (2 * pop1_freq * (1 - pop1_freq) + 2 * pop2_freq * (1 - pop2_freq)) / 2
    HT = 2 * ((pop1_freq + pop2_freq) / 2) * (1 - (pop1_freq + pop2_freq) / 2)
    if HT == 0:
        return 0
    else:
        return (HT - HS) / HT



# Create the index page
@app.route('/')
def index():
    return render_template('index.html') # Use index.html as template

# Create the clustering analysis page
@app.route('/clustering_analysis', methods=['GET', 'POST'])  # Create a website that can request data from the database and send data to the server
def clustering_analysis():
    form = QueryForm()  # Create an instance of a QueryForm class
    # Check the form has been submitted and the data in the form is in compliance with the validation rules
    if form.validate_on_submit():
        pops = []
        superpops = []  # Create two list variables called pops and superpops.
        judge = 'pop'  # Create a string variable called judge, which will be used to decide the levels to be plotted
        if form.SIB.data: 
            pops.append('SIB')  # If the BooleanField has been clicked, the pops variable will have its name
        
        if form.ACB.data:
            pops.append('ACB')
        if form.ASW.data:
            pops.append('ASW')
        if form.ESN.data:
            pops.append('ESN')
        if form.GWD.data:
            pops.append('GWD')
        if form.LWK.data:
            pops.append('LWK')
        if form.MSL.data:
            pops.append('MSL')
        if form.YRI.data:
            pops.append('YRI')

        if form.CLM.data:
            pops.append('CLM')
        if form.MXL.data:
            pops.append('MXL')
        if form.PEL.data:
            pops.append('PEL')
        if form.PUR.data:
            pops.append('PUR')
        
        if form.CDX.data:
            pops.append('CDX')
        if form.CHB.data:
            pops.append('CHB')
        if form.CHS.data:
            pops.append('CHS')
        if form.JPT.data:
            pops.append('JPT')
        if form.KHV.data:
            pops.append('KHV')
        
        if form.CEU.data:
            pops.append('CEU')
        if form.FIN.data:
            pops.append('FIN')
        if form.GBR.data:
            pops.append('GBR')
        if form.IBS.data:
            pops.append('IBS')
        if form.TSI.data:
            pops.append('TSI')
    
        if form.BEB.data:
            pops.append('BEB')
        if form.GIH.data:
            pops.append('GIH')
        if form.ITU.data:
            pops.append('ITU')
        if form.PJL.data:
            pops.append('PJL')
        if form.STU.data:
            pops.append('STU')

        if form.AFR.data:
            judge = 'superpop'  # When the Boolean field of the superpopulation has been clicked, the string in the judge variable will be changed
            for pop in ['ACB','ASW', 'ESN', 'GWD', 'LWK', 'MSL', 'YRI']:
                superpops.append(pop)  # The superpops variable has all the population names related to the superpopulations clicked
        if form.AMR.data:
            judge = 'superpop'
            for pop in ['CLM','MXL', 'PEL', 'PUR']:
                superpops.append(pop)
        if form.EAS.data:
            judge = 'superpop'
            for pop in ['CDX','CHB', 'CHS', 'JPT', 'KHV']:
                superpops.append(pop)
        if form.EUR.data:
            judge = 'superpop'
            for pop in ['CEU','FIN', 'GBR', 'IBS', 'TSI']:
                superpops.append(pop)
        if form.SAS.data:
            judge = 'superpop'
            for pop in ['BEB','GIH', 'ITU', 'PJL', 'STU']:
                superpops.append(pop)
        
        if form.search_pop.data:
            return redirect(url_for('cluster_results', pops=pops, judge=judge))
        
        elif form.search_superpop.data:
            return redirect(url_for('cluster_results', pops=superpops, judge=judge))  # Redirect different data to the same function based on user choice

    return render_template('clustering_analysis.html', form=form)  # Use clustering_analysis.html as template

# Create the page showing the result of the clustering analysis
@app.route('/clustering_analysis/pops/<pops>/<judge>')  # Pass two variables called pops and judge to the function
def cluster_results(pops, judge):
    pops = [p.strip(" '") for p in pops.strip("[]").split(',')]  # Change string to list
    pca_data = []
    for pop in pops:
        pca = pca_scores(pop)
        pca_data.extend(pca)
    
    # Initialise a plot
    fig, ax = plt.subplots()

    if judge == 'superpop':  # Decide whether to plot at population or superpopulation level
        superpops = set(score['SuperpopulationCode'] for score in pca_data)  # Group data by superpopulation level and plot each group in a different colour
        for superpop in superpops:
            # Filter scores for the selected superpopulation
            pc1 = [score['PC_1'] for score in pca_data if score['SuperpopulationCode'] == superpop]
            pc2 = [score['PC_2'] for score in pca_data if score['SuperpopulationCode'] == superpop]
            # Plot the scores with a label for the legend
            ax.scatter(pc1, pc2, label=superpop)
    
    else:
        populations = set(score['Population'] for score in pca_data)  # Group data by population level and plot each group in a different colour
        for pop in populations:
            # Filter scores for the selected superpopulation
            pc1 = [score['PC_1'] for score in pca_data if score['Population'] == pop]
            pc2 = [score['PC_2'] for score in pca_data if score['Population'] == pop]
            # Plot the scores with a label for the legend
            ax.scatter(pc1, pc2, label=pop)

    # Add title and labels
    plt.title('PCA Plot')
    plt.xlabel('PC_1')
    plt.ylabel('PC_2')

    # Define the layout of the legend based on the number of populations (superpopulations) selected
    if judge == 'superpop':
        n_superpops = len(superpops)
        if n_superpops == 5:
            columns = 5
        elif n_superpops == 4:
            columns = 4
        elif n_superpops == 3:
            columns = 3
        elif n_superpops == 2:
            columns = 2
        elif n_superpops == 1:
            columns = 1
        else:
            columns = 6
    else:
        n_populations = len(populations)
        if n_populations <= 5:
            columns = 1
        elif n_populations <= 10:
            columns = 2
        elif n_populations <= 15:
            columns = 3
        elif n_populations <= 20:
            columns = 4
        elif n_populations <= 25:
            columns = 5
        else:
            columns = 6  

    # Add a legend outside the plot at the centre bottom
    plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.3), ncol=columns, borderaxespad=0.5)

    # Adjust the layout to make room for the legend
    plt.tight_layout()

    # Store the plot in a bytes buffer, encode in base64 and pass to the template
    img = io.BytesIO()
    plt.savefig(img, format='png', bbox_inches='tight')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode('utf-8')

    return render_template('pca_plot.html', plot_url=plot_url)  # Use pca_plot.html as template

# Create the admixture analysis page
@app.route('/admixture_analysis', methods=['GET', 'POST'])
def admixture_analysis():
    form = QueryForm()
    if form.validate_on_submit():
        pops = []
        superpops = []
        judge = 'pop'
        if form.SIB.data:
            pops.append('SIB')
        
        if form.ACB.data:
            pops.append('ACB')
        if form.ASW.data:
            pops.append('ASW')
        if form.ESN.data:
            pops.append('ESN')
        if form.GWD.data:
            pops.append('GWD')
        if form.LWK.data:
            pops.append('LWK')
        if form.MSL.data:
            pops.append('MSL')
        if form.YRI.data:
            pops.append('YRI')

        if form.CLM.data:
            pops.append('CLM')
        if form.MXL.data:
            pops.append('MXL')
        if form.PEL.data:
            pops.append('PEL')
        if form.PUR.data:
            pops.append('PUR')
        
        if form.CDX.data:
            pops.append('CDX')
        if form.CHB.data:
            pops.append('CHB')
        if form.CHS.data:
            pops.append('CHS')
        if form.JPT.data:
            pops.append('JPT')
        if form.KHV.data:
            pops.append('KHV')
        
        if form.CEU.data:
            pops.append('CEU')
        if form.FIN.data:
            pops.append('FIN')
        if form.GBR.data:
            pops.append('GBR')
        if form.IBS.data:
            pops.append('IBS')
        if form.TSI.data:
            pops.append('TSI')
    
        if form.BEB.data:
            pops.append('BEB')
        if form.GIH.data:
            pops.append('GIH')
        if form.ITU.data:
            pops.append('ITU')
        if form.PJL.data:
            pops.append('PJL')
        if form.STU.data:
            pops.append('STU')

        if form.AFR.data:
            judge = 'superpop'
            for pop in ['ACB','ASW', 'ESN', 'GWD', 'LWK', 'MSL', 'YRI']:
                superpops.append(pop)
        if form.AMR.data:
            judge = 'superpop'
            for pop in ['CLM','MXL', 'PEL', 'PUR']:
                superpops.append(pop)
        if form.EAS.data:
            judge = 'superpop'
            for pop in ['CDX','CHB', 'CHS', 'JPT', 'KHV']:
                superpops.append(pop)
        if form.EUR.data:
            judge = 'superpop'
            for pop in ['CEU','FIN', 'GBR', 'IBS', 'TSI']:
                superpops.append(pop)
        if form.SAS.data:
            judge = 'superpop'
            for pop in ['BEB','GIH', 'ITU', 'PJL', 'STU']:
                superpops.append(pop)
        
        if form.search_pop.data:
            return redirect(url_for('admixture_results', pops=pops, judge=judge))
        
        elif form.search_superpop.data:
            return redirect(url_for('admixture_results', pops=superpops, judge=judge))
        
    return render_template('admixture_analysis.html', form=form)  # Use admixture_analysis.html as template

# Create the page showing the result of the admixture analysis
@app.route('/admixture_analysis/pops/<pops>/<judge>')
def admixture_results(pops, judge):
    pops = [p.strip(" '") for p in pops.strip("[]").split(',')]
    admixture_data = []  # Create a list to get the results of the read_admixture_data function
    for pop in pops:
        adm = read_admixture_data(pop)
        admixture_data.extend(adm)

    # Set up a Pandas dataframe for easy manipulation of the data
    df = pd.DataFrame(admixture_data, columns=['population', 'SuperpopulationCode', 'K1', 'K2', 'K3', 'K4', 'K5', ])
    
    # Group data based on user selection
    if judge == 'superpop': 
        df = df.drop('population', axis=1)  # Drop the population column
        df = df.groupby('SuperpopulationCode', as_index=False).mean()  # Group the data at the superpopulation level and calculate the average K
        group = 'SuperpopulationCode'
    else:
        df = df.drop('SuperpopulationCode', axis=1)  # Drop the SuperpopulationCode column
        df = df.groupby('population', as_index=False).mean()   # Group the data at the population level and calculate the average K
        group = 'population'
    
    # Initialise a plot
    fig, ax = plt.subplots()

    components = ['K1', 'K2', 'K3', 'K4', 'K5']
    df.plot(kind='bar', x=group, stacked=True, y=components)  # Plot the stacked bar chart
    
    # Add title, labels and legend
    ax.set_ylabel('Values')
    ax.set_title(f'Admixture by {group}')
    plt.xticks(rotation=45)
    plt.legend(title='Components', loc='upper left', bbox_to_anchor=(1, 1))

    # Adjust the layout to make room for the legend
    plt.tight_layout(rect=[0, 0, 0.85, 1])

    # Store the plot in a bytes buffer, encode in base64
    buf = io.BytesIO()
    plt.tight_layout()  # Adjust the layout to make room for the rotated x-axis labels
    plt.savefig(buf, format='png')
    buf.seek(0)
    image = base64.b64encode(buf.getvalue()).decode('utf-8')

    return render_template('admixture_results.html', image=image)  # Use admixture_results.html as template

# Generate allele frequencies, genotype frequencies, and clinical relevance retrieval page   
@app.route('/allele&genotype_frequencies-clinical_relevance', methods=['GET', 'POST'])
def AF_GF_CR():
    form = QueryForm()
    if form.validate_on_submit():
        pops = []
        if form.SIB.data:
            pops.append('SIB')
        
        if form.ACB.data:
            pops.append('ACB')
        if form.ASW.data:
            pops.append('ASW')
        if form.ESN.data:
            pops.append('ESN')
        if form.GWD.data:
            pops.append('GWD')
        if form.LWK.data:
            pops.append('LWK')
        if form.MSL.data:
            pops.append('MSL')
        if form.YRI.data:
            pops.append('YRI')

        if form.CLM.data:
            pops.append('CLM')
        if form.MXL.data:
            pops.append('MXL')
        if form.PEL.data:
            pops.append('PEL')
        if form.PUR.data:
            pops.append('PUR')
        
        if form.CDX.data:
            pops.append('CDX')
        if form.CHB.data:
            pops.append('CHB')
        if form.CHS.data:
            pops.append('CHS')
        if form.JPT.data:
            pops.append('JPT')
        if form.KHV.data:
            pops.append('KHV')
        
        if form.CEU.data:
            pops.append('CEU')
        if form.FIN.data:
            pops.append('FIN')
        if form.GBR.data:
            pops.append('GBR')
        if form.IBS.data:
            pops.append('IBS')
        if form.TSI.data:
            pops.append('TSI')
    
        if form.BEB.data:
            pops.append('BEB')
        if form.GIH.data:
            pops.append('GIH')
        if form.ITU.data:
            pops.append('ITU')
        if form.PJL.data:
            pops.append('PJL')
        if form.STU.data:
            pops.append('STU')

        if form.search_id.data:  # When the search buttons have been clicked, the web page is redirected based on the function that the user has selected
            return redirect(url_for('id', id=form.id.data, pops=pops))
        elif form.search_region.data:
            return redirect(url_for('region', chr=form.chr.data, start=form.start.data, end=form.end.data, pops=pops))
        elif form.search_gene.data:
            return redirect(url_for('gene_name', gene_name=form.gene_name.data, pops=pops))
    return render_template('AF_GF_CR.html', form=form)  # Use AF_GF_CR.html as template

# Create the page that shows the result of the retrieval by SNP ID
@app.route('/allele&genotype_frequencies-clinical_relevance/id/<id>/<pops>')
def id(id, pops):
    pops = [p.strip(" '") for p in pops.strip("[]").split(',')]
    snp_ids = re.split('[^a-zA-Z0-9+-:]+', id)  # Allow users to split their input with ' ', ',', ';' or other special characters except ':'
    results = []
    for pop in pops:
        result = snp_id(snp_ids, pop)
        results.extend(result)
    file_path = create_temp_file(results)  # Use a temporary file to pass the results variable to the next function
    return render_template('results.html', results=results, file_path=file_path)  # Use results.html as template

# Create the page that shows the result of the retrieval by region
@app.route('/allele&genotype_frequencies-clinical_relevance/region/<chr>/<start>/<end>/<pops>')
def region(chr, start, end, pops):
    pops = [p.strip(" '") for p in pops.strip("[]").split(',')]
    results = []
    for pop in pops:
        result = position(chr, start, end, pop)
        results.extend(result)
    file_path = create_temp_file(results)
    return render_template('results.html', results=results, file_path=file_path)  # Use results.html as template

# Create the page that shows the result of the retrieval by gene name
@app.route('/allele&genotype_frequencies-clinical_relevance/gene/<gene_name>/<pops>')
def gene_name(gene_name, pops):
    pops = [p.strip(" '") for p in pops.strip("[]").split(',')]
    list_gene_name = re.split('[^a-zA-Z0-9+-]+', gene_name)
    results = []
    query_genes(list_gene_name)
    results.extend(select_pops(pops))
    file_path = create_temp_file(results)
    return render_template('results.html', results=results, file_path=file_path)  # Use results.html as template

# Create the page that shows the population matrix
@app.route('/allele&genotype_frequencies-clinical_relevance/pop_matrix')
def pop_matrix():
    # Get the file path from the query parameter
    file_path = request.args.get('file_path')

    # Open the temporary file and read the data
    with open(file_path, 'r') as temp_file:
        SNP_data = json.load(temp_file)

    # Delete the temporary file after reading
    os.unlink(file_path)

    # Create a Pandas dataframe based on the SNP data
    df = pd.DataFrame(SNP_data, columns=['CHROM', 'POS', 'SNP_ID', 'REF', 'ALT', 'GENES', 'dbSNP_ID', 'Clinical_impact', 'ALT_FRQ', 'REF_FRQ', 'HOM_ALT', 'HOM_REF', 'HET', 'POP'])
    print(df)
    session.pop('results', None)

    # Specify the populations and SNPs
    populations = df['POP'].unique()
    snps = df['SNP_ID'].unique()

    # Create an empty Fst matrix
    fst_matrix = pd.DataFrame(np.nan, index=populations, columns=populations)
    print(fst_matrix)

    # For each pair of populations, calculate Fst
    for snp in snps:
        for i, pop1 in enumerate(populations):
            for j, pop2 in enumerate(populations):
                if i >= j:  # Avoid redundant calculations and self-comparisons
                   continue
                # Get the allele frequencies from the Pandas dataframe for the populations for this SNP
                freq_pop1 = df[(df['SNP_ID'] == snp) & (df['POP'] == pop1)]['ALT_FRQ'].values[0]
                freq_pop2 = df[(df['SNP_ID'] == snp) & (df['POP'] == pop2)]['ALT_FRQ'].values[0]
            
                # Calculate Fst for this pair of populations and SNP
                fst = calculate_fst(freq_pop1, freq_pop2)
            
                # Store Fst in matrix
                fst_matrix.at[pop1, pop2] = fst if pd.isna(fst_matrix.at[pop1, pop2]) else (fst_matrix.at[pop1, pop2] + fst) / 2
                fst_matrix.at[pop2, pop1] = fst_matrix.at[pop1, pop2]

    # Fill the diagonal elements with the value 0
    np.fill_diagonal(fst_matrix.values, 0)
    

    # Create the population matrix that can be displayed in html
    pop_matrix = fst_matrix.to_html(classes='fst-matrix')

    # Create the population matrix that can be displayed in text
    soup = BeautifulSoup(pop_matrix, 'html.parser')
    rows = soup.find_all('tr')
    text = ""
    for row in rows:
        cells = row.find_all(['th', 'td'])
        row_text = '\t'.join(cell.get_text() for cell in cells)
        text += row_text + '\n'

    # Use the session package to pass the text variable to the next function
    session['text'] = text

    # Create the Pandas dataframe for the Fst matrix
    df = pd.DataFrame(fst_matrix)

    # Plot Heatmap
    plt.figure(figsize=(10, 10))
    sns.heatmap(df, cmap='viridis', annot=True, linewidths=.5, cbar_kws={'label': 'Genetic Differentiation'})
    plt.title('Population Matrix')
    plt.xlabel('Population')
    plt.ylabel('SNP_ID')
    
    # Store the plot in a bytes buffer, encode in base64
    img = io.BytesIO()
    plt.savefig(img, format='png', bbox_inches='tight')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode('utf-8')
    return render_template('pop_matrix.html', pop_matrix=pop_matrix, plot_url=plot_url)  # Use pop_matrix.html as template

# Create the path to download the text file for the population matrix
@app.route('/allele&genotype_frequencies-clinical_relevance/pop_matrix/download')
def download():
    text = session.get('text', [])
    response = Response(text, mimetype='text/plain')  # Use Response function to create text file
    response.headers["Content-Disposition"] = "attachment; filename=pop_matrix.txt"  # Download the text file as an attachment
    session.pop('text', None)
    return response

# Start the web server
if __name__ == '__main__':
    app.run(debug=True)
