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

#itemJson = {"light": 0, "temperature": 21.4, "moisture": 18, "conductivity": 373, "battery": 63, "timestamp": "2022-06-30 08:34:59"}
  
@app.get("/items/{itemJson}")
async def update_df(itemJson : str):
    item = json.loads(itemJson)
    df = pd.json_normalize((item))
    fileName = r"./capteurs.csv"
    fileObj = Path(fileName)
    df.to_csv('capteurs.csv',mode='a',header=not(fileObj.is_file()))
