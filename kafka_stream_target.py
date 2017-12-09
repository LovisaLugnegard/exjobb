"""Module to connect to Kafka server and send messages to Kafka producer."""

import time

from kafka import KafkaProducer, KafkaClient, SimpleProducer
from kafka.common import LeaderNotAvailableError


class KafkaStreamTarget:

    def __init__(self):
        # kafka = KafkaClient("129.16.125.231:9092")
        self.producer = KafkaProducer(bootstrap_servers=["130.239.81.54:9092"])
        self.topic = 'test'
        print(type(self.producer))
        # return [topic, producer]

    def old_connect(self, message):
        kafka = KafkaClient("130.239.81.54:9092")
        self.producer = SimpleProducer(kafka)
        self.topic = 'test'

        try:
            self.producer.send_messages(self.topic, message)
        except LeaderNotAvailableError:
            # https://github.com/mumrah/kafka-python/issues/249
            time.sleep(1)
            KafkaStreamTarget.print_response(self.producer.send_messages(self.topic, message))

        kafka.close()

    def send_kafka_message(self, message, file_name):
        # kafka = KafkaClient("130.239.81.54:9092")
        # self.producer = SimpleProducer(kafka)
        # self.topic = 'test'
        # self.producer = KafkaProducer(bootstrap_servers=["130.239.81.54:9092"])
        # self.producer = KafkaProducer(bootstrap_servers=["130.239.81.54:9092"])
        print("in send_msg!")
        print("prod: {} topic: {}".format(self.producer, self.topic))

        try:
            self.producer.send(self.topic, key=str.encode(file_name), value=message)
            #  self.producer.send(self.topic, key=file_name, value=message)
            print("msg sent!")
        except LeaderNotAvailableError:
            print("in except :(")
            # https://github.com/mumrah/kafka-python/issues/249
            time.sleep(1)
            KafkaStreamTarget.print_response(self.producer.send(self.topic, key=file_name, value=message))

        #  kafka.close()

    @staticmethod
    def print_response(response=None):
        if response:
            print('Error: {0}'.format(response[0].error))
            print('Offset: {0}'.format(response[0].offset))