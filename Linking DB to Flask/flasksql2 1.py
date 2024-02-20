"""FLASK file which allows to connect to the database and get information on SNPs based on gene names """

from flask import Flask, render_template
import mysql.connector
from mysql.connector import Error
from genes_function import query_genes

app = Flask(__name__)

@app.route('/')
def index():
    return 'Welcome to Ubuntu page'

#define a route called 'gene' that accepts a gene name parameter
@app.route('/gene/<gene_name>')
def gene(gene_name):
    #connection to db
    config = {
        'user': 'root',
        'password': 'xxxx',  
        'host': 'localhost',
        'database': 'ubuntu4',
    }
    SNP_data=[]
    
    #in case the user is giving out a list 
    if not isinstance(gene_name, list):
        gene_name = [gene_name]
    
    try:
        #database connection
        db = mysql.connector.connect(**config)
        cursor = db.cursor()
        
        
        for gene in gene_name:
            gene=gene.upper()
            query = """
            WITH gene_range AS (
                SELECT POS_START, POS_END 
                FROM genes 
                WHERE GENE = %s
            )
            SELECT si.* 
            FROM snp_info si, gene_range gr 
            WHERE si.POS BETWEEN gr.POS_START AND gr.POS_END;
            """
            cursor.execute(query, (gene,))
            rows = cursor.fetchall()
            
            if rows:
                print(f"Results for {gene}:")
                for row in rows:
                    SNP_data.append(row)
            return render_template('gene.html',results=SNP_data)
            # else:
            #     print(f"No results found for {gene}.")
    
    except mysql.connector.Error as err:
        print(f"Something went wrong: {err}")
    
    finally:
        if cursor is not None:
            cursor.close()
        if db is not None and db.is_connected():
            db.close()


if __name__ == '__main__':
    app.run(debug=True)