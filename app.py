# app.py
# Første steg i kantinaprosjektet: minimal Flask-app
# Jeg starter bare serveren og legger inn en rute ( forsiden) 
from flask import Flask # importerer flask-rammeverket 
app = Flask(__name__) # lager en Flask-app