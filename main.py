from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import csv
import json

app = FastAPI()

class Item(BaseModel):
    light:int
    temperature:float
    moisture:int
    conductivity:int
    battery:int
    timestamp:str


@app.get("files/{file_path}")
async def stockage():
    file = open('file_path', "r")
    lines = file.readlines()
    file.close()

    toCSV = []
    for line in lines:
        line = line.replace("\n", "")
        if line != "":
            line = json.loads(line)
            toCSV.append(line)
    keys = toCSV[0].keys()
    with open('capteur.csv', 'w', newline='') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(toCSV)

itemJson = {"light": 0, "temperature": 21.4, "moisture": 18, "conductivity": 373, "battery": 63, "timestamp": "2022-06-30 08:34:59"}

@app.get("/itemJson")
async def create_item(itemJson : str):
    item = json.loads(itemJson)
    df = pd.json_normalize((item))
    df.to_csv("capteurs.csv")

