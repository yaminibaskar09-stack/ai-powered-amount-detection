from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
import shutil
import os

from app.ocr import extract_text_from_image
from app.extract import extract_raw_tokens
from app.normalize import normalize_tokens
from app.classify import classify_amounts

app = FastAPI(
    title="AI-Powered Amount Detection API",
    description="Detects and classifies monetary amounts from text or images",
    version="1.0.0"
)


class TextRequest(BaseModel):
    text: str



@app.post("/detect/text", tags=["Text Detection"])
async def detect_from_text(request: TextRequest):
    text = request.text

    raw_tokens = extract_raw_tokens(text)
    normalized = normalize_tokens(raw_tokens)
    classified = classify_amounts(text, normalized)

    return {
        "currency": "INR",
        "amounts": classified,
        "status": "ok"
    }



# Image-based Detection

@app.post("/detect/image", tags=["Image Detection"])
async def detect_from_image(image: UploadFile = File(...)):
    temp_path = f"temp_{image.filename}"

    with open(temp_path, "wb") as buffer:
        shutil.copyfileobj(image.file, buffer)

    text = extract_text_from_image(temp_path)
    os.remove(temp_path)

    raw_tokens = extract_raw_tokens(text)
    normalized = normalize_tokens(raw_tokens)
    classified = classify_amounts(text, normalized)

    return {
        "currency": "INR",
        "amounts": classified,
        "status": "ok"
    }
