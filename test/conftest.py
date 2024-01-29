import pytest
import mysql.connector

@pytest.fixture
def db():
    # Get the MySQL service IP address from services.db.ports
    mysql_service_ip = "127.0.0.1"
    for port_info in pytest.config.getoption("--docker-services-ports"):
        if "db" in port_info:
            mysql_service_ip = port_info.split(":")[0]
            break

    mydb = mysql.connector.connect(
        host=mysql_service_ip,
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
def client(app):
    return app.test_client()

