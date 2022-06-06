from fastapi import APIRouter
from app.services.bull import BullService

router = APIRouter()
bs = BullService()

@router.get("/bull/{id}", tags=["bull"])
async def get_bull(id: str):
    global_id = bs.get_global_id(id=id)
    return bs.get_bull(global_id=global_id)

@router.get("/bulls/{breed_group}/{marketing_group}", tags=["bulls"])
async def get_marketed_bulls(breed_group: str, marketing_group: str):
    return bs.get_marketed_bulls(breed_group=breed_group, marketing_groups=marketing_group)