import pytest


@pytest.fixture()
def app():
    from src.app import app
    yield app

@pytest.fixture()
def client(app):
    return app.test_client()
