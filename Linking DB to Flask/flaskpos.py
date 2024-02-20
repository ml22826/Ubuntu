"""FLASK file which allows to connect to the database and get information on SNPs based on chromosome position """

from flask import Flask, render_template, request
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

@app.route('/')
def index():
    return 'Welcome to the page'

@app.route('/snp_range')
def snp_range():
    #start and end positions from query parameters
    pop_group = request.args.get('pop')
    start_pos = request.args.get('start', type=int)
    end_pos = request.args.get('end', type=int)

    
    #validation to ensure both start and end positions are provided and valid
    if start_pos is None or end_pos is None:
        return 'Both start and end positions must be provided.', 400

    config = {
        'user': 'root',
        'password': 'xxx',  
        'host': 'localhost',
        'database': 'ubuntu4',
    }
    SNP_data = []

    try:
        db = mysql.connector.connect(**config)
        cursor = db.cursor()

        query = """
           SELECT sni.*,af.ALT_FRQ,AF.REF_FRQ
            FROM snp_info 
	            AS sni
            JOIN allele_frequencies 
	            AS af 
	            ON af.SNP=sni.SNP_ID
            WHERE af.POP=%s AND sni.POS BETWEEN %s AND %s;
        """
        cursor.execute(query, (pop_group,start_pos, end_pos))
        SNP_data = cursor.fetchall()

    except mysql.connector.Error as err:
        print(f"Something went wrong: {err}")
    finally:
        if cursor:
            cursor.close()
        if db and db.is_connected():
            db.close()

    return render_template('pop.html', results=SNP_data)

if __name__ == '__main__':
    app.run(debug=True)
