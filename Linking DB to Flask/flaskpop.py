"""FLASK file which allows to connect to the database and get information on SNPs based on pop names """

from flask import Flask, render_template
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

@app.route('/')
def index():
    return 'Welcome to Ubuntu page'

#define a route called 'pop' that accepts a population name parameter
@app.route('/pop/<pop_name>')
def pop(pop_name):
    #connection to db
    config = {
        'user': 'root',
        'password': 'xx',  
        'host': 'localhost',
        'database': 'ubuntu4',
    }
    SNP_data=[]
    
    #in case the user is giving out a list 
    if not isinstance(pop_name, list):
        pop_name = [pop_name]
    
    try:
        #database connection
        db = mysql.connector.connect(**config)
        cursor = db.cursor()
        
        
        for pop in pop_name:
            pop=pop.upper()
            query = """
          SELECT gr.*, af.ALT_FRQ,af.REF_FRQ
            FROM arg gr
            JOIN allele_frequencies af ON af.POS = gr.POS
            WHERE af.POP = %s;

            
            """
            cursor.execute(query, (pop,))
            rows = cursor.fetchall()
            
            if rows:
                print(f"Results for {pop}:")
                for row in rows:
                    SNP_data.append(row)
            return render_template('pop.html',results=SNP_data)
            # else:
            #     print(f"No results found for {pop}.")
    
    except mysql.connector.Error as err:
        print(f"Something went wrong: {err}")
    
    finally:
        if cursor is not None:
            cursor.close()
        if db is not None and db.is_connected():
            db.close()


if __name__ == '__main__':
    app.run(debug=True)