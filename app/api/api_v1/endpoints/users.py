

from fastapi import APIRouter

router = APIRouter()

@router.get("")
async def users():
    return {"message": "Get Users!"}
