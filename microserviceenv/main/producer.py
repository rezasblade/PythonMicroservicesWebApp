import pika, json

params = pika.URLParameters('amqps://ohmdljko:h6RD1mcBJtkjCAb0CeYt95cwwWnpwSdB@goose.rmq2.cloudamqp.com/ohmdljko')

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='admin', body=json.dumps(body), properties=properties)