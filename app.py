# app.py
# Blokk 1 - Starter Flask-appen

from flask import Flask # importerer Flask

app = Flask (__name__) # Lager appen

# Blokk 2 - Legger til forsiden
@app.route("/") 
def index():
    return "Hjem - Flask kjører! Prøv /meny, /varer eller /kontakt."

if __name__ == "__main__":
    app.run(debug=True) # Starter serveren

