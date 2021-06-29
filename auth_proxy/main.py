import uvicorn
from fastapi import FastAPI

from src.db import engine, Base
from src.routes import router


app = FastAPI()
app.include_router(router)


if __name__ == '__main__':

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

    uvicorn.run('main:app', host='0.0.0.0', port=8000)
