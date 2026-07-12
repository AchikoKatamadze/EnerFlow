from fastapi import APIRouter

router = APIRouter(
    prefix="/river",
    tags=["River"]
)


@router.get("/")
def river():

    return {
        "flow_rate": 96.2,
        "water_level": 74,
        "reservoir": 81
    }