import requests
import sys
import subprocess

if len(sys.argv)==1:
    dodo=120
else:
    dodo=sys.argv[1]
    
data=subprocess.call("miFlora.py", shell=True)
#requete = 'http://127.0.0.1:8000/items/'+data
#r=requests.get(requete)
#time.sleep(dodo)
print(dodo)
print(data)
