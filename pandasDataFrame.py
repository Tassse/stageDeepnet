
import pandas as pd

data = {"light": 0, "temperature": 28.4, "moisture": 3, "conductivity": 0, "battery": 100, "timestamp": "2022-06-23 14:29:33"}
data2 = {"light": 4, "temperature": 24.9, "moisture": 2, "conductivity": 0, "battery": 100, "timestamp": "2022-06-27 14:44:58"}

filecontent = """
{"light": 314, "temperature": 27.0, "moisture": 2, "conductivity": 0, "battery": 100, "timestamp": "2022-06-27 15:30:59"}
"""
filecontent = json2dict(filecontent) --> json
filecontent["light"]
datFrame = pd.Series(data)

print(datFrame)
