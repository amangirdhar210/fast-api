from fastapi import FastAPI

from fast_project.controllers.auth import authRouter
from fast_project.controllers.notes import notesRouter
from fast_project.controllers.users import userRouter

app = FastAPI()

app.include_router(authRouter)
app.include_router(notesRouter)
app.include_router(userRouter)
