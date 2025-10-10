# app.py - Flask-ruter for kantineprosjektet 
# Blokk 1 - Starter Flask-appen

from flask import Flask, render_template  # for å bruke HTML-templates

app = Flask(__name__) # Lager appen


# Blokk 6: Felles data (lett å bruke flere steder)
UKENS_MENY = [
    "Mandag: Pizza",
    "Tirsdag: Taco",
    "Onsdag: Pasta",
    "Torsdag: Kylling",
    "Fredag: Pizza",
]

VARER = [
    "Bagett (45 kr)",
    "Kaffe (20 kr)",
    "Smoothie (35 kr)",
    "Salat (50 kr)",
]

#Rute til forsiden /
@app.route("/")
def index():
    return render_template("index.html")  # viser templates/index.html

# Rute: /meny – ukens meny
@app.route("/meny")                             
def meny():
    return render_template(
        "meny.html",       # bruker templates/meny.html
        ukens_meny=UKENS_MENY   # sender Python-lista til Jinja
    )
# Blokk 4: /varer bruker felles listen
@app.route("/varer")
def varer_side():
    return "Faste varer:\n" + "\n".join(f"- {v}" for v in VARER)

# Blokk 5 - Legger til kontakt-siden
@app.route("/kontakt")
def kontakt():
    return "Kontakt oss på bislett@akademiet.no - Telefon: 93 07 79 90"

# Blokk 9: enkel 404-side
@app.errorhandler(404)
def not_found(_):
    return "404 - Siden ble ikke funnet. Prøv /meny, /varer eller /kontakt.", 404


if __name__ == "__main__":
    app.run(debug=True) # slår på debug når du tester, slår av når du er ferdig

