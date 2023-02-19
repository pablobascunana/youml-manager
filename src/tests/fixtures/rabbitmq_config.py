import pytest


@pytest.fixture
def rabbit_config():
    return {
        "user": "guest",
        "password": "guest",
        "host": "localhost",
        "vhost": "/",
        "queue_name": "train-queue"
    }
