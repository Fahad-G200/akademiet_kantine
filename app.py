from flask import Flask, render_template 

app = Flask(__name__)




# Lager en rute for forsiden slik at brukeren ser satrtsiden først 
@app.route('/') 
def index():
    return render_template('index.html') # Viser startsiden (index.html) 


# Ukens meny
# Viser en liste med retter for hver dag

@app.route("/meny")
def meny():
    ukens_meny = [
        "Mandag: Pizza",
        "Tirsdag: Taco",
        "Onsdag: Pasta",
        "Torsdag: Kylling",
        "Fredag: Pizza"
    ]
    return render_template("meny.html", ukens_meny=ukens_meny)




# Vareside
# Viser faste varer som alltid selges i kantina
@app.route("/varer")
def varer():
    varer = ["Bagett (45 kr)", "Kaffe (20 kr)", "Smoothie (35 kr)", "Salat (50 kr)"]
    return render_template("varer.html", varer=varer)



