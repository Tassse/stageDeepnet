import pandas as pd
import json


itemJson= {"light": 0, "temperature": 20, "moisture": 15, "conductivity": 374, "battery": 63, "timestamp": "2022-06-30 06:58:53"}

df = pd.json_normalize((itemJson))
df.to_csv('fichier.csv', mode='a', header=False)