from flask import Flask, render_template 

app = Flask(__name__)




# Lager en rute for forsiden slik at brukeren ser satrtsiden først 
@app.route('/') 
def index():
    return render_template('index.html') # Viser startsiden (index.html) 


