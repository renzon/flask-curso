import pytest
import sqlalchemy
from sqlalchemy.exc import OperationalError, ProgrammingError

import settings
from app_factory import create_app
from ext.db import db as slq_alchemy_db

test_db = 'testdb'
settings.SQLALCHEMY_DATABASE_URI = f'{settings.DATABASE_LOCATION}/{test_db}'


@pytest.fixture(scope='session')
def app():
    app = create_app(settings)
    return app


@pytest.fixture(scope='session')
def _create_db(app):
    postgres_database = f'{settings.DATABASE_LOCATION}/postgres'
    engine = sqlalchemy.create_engine(postgres_database)
    try:
        conn = engine.connect()
    except OperationalError:
        print(f'Not able to connect with {postgres_database}')
    else:
        try:
            conn.execute('commit')
            conn.execute(f'DROP DATABASE {test_db}')
        except ProgrammingError:
            print("Database already cleaned")
        conn.execute('commit')
        conn.execute(f'CREATE DATABASE {test_db}')
        conn.close()
    db_url = f'{settings.SQLALCHEMY_DATABASE_URI}?client_encoding=utf8'
    print(f'Test database: {db_url}')
    return db_url


@pytest.fixture
def db(app, _create_db):
    with app.app_context():
        slq_alchemy_db.create_all()
    slq_alchemy_db.session.commit()
    yield slq_alchemy_db
    slq_alchemy_db.session.rollback()
    with app.app_context():
        slq_alchemy_db.drop_all()


@pytest.fixture
def client(app):
    client = app.test_client()
    context = app.test_request_context()
    context.push()
    return client
