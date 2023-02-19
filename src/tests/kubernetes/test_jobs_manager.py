# from unittest.mock import MagicMock, patch
# from kubernetes import client
# from core.kubernetes.jobs_manager import KubernetesJobManager
#
#


import pytest
from unittest.mock import patch, MagicMock, Mock
from kubernetes import config
from kubernetes.client import BatchV1Api, V1Job
from core.kubernetes.jobs_manager import KubernetesJobManager


job_name = "test-job"
image_name = "test-image"
params = {"dataset": "", "path": "/test/path"}


class TestKubernetesJobManager:

    @staticmethod
    def test_create_job(mock_api, mock_job):
        with patch.object(config, "load_incluster_config") as mock_load_config:
            mock_instance = MagicMock()
            mock_api.return_value = mock_instance
            job_manager = KubernetesJobManager(job_name, image_name, params)
            job_manager.create_job(mock_instance, mock_job)

            mock_load_config.assert_called_once()
            assert mock_api.call_count == 1
            assert mock_instance.create_namespaced_job.call_count == 1

    @staticmethod
    def test_get_job_status(mock_api):
        with patch.object(config, "load_incluster_config") as mock_load_config:
            mock_instance = MagicMock()
            mock_api.return_value = mock_instance
            job_manager = KubernetesJobManager(job_name, image_name, params)
            job_manager.get_job_status(mock_instance, job_name)

            mock_load_config.assert_called_once()
            assert mock_api.call_count == 1
            assert mock_instance.read_namespaced_job_status.call_count == 1

    @staticmethod
    def test_delete_job(mock_api):
        with patch.object(config, "load_incluster_config") as mock_load_config:
            mock_instance = MagicMock()
            mock_api.return_value = mock_instance
            job_manager = KubernetesJobManager(job_name, image_name, params)
            job_manager.delete_job(mock_instance, job_name)

            mock_load_config.assert_called_once()
            assert mock_api.call_count == 1
            assert mock_instance.delete_namespaced_job.call_count == 1
