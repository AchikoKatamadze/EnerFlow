from fastapi import APIRouter
router=APIRouter(prefix="/weather",tags=["Weather"])

@router.get("/")
def get_weather():
    return {"temperature":14,"humidity":60}
