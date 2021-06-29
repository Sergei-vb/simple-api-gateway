from sqlalchemy.engine import URL, make_url
from starlette.config import Config


config = Config()


DATABASE = {
    'DB_DRIVER_ASYNC': config('DB_DRIVER_ASYNC', default='postgresql+asyncpg'),
    'DB_DRIVER_SYNC': config('DB_DRIVER_SYNC', default='postgresql'),
    'DB_NAME': config('DB_NAME', default='auth'),
    'USER': config('DB_USER'),
    'PASSWORD': config('DB_PASSWORD'),
    'HOST': config('DB_HOST', default='postgresdb'),
    'PORT': config('DB_PORT', cast=int, default=5432),
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
