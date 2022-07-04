import requests
import sys
import miFlora.py

if len(sys.argv==1):
    dodo=120
else:
    dodo=sys.argv[1]
    
data=miFlora.py
requete = 'http://127.0.0.1:8000/items/'+data
r=requests.get(requete)
#time.sleep(dodo)
print(dodo)
