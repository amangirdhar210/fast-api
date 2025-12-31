from fastapi import APIRouter
from ..services.users import UserService
userRouter= APIRouter()


@userRouter.get("/users")
async def get_all_users():
    return UserService.get_all_users()
    
