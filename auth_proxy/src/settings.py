from sqlalchemy.engine import URL, make_url
from starlette.config import Config


config = Config()

RELOAD = config('RELOAD', cast=bool, default=False)

DATABASE = {
    'DB_DRIVER_ASYNC': config('DB_DRIVER_ASYNC', default='postgresql+asyncpg'),
    'DB_DRIVER_SYNC': config('DB_DRIVER_SYNC', default='postgresql'),
    'DB_NAME': config('DB_NAME'),
    'DB_USER': config('DB_USER'),
    'DB_PASSWORD': config('DB_PASSWORD'),
    'DB_HOST': config('DB_HOST'),
    'DB_PORT': config('DB_PORT', cast=int),
}
DB_DSN = config(
    'DB_DSN',
    cast=make_url,
    default=URL.create(
        drivername=DATABASE['DB_DRIVER_ASYNC'],
        username=DATABASE['DB_USER'],
        password=DATABASE['DB_PASSWORD'],
        host=DATABASE['DB_HOST'],
        port=DATABASE['DB_PORT'],
        database=DATABASE['DB_NAME'],
    ),
)
DB_DSN_ALEMBIC = config(
    'DB_DSN_ALEMBIC',
    cast=make_url,
    default=URL.create(
        drivername=DATABASE['DB_DRIVER_SYNC'],
        username=DATABASE['DB_USER'],
        password=DATABASE['DB_PASSWORD'],
        host=DATABASE['DB_HOST'],
        port=DATABASE['DB_PORT'],
        database=DATABASE['DB_NAME'],
    ),
)
