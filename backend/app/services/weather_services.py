import requests

from ..config import settings


class WeatherService:

    @staticmethod
    def get_weather(lat, lon):

        response = requests.get(

            settings.WEATHER_API,

            params={

                "latitude": lat,

                "longitude": lon,

                "current":

                    "temperature_2m,relative_humidity_2m"

            }

        )

        return response.json()