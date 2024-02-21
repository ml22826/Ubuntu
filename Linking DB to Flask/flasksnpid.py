from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

@app.route('/')
def index():
    return 'Welcome to Ubuntu page'

@app.route('/snps')
def snps():
    snp_ids = request.args.get('ids')
    pop_group = request.args.get('pop')
    
    if not snp_ids or not pop_group:
        return 'You need to provide both SNP ids and population groups.', 400
    
    snp_id_list = snp_ids.split(',')
    pop_list = pop_group.split(',')
    
    config = {
        'user': 'root',
        'password': 'Singapour9802!',  
        'host': 'localhost',
        'database': 'ubuntu4',
    }
    SNP_data = []
    
    try:
        db = mysql.connector.connect(**config)
        cursor = db.cursor()

        #placeholders for the query
        ids_placeholders = ', '.join(['%s'] * len(snp_id_list))
        pop_placeholders = ', '.join(['%s'] * len(pop_list))
        
        #all parameters into a single tuple for the execute method
        params = tuple(snp_id_list + pop_list)
        
        query = f"""
        SELECT DISTINCT sni.*, af.ALT_FRQ, af.REF_FRQ,af.POP
        FROM snp_info AS sni
        JOIN allele_frequencies AS af ON af.SNP = sni.SNP_ID
        WHERE sni.SNP_ID IN ({ids_placeholders}) AND af.POP IN ({pop_placeholders});
        """
        
        cursor.execute(query, params)
        SNP_data = cursor.fetchall()
    
    except mysql.connector.Error as err:
        return f"Something went wrong: {err}", 500
    
    finally:
        if cursor:
            cursor.close()
        if db and db.is_connected():
            db.close()
    
    return render_template('pop.html', results=SNP_data)

if __name__ == '__main__':
    app.run(debug=True)
