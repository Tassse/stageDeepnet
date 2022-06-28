import requests
import base64
from io import BytesIO
from PIL import Image

lien = "image2.png"
with open(lien, "rb") as image_file:
    data = image_file.read()

payload = {"image_b64" : str(base64.b64encode(data), "ascii")}

r = requests.post('http://192.168.105.214:8000/plant/', json=payload)
r
