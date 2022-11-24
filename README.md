# youml-manager

## Dependencies

*  Python >= 3.8

## Installation

* Create virtual environment

```shell
python -m venv <venv name>
```

* Install pipenv

```shell
pip install pipenv
```

* Install dependencies

```shell
pipenv install
```

## Install RabbitMQ in local environment

You should install [Docker Desktop](https://www.docker.com/products/docker-desktop/) and execute the
**docker-compose.yml** inside **.local/rabbitmq** directory, to do this, place in the specified directory and execute
the following command:

```shell
docker compose up
```

To access to **RabbitMQ** UI management use the following URL: [UI Management](http://localhost:15672)
