import logging
import time
from typing import Dict

from kubernetes import client, config
from kubernetes.client import BatchV1Api, V1Job

logger = logging.getLogger("youML-manager")


class KubernetesJobManager:

    def __init__(self, job_name: str, container_image_name: str, params: Dict[str, str]):
        config.load_kube_config()
        self.batch_v1 = client.BatchV1Api()
        self.job = self._create_job_object(job_name, container_image_name, params)

    @staticmethod
    def _create_job_object(job_name: str, image_name: str, params: Dict[str, str]):
        container = client.V1Container(name=job_name, image=image_name,
                                       env=[client.V1EnvVar(name="DATASET_UUID", value=params["dataset"]),
                                            client.V1EnvVar(name="DATASET_PATH", value=params["path"])],
                                       resources=client.V1ResourceRequirements(
                                           requests={"cpu": "100m", "memory": "200Mi"},
                                           limits={"cpu": "500m", "memory": "500Mi"}))
        template = client.V1PodTemplateSpec(metadata=client.V1ObjectMeta(labels={'name': job_name}),
                                            spec=client.V1PodSpec(restart_policy='Never', containers=[container]))
        spec = client.V1JobSpec(template=template)
        return client.V1Job(api_version='batch/v1', kind='Job', metadata=client.V1ObjectMeta(name=job_name), spec=spec)

    @staticmethod
    def create_job(api_instance: BatchV1Api, job: V1Job):
        api_response = api_instance.create_namespaced_job(body=job, namespace='default')
        logger.info(f"Job created: status={api_response.status}")

    @staticmethod
    def get_job_status(api_instance: BatchV1Api, job_name: str):
        job_completed = False
        while not job_completed:
            response = api_instance.read_namespaced_job_status(name=job_name, namespace="default")
            if response.status.succeeded is not None or response.status.failed is not None:
                job_completed = True
            time.sleep(1)
            logger.info(f"Job status: status={response.status}")

    @staticmethod
    def delete_job(api_instance: BatchV1Api, job_name: str):
        api_response = api_instance.delete_namespaced_job(name=job_name, namespace='default',
                                                          body=client.V1DeleteOptions(propagation_policy='Foreground',
                                                                                      grace_period_seconds=0))
        logger.info(f"Job deleted: status={api_response.status}")
