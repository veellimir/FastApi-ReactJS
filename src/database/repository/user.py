from sqlalchemy import select

from src.database.database import new_session, UserOrm
from src.api.response_models.schem_user import SchemCreateUser


class UserRepository:
    @classmethod
    async def create_user(cls, data: SchemCreateUser) -> int:
        async with new_session() as session:
            user_dict = data.model_dump()
            user = UserOrm(**user_dict)
            session.add(user)

            await session.flush()
            await session.commit()
            return user.id

    @classmethod
    async def get_all_user(cls):
        async with new_session() as session:
            query = select(UserOrm)
            result = await session.execute(query)
            user_models = result.scalars().all()

            return user_models
