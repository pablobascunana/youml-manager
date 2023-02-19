from unittest.mock import MagicMock, patch
from kubernetes import client
from core.kubernetes.jobs_manager import KubernetesJobManager


class TestKubernetesJobManager:

    @staticmethod
    def test_create_job(kubernetes: KubernetesJobManager):
        with patch.object(client.BatchV1Api, 'create_namespaced_job') as mock_create_job:
            job = MagicMock()
            mock_create_job.return_value = job
            kubernetes.create_job(kubernetes.batch_v1, job)
            mock_create_job.assert_called_once_with(body=job, namespace='default')

    @staticmethod
    def test_get_job_status(kubernetes: KubernetesJobManager):
        with patch.object(client.BatchV1Api, 'read_namespaced_job_status') as mock_read_job_status:
            kubernetes.get_job_status(kubernetes.batch_v1, 'my-job')
            mock_read_job_status.assert_called_once_with(name='my-job', namespace='default')

    @staticmethod
    def test_delete_job(kubernetes: KubernetesJobManager):
        with patch.object(client.BatchV1Api, 'delete_namespaced_job') as mock_delete_job:
            kubernetes.delete_job(kubernetes.batch_v1, 'my-job')
            mock_delete_job.assert_called_once_with(name='my-job', namespace='default',
                                                    body=client.V1DeleteOptions(propagation_policy='Foreground',
                                                                                grace_period_seconds=0))
