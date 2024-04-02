import pytest
import mysql.connector
import os
from dotenv import load_dotenv
load_dotenv()

@pytest.fixture
def db():          # connect to the database with the .env file
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
def app():         # enter to app
   from src.app import app
   yield app

@pytest.fixture()
def client(app, db):      # create client who enter the app and use the database
   return app.test_client()
