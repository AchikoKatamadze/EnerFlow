from fastapi import APIRouter

from ..services.weather_services import WeatherService

router = APIRouter(
    prefix="/weather",
    tags=["Weather"]
)


@router.get("/")
def weather():

    return WeatherService.get_weather(
        42.52,
        43.15
    )