# app.py
# Blokk 1 - Starter Flask-appen

from flask import Flask # importerer Flask

app = Flask (__name__) # Lager appen

if __name__ == "__main__":
    app.run(debug=True) # Starter serveren

