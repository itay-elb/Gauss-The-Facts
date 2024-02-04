import pytest
import mysql.connector
import os

@pytest.fixture
def db():
    mydb = mysql.connector.connect(
        host=os.getenv('DB_HOST'),
        user=os.getenv('DB_USER'),
        passwd=os.getenv('DB_PASSWD'),
        database=os.getenv('DB_NAME'),
        port=os.getenv('DB_PORT')
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
