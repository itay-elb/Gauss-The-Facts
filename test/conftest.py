import pytest
import mysql.connector

@pytest.fixture
def db():
    mydb = mysql.connector.connect(
        host='localhost',
        user='root',
        passwd='root',
        database='project',
        port=3306
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
