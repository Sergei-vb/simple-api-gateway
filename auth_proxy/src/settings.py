from sqlalchemy.engine import URL, make_url
from starlette.config import Config


config = Config()

RELOAD = config('RELOAD', cast=bool, default=False)

DATABASE = {
    'DB_DRIVER_ASYNC': config('DB_DRIVER_ASYNC', default='postgresql+asyncpg'),
    'DB_DRIVER_SYNC': config('DB_DRIVER_SYNC', default='postgresql'),
    'DB_NAME': config('DB_NAME'),
    'USER': config('DB_USER'),
    'PASSWORD': config('DB_PASSWORD'),
    'HOST': config('DB_HOST'),
    'PORT': config('DB_PORT', cast=int),
}
DB_DSN = config(
    'DB_DSN',
    cast=make_url,
    default=URL.create(
        drivername=DATABASE['DB_DRIVER_ASYNC'],
        username=DATABASE['USER'],
        password=DATABASE['PASSWORD'],
        host=DATABASE['HOST'],
        port=DATABASE['PORT'],
        database=DATABASE['DB_NAME'],
    ),
)
DB_DSN_ALEMBIC = config(
    'DB_DSN',
    cast=make_url,
    default=URL.create(
        drivername=DATABASE['DB_DRIVER_SYNC'],
        username=DATABASE['USER'],
        password=DATABASE['PASSWORD'],
        host=DATABASE['HOST'],
        port=DATABASE['PORT'],
        database=DATABASE['DB_NAME'],
    ),
)
