from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )

    DATABASE_URL: str = Field(default="sqlite:///./enerflow.db")
    WEATHER_API: str = Field(default="https://api.open-meteo.com/v1/forecast")


settings = Settings()