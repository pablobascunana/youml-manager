# youml-manager

## Dependencies

*  Python >= 3.8

## Installation

* Create virtual environment

```shell
python3 -m venv <venv name>
```

* Install pipenv

```shell
pip install pipenv
```

* Install dependencies

```shell
pipenv install
```

If you use PyCharm you have all available commands for this project inside **.run** folder

* To start server

```shell
python src/manage.py runserve
```

* To run tests without coverage

```shell
pytest src/tests
```

* To run tests with coverage in console

```shell
pytest --cov-report term-missing --cov-config=.coveragerc --cov=src src/tests
```

* To run tests with coverage in HTML files

```shell
pytest src/tests --cov=src --cov-config=.coveragerc --cov-report=html:.test-results
```

* To run tests with coverage in XML for Codacy

```shell
pytest src/tests --cov=src --cov-config=.coveragerc --cov-report=xml:coverage-reports/coverage.xml
```

## Install RabbitMQ in local environment

You should install [Docker Desktop](https://www.docker.com/products/docker-desktop/) and execute the
**docker-compose.yml** inside **.local/rabbitmq** directory, to do this, place in the specified directory and execute
the following command:

```shell
docker compose up
```

To access to **RabbitMQ** UI management use the following URL: [UI Management](http://localhost:15672)

## Install Minikube in local environment

....

```shell
minikube start
```

#### Work with Kubernetes

Start job from yaml file:
```shell
kubectl apply -f <FILENAME>.yaml 
```
Get pods:
```shell
kubectl get pods 
```
Obtain more information about pods:
```shell
kubectl describe pods
```
Get log of specific pod:
```shell
kubectl logs <POD-NAME> -f
```
Delete job
```shell
kubectl delete job <JOB_NAME> 
```
