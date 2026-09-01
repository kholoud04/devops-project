from fastapi import FastAPI

app = FastAPI(title="DevOps Demo App")

@app.get("/")
def read_root():
    return {"status": "success", "message": "DevOps Pipeline is Working!", "version": "v2.0.0"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}