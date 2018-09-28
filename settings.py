from decouple import config

DEBUG = config('DEBUG', default=False, cast=bool)
SQLALCHEMY_DATABASE_URI = config('SQLALCHEMY_DATABASE_URI')
