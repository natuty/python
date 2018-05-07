#!/usr/bin/env python
import pika

credentials = pika.PlainCredentials('root', '123456')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='192.168.1.188',credentials=credentials))
channel = connection.channel()

channel.queue_declare(queue='hello')

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)

channel.basic_consume(callback,
                      queue='hello',
                      no_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()