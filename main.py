from fastapi import FastAPI

# Exposing and Creating the web application
app = FastAPI()

# Health Check for the Application
@app.get("/health")
async def health():
    return {"status": "ok"}