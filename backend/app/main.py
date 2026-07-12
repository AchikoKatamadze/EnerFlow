from fastapi import FastAPI

from app.database import Base, engine
from app.models.hydro_station import HydroStation

from app.api.weather import router as weather_router
from app.api.river import router as river_router
from app.api.prediction import router as prediction_router
from app.api.dashboard import router as dashboard_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="EnerFlow API")

app.include_router(weather_router)
app.include_router(river_router)
app.include_router(prediction_router)
app.include_router(dashboard_router)

@app.get("/")
def root():
    return {"status": "running"}