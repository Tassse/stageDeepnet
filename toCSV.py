import csv
import json

file = open('/home/stage/data.txt', "r")
lines = file.readlines()
file.close()

toCSV=[]
for line in lines:
    line = line.replace("\n","")
    if line != "" and "Retrying" not in line:
        line=json.loads(line)
        toCSV.append(line)
keys = toCSV[0].keys()
with open('capteur.csv', 'w', newline='') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(toCSV)

