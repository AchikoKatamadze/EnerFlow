from fastapi import APIRouter
router=APIRouter(prefix="/river",tags=["River"])

@router.get("/")
def get_river():
    return {"flow_rate":95.2,"reservoir":81}
