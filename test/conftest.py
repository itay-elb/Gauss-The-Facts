import pytest
import mysql.connector

@pytest.fixture
def db():
    mydb = mysql.connector.connect(
        host='mysql',
        user='root',
        passwd='root',
        database='project'
    )
    yield mydb
    mydb.close()

@pytest.fixture
def app():
   from src.app import app
   yield app

@pytest.fixture()
def client(app):
   return app.test_client()
