from fastapi import FastAPI, APIRouter, status
from pydantic import BaseModel
from fast_project.models.models import LoginRequest, SignupRequestBody
from fast_project.services.users import UserService

authRouter = APIRouter()


@authRouter.post("/login")
async def login(req_body: LoginRequest):
    print(req_body)


@authRouter.post("/signup")
async def signup(req_body: SignupRequestBody):
    print(req_body)
    UserService.signup(req_body)


