from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

import base64
from io import BytesIO
from PIL import Image

app = FastAPI()


class B64(BaseModel):
    image_b64: str

def mock_model(img):
    return img.size

@app.post("/plant/")
def analyse_plant(data: B64):
    image_b64 = data.image_b64
    image = bytes(image_b64, "ascii")
    image = Image.open(BytesIO(base64.b64decode(image)))
    analyse = mock_model(image)
    return {"healthy": analyse}
