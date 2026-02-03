from fastapi import FastAPI, File, UploadFile, Header, HTTPException
from fastapi.responses import JSONResponse

app = FastAPI(title="AI Voice Detection API")

API_KEY = "hcl_guvi_2026_key"  # keep this same for submission


@app.post("/detect-voice")
async def detect_voice(
    file: UploadFile = File(...),
    x_api_key: str = Header(None)
):
    # 1. API Key validation
    if x_api_key != API_KEY:
        raise HTTPException(
            status_code=401,
            detail="Invalid API Key"
        )

    # 2. File validation
    if not (file.filename.endswith(".wav") or file.filename.endswith(".mp3")):
        raise HTTPException(
            status_code=400,
            detail="Only .wav or .mp3 files are allowed"
        )

    # 3. Dummy detection logic (safe placeholder)
    prediction = "AI"
    confidence = 0.85

    # 4. Proper JSON response
    return JSONResponse(content={
        "prediction": prediction,
        "confidence": confidence
    })
