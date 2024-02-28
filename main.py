from fastapi import FastAPI
from contextlib import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware

from src.api.routers.user import router as user_router
from src.database.database import create_tables, delete_tables


app = FastAPI()

origins = [
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS", "DELETE", "PATCH", "PUT"],
    allow_headers=["*"],
)


@asynccontextmanager
async def lifespan(app: FastAPI):
    # await delete_tables()
    # print('БД очищена')
    await create_tables()
    print('БД подключена')
    yield
    print('выключение')


# app = FastAPI(lifespan=lifespan)
app.include_router(user_router)
