from fastapi import FastAPI

app = FastAPI(title="Vision Change Story API")

@app.get("/health")
def health():
    return {"status": "ok"}