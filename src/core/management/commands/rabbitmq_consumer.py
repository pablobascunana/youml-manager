import json
from typing import Dict

import pika

from django.core.management.base import BaseCommand
from pika import BlockingConnection, BasicProperties
from pika.adapters.blocking_connection import BlockingChannel
from pika.spec import Basic


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('--rabbit_config', nargs='?', type=str)

    def handle(self, *args, **options):
        rabbit_config = json.loads(options.get('rabbit_config'))
        queue_name = rabbit_config["queue_name"]
        connection = self.create_connection(rabbit_config)
        channel = self.create_channel(connection)
        self.queue_declare(channel, queue_name)
        self.consume_message(channel, queue_name)

    @staticmethod
    def create_connection(rabbit_config: Dict[str, str]) -> BlockingConnection:
        credentials = pika.PlainCredentials(rabbit_config["user"], rabbit_config["password"])
        connection_params = pika.ConnectionParameters(host=rabbit_config["host"], credentials=credentials,
                                                      virtual_host=rabbit_config["vhost"])
        return pika.BlockingConnection(connection_params)

    @staticmethod
    def create_channel(connection: BlockingConnection) -> BlockingChannel:
        return connection.channel()

    @staticmethod
    def queue_declare(channel: BlockingChannel, queue_name: str):
        channel.queue_declare(queue=queue_name)

    def consume_message(self, channel: BlockingChannel, queue_name: str):
        channel.basic_consume(queue=queue_name, on_message_callback=self.on_message, auto_ack=True)
        print('Subscribed to train, waiting for messages...')
        channel.start_consuming()

    @staticmethod
    def on_message(channel: BlockingChannel, method: Basic.Deliver, properties: BasicProperties, body: bytes):
        message = body.decode('UTF-8')
        print(message)
