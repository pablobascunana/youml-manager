import json
from unittest.mock import MagicMock, Mock

from core.management.commands.rabbitmq_consumer import Command


class TestRabbitMQConsumer:

    @staticmethod
    def test_handle_calls_create_connection_create_channel_and_consume_message(mocker, rabbit_config):
        mock_create_connection = mocker.patch.object(Command, 'create_connection', return_value=MagicMock())
        mock_create_channel = mocker.patch.object(Command, 'create_channel', return_value=MagicMock())
        mock_queue_declare = mocker.patch.object(Command, 'queue_declare')
        mock_consume_message = mocker.patch.object(Command, 'consume_message')

        cmd = Command()
        cmd.handle(rabbit_config=json.dumps(rabbit_config))

        mock_create_connection.assert_called_once_with(rabbit_config)
        mock_create_channel.assert_called_once_with(mock_create_connection.return_value)
        mock_queue_declare.assert_called_once_with(mock_create_channel.return_value, rabbit_config["queue_name"])
        mock_consume_message.assert_called_once_with(mock_create_channel.return_value, rabbit_config["queue_name"])

    @staticmethod
    def test_create_connection_returns_blocking_connection(mocker, rabbit_config):
        mock_blocking_connection = mocker.patch('core.management.commands.rabbitmq_consumer.pika.BlockingConnection')

        cmd = Command()
        connection = cmd.create_connection(rabbit_config)

        mock_blocking_connection.assert_called_once_with(mocker.ANY)
        connection_params = mock_blocking_connection.call_args[0][0]
        assert connection_params.host == rabbit_config["host"]
        assert connection_params.credentials.username == rabbit_config["user"]
        assert connection_params.credentials.password == rabbit_config["password"]
        assert connection_params.virtual_host == rabbit_config["vhost"]
        assert isinstance(connection, mocker.MagicMock)

    @staticmethod
    def test_create_channel_returns_blocking_channel(mocker):
        mock_blocking_connection = mocker.MagicMock()
        mock_blocking_channel = mocker.patch.object(mock_blocking_connection, 'channel', return_value=MagicMock())

        cmd = Command()
        channel = cmd.create_channel(mock_blocking_connection)

        mock_blocking_channel.assert_called_once()
        assert isinstance(channel, mocker.MagicMock)

    @staticmethod
    def test_queue_declare_calls_channel_queue_declare(mocker):
        mock_blocking_channel = mocker.MagicMock()

        cmd = Command()
        cmd.queue_declare(mock_blocking_channel, "my_queue")

        mock_blocking_channel.queue_declare.assert_called_once_with(queue="my_queue")

    @staticmethod
    def test_consume_message_calls(mocker):
        mock_blocking_channel = mocker.MagicMock()

        cmd = Command()
        cmd.consume_message(mock_blocking_channel, "my_queue")

        mock_blocking_channel.basic_consume.assert_called_once_with(queue="my_queue",
                                                                    on_message_callback=cmd.on_message, auto_ack=True)
        mock_blocking_channel.start_consuming.assert_called_once()

    @staticmethod
    def test_on_message_logs_message(mocker):
        mock_logger = mocker.patch('core.management.commands.rabbitmq_consumer.logger')

        cmd = Command()
        cmd.on_message(Mock(), Mock(), Mock(), b"Hello, world!")

        mock_logger.info.assert_called_once_with("Hello, world!")
