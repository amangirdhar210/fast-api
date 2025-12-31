from pydantic import BaseModel, Field, EmailStr
from fast_project.utils.password import generate_pwd_hash

class LoginRequest(BaseModel):
    email: EmailStr = Field(min_length=10)
    password: str = Field(min_length=8, max_length=20)


class SignupRequestBody(BaseModel):
    first_name: str = Field(min_length=2, max_length=10)
    middle_name: str | None = None
    last_name: str = Field(min_length=2, max_length=10)
    email: EmailStr = Field(min_length=7, max_length=20)
    password: str = Field(min_length=8, max_length=20)


class User:
    first_name: str
    middle_name: str | None = None
    last_name: str
    email: str
    password_hash: str

    def __init__(self, first_name,last_name,email,password,middle_name=None):
        self.first_name= first_name
        self.middle_name= middle_name
        self.last_name= last_name
        self.email= email
        self.password_hash= generate_pwd_hash(password)
