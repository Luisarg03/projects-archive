from fastapi import APIRouter, Depends
from modules.security import get_current_user

router = APIRouter()


@router.get("/user/me")
def read_users_me(current_user: str = Depends(get_current_user)):
    return {"username": current_user}
