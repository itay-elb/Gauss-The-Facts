import pytest
import mysql.connector
import os

@pytest.fixture
def db():
    host = os.environ.get('MYSQL_HOST')
    user = os.environ.get('MYSQL_USER')
    password = os.environ.get('MYSQL_PASSWORD')
    database = os.environ.get('MYSQL_DATABASE')
    port = int(os.environ.get('MYSQL_PORT'))

    mydb = mysql.connector.connect(
        host=host,
        user=user,
        passwd=password,
        database=database,
        port=port
    )
    yield mydb
    mydb.close()

@pytest.fixture
def app():
   from src.app import app
   yield app

@pytest.fixture()
def client(app, db):
   return app.test_client()
