from fastapi import APIRouter

router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"]
)


@router.get("/")
def get_dashboard():
    return {
        "current_generation": 540,
        "predicted_generation": 615,
        "reservoir_level": 81,
        "river_flow": 95.2,
        "winter_risk": "LOW",
        "peak_hour": "20:00",
        "recommendations": [
            "Save water until evening peak",
            "Keep reservoir above 80%",
            "Use turbine #2"
        ]
    }