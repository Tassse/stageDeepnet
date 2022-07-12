from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import csv
import json
from pathlib import Path
from fastapi.responses import FileResponse

path_capteur_db = Path("/app/capteurs-testlaurene.csv")

app = FastAPI()

class Item(BaseModel):
    light:int
    temperature:float
    moisture:int
    conductivity:int
    battery:int
    timestamp:str

#itemJson = {"light": 0, "temperature": 21.4, "moisture": 18, "conductivity": 373, "battery": 63, "timestamp": "2022-06-30 08:34:59"}
  
@app.get("/items/{itemJson}")
async def update_df(itemJson : str):
    item = json.loads(itemJson)
    df = pd.json_normalize((item))
    #return str(fileObj.absolute())
    df.to_csv(path_capteur_db,mode='a',header=not(path_capteur_db.is_file()))

@app.get("/fichier")
async def fichier():
    return FileResponse(path_capteur_db)
