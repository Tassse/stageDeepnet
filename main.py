from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import csv
import json
from pathlib import Path
#from fastapi.responses import FileResponse
from flask import Flask

path_capteur_db = Path("/Users/thais/PycharmProjects/pythonDeepnetAPI/stageDeepnet/capteurs-testthais.csv")

#app = FastAPI()

app = Flask(__name__)

class Item(BaseModel):
    light:int
    temperature:float
    moisture:int
    conductivity:int
    battery:int
    timestamp:str

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
    return FileResponse(path_capteur_db)


#Version FastAPI

"""@app.get("/items/{itemJson}")
async def update_df(itemJson : str):
    item = json.loads(itemJson)
    df = pd.json_normalize((item))
    #return str(fileObj.absolute())
    df.to_csv(path_capteur_db,mode='a',header=not(path_capteur_db.is_file()))
    #return str(path_capteur_db.absolute())

@app.get("/fichier")
async def fichier():
    return FileResponse(path_capteur_db)"""
