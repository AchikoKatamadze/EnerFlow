from fastapi import APIRouter
router=APIRouter(prefix="/prediction",tags=["Prediction"])

@router.get("/")
def predict():
    return {"generation_mw":620,"risk":"LOW"}
