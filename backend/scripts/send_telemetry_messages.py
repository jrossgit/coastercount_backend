#!/usr/bin/env python
import pika, requests, sys

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

for i in range(10000):
    # requests.post("http://localhost:8000/telemetry_message/", {"value": i})
    channel.basic_publish(
        exchange='',
        routing_key='telemetry',
        body=str(i))

connection.close()
