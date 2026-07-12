from fastapi import APIRouter

router = APIRouter(
    prefix="/prediction",
    tags=["Prediction"]
)


@router.get("/")
def prediction():

    return {

        "expected_generation": 615,

        "winter_risk": "LOW",

        "recommendation": "Save water until evening peak."
    }