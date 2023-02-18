import pytest

from core.kubernetes.jobs_manager import KubernetesJobManager


@pytest.fixture()
def kubernetes():
    return KubernetesJobManager('job-name', 'hello-world', params={"dataset": "1234", "path": "/path/to/images"})
