import pandas as pd
import csv
import json
from pathlib import Path
from flask import Flask
import flask

path_capteur_db = Path("database.csv")

app = Flask(__name__)

#itemJson = {"light": 0, "temperature": 21.4, "moisture": 18, "conductivity": 373, "battery": 63, "timestamp": "2022-06-30 08:34:59"}


#Version Flask

@app.route("/items/<string:itemJson>")
def update_df(itemJson):
    item = json.loads(itemJson)
    df = pd.json_normalize((item))
    #return str(fileObj.absolute())
    df.to_csv(path_capteur_db,mode='a',header=not(path_capteur_db.is_file()))
    return str(path_capteur_db.absolute())

@app.route("/fichier")
def fichier():
    return flask.send_file(path_capteur_db)
