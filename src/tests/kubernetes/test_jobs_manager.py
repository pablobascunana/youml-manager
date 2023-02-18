from kubernetes.client import V1Job, BatchV1Api, V1Status

from core.kubernetes.jobs_manager import KubernetesJobManager


job_name = 'job-name'


class TestKubernetesJobManager:

    @staticmethod
    def test_create_job_object(kubernetes: KubernetesJobManager):
        assert isinstance(kubernetes.job, V1Job)
        assert isinstance(kubernetes.batch_v1, BatchV1Api)

    @staticmethod
    def test_create_job(kubernetes: KubernetesJobManager):
        response = kubernetes.create_job(kubernetes.batch_v1, kubernetes.job)
        assert isinstance(response, V1Job)
        assert response.metadata.name == job_name
        assert response.metadata.namespace == 'default'

    @staticmethod
    def test_get_job_status(kubernetes: KubernetesJobManager):
        response = kubernetes.get_job_status(kubernetes.batch_v1, job_name)
        assert isinstance(response, V1Job)
        assert response.metadata.name == job_name
        assert response.metadata.namespace == 'default'

    @staticmethod
    def test_delete_job(kubernetes: KubernetesJobManager):
        response = kubernetes.delete_job(kubernetes.batch_v1, job_name)
        assert isinstance(response, V1Status)
