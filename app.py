from fastapi import FastAPI, File, UploadFile
import easyocr
from PIL import Image
import numpy as np
import io

app = FastAPI()
reader = easyocr.Reader(['fr', 'en'])

@app.post("/ocr")
async def ocr_api(file: UploadFile = File(...)):
    img_bytes = await file.read()
    img = Image.open(io.BytesIO(img_bytes))
    img_np = np.array(img)

    result = reader.readtext(img_np, detail=0)
    return {"text": " ".join(result)}
