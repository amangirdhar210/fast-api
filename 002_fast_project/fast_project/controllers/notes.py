from pydantic import BaseModel
from fastapi import APIRouter, status

notesRouter = APIRouter()


@notesRouter.get("/user", status_code=status.HTTP_200_OK)
async def function1():
    return {"m": "user"}
