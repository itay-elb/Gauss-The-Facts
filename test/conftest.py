import pytest


@pytest.fixture()
def app():
    from project.src.app import app
    yield app

@pytest.fixture()
def client(app):
    return app.test_client()
