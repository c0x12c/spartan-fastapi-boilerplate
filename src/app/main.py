from fastapi import FastAPI
from src.app.routers import user_router, token_router
from src.adapters import orm

app = FastAPI()
orm.start_mappers()


app.include_router(user_router, prefix="/api")
app.include_router(token_router, prefix="/api")
