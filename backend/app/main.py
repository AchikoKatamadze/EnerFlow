from fastapi import FastAPI

app = FastAPI(title="EnerFlow API")

@app.get("/")
def root():
    return {"status":"running","project":"EnerFlow"}
