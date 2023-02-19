import pytest

from unittest.mock import patch


@pytest.fixture
def mock_api():
    with patch("core.kubernetes.jobs_manager.client.BatchV1Api") as mock_api:
        yield mock_api


@pytest.fixture
def mock_job():
    with patch("core.kubernetes.jobs_manager.client.V1Job") as mock_job:
        yield mock_job
