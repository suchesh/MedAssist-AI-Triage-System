from fastapi import FastAPI, File, UploadFile, Form
from fastapi.responses import HTMLResponse, PlainTextResponse
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse
from assistant import medical_Assistant


app = FastAPI()

# Mount static folder
app.mount("/static", StaticFiles(directory="static"), name="static")

# Serve index.html
@app.get("/", response_class=HTMLResponse)
async def get_index():
    with open("templates/index.html", "r", encoding="utf-8") as f:
        return f.read()

# Serve patient.html
@app.get("/patient.html", response_class=HTMLResponse)
async def get_patient():
    with open("templates/patient.html", "r", encoding="utf-8") as f:
        return f.read()

# API endpoint
@app.post("/fetch-ai-analysis")
async def fetch_ai_analysis(
    text_data: str = Form(...),
    pdf_file: UploadFile = File(None)
):
    print("Received text data:", text_data)
    response = medical_Assistant(text_data, pdf_file.file if pdf_file else None)
    return JSONResponse(content=response)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
