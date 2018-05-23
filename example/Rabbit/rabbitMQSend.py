#!/usr/bin/env python
import pika

credentials = pika.PlainCredentials('root', '123456')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='192.168.1.188',credentials=credentials))
channel = connection.channel()

# class ReportMessage:
# 	def __init__(self, isDevice, action, log, clock, projectId)
# 		self.isDevice=isDevice
# 		self.action=action
# 		self.workPlanDetail=log
# 		self.type=clock
# 		self.projectId=projectId

channel.queue_declare(queue='hello')
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World!')
print(" [x] Sent 'Hello World!'")
connection.close()