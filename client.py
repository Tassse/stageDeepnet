import requests

requete = 'http://127.0.0.1:8000/items/'+'{"light": 0, "temperature": 21.4, "moisture": 18, "conductivity": 373, "battery": 63, "timestamp": "2022-06-30 08:34:59"}'
#requete = 'http://127.0.0.1:8000/items/'+miflora.py (il faudra probablement modifier le programme pour que ça marche mais c'est l'idée)

r=requests.get(requete)