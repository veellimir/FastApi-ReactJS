from fastapi import FastAPI
from contextlib import asynccontextmanager

from src.api.routers.user import router as user_router


app = FastAPI()


@asynccontextmanager
async def lifespan(app: FastAPI):
    # await delete_tables()
    print('БД очищена')
#     await create_tables()
    print('БД готова')
    yield
    print('выключение')


app = FastAPI(lifespan=lifespan)
app.include_router(user_router)