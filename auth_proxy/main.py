import uvicorn
from fastapi import FastAPI

from src.routes import router
from src import settings


app = FastAPI(title='Auth proxy')
app.include_router(router, tags=['auth'])


if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=8000, reload=settings.RELOAD)
