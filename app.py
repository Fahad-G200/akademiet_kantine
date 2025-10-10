# app.py - Flask-ruter for kantineprosjektet 
# Blokk 1 - Starter Flask-appen

from flask import Flask # importerer Flask

app = Flask(__name__) # Lager appen

# Blokk 2 - Legger til forsiden
@app.route("/") 
def index():
    return "Hjem - Flask kjører! Prøv /meny, /varer eller /kontakt."

# Blokk 3: legger til /meny (bruker liste + join)
@app.route("/meny")
def meny():
    ukens_meny = [
        "Mandag: Pizza",
        "Tirsdag: Taco",
        "Onsdag: Pasta",
        "Torsdag: Kylling",
        "Fredag: Pizza",
    ]
    return "Ukens meny:\n" + "\n".join(ukens_meny)

# Blokk 4 - Legger til varer-siden
@app.route("/varer")
def varer_side():
    return (
        "Faste varer:\n"
        "- Bagett (45 kr)\n"
        "- Kaffe (20 kr)\n"
        "- Smoothie (35 kr)\n"
        "- Salat (50 kr)"
    )

# Blokk 5 - Legger til kontakt-siden
@app.route("/kontakt")
def kontakt():
    return "Kontakt oss på bislett@akademiet.no - Telefon: 93 07 79 90"
if __name__ == "__main__":
    app.run(debug=True) # slår på debug når du tester, slår av når du er ferdig

