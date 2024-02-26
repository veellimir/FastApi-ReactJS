from pydantic import BaseModel
from typing import Optional


class SchemCreateUser(BaseModel):
    login: str
    name: str
    surname: str
    email: str


class SchemUser(SchemCreateUser):
    id: int


class SchemUserId(BaseModel):
    ok: bool = True
    user_id: int