from typing import Optional

from pydantic import BaseModel


class ProfileSchema(BaseModel):
    id: Optional[int] = None
    username: str
    email: str
    first_name: str
    last_name: str
    password: str

    class Config:
        orm_mode = True


class LoginSchema(BaseModel):
    username: str
    password: str
