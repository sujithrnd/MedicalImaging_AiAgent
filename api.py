# api.py
import os
import shutil
from fastapi import FastAPI, UploadFile, File, HTTPException
from PIL import Image as PILImage
from agno.agent import Agent
from agno.media import Image as AgnoImage
from medical_fastapi import medical_agent, query





app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}



# Function to analyze medical image
# ---- FASTAPI ENDPOINT ----
@app.post("/analyze")
async  def analyze_medical_image(file: UploadFile = File(...)):
    if file.content_type not in ["image/png", "image/jpeg"]:
        raise HTTPException(status_code=400, detail="Invalid image type")

    temp_path = f"temp_{file.filename}"
    print("Saving uploaded file to", temp_path)
    with open(temp_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    try:
        report = analyze_medical_image(temp_path)
        return {"report": report}
    finally:
        os.remove(temp_path)