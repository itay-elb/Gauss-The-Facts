import pytest
from pytest_docker import docker_services
import mysql.connector

@pytest.fixture(scope="module")
def mysql_service(docker_services):
    service = docker_services.start('mysql',
        environment={
            'MYSQL_ROOT_PASSWORD': 'root',
            'MYSQL_DATABASE': 'project'
        },
        network='protest_default')
    docker_services.wait_until_responsive(timeout=30, host='mysql', port=3307)
    yield service
    service.remove()

@pytest.fixture
def db(mysql_service):
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
