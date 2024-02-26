from typing import Annotated
from fastapi import APIRouter, Depends

from src.api.response_models.schem_user import SchemCreateUser, SchemUserId
from src.database.repository.user import UserRepository


router = APIRouter(
    prefix='/users',
    tags=['Пользователи']
)


@router.post('')
async def create_user(user: Annotated[SchemCreateUser, Depends()]) -> SchemUserId:
    user_id = await UserRepository.create_user(user)
    return {'ok': True, 'user_id': user_id}


@router.get('')
async def get_all_user():
    users = await UserRepository.get_all_user()
    return {'users': users}