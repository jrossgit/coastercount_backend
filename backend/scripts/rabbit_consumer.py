#!/usr/bin/env python
import pika, sys, os, requests

def send_telemetry_to_backend(ch, method, properties, body):
    if "." in body.decode():
        value = float(body)
    else:
        value = int(body)

    print(f"{value} class {value.__class__}")
    response = requests.post(
        "http://localhost:8000/telemetry_message/",
        {"value": 100})

    return response.status_code == 201


def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host="rabbitmq"))
    channel = connection.channel()

    def callback(ch, method, properties, body):
        print(" Received %r" % body)

    channel.basic_consume(
        queue='telemetry',
        on_message_callback=send_telemetry_to_backend,
        auto_ack=True
        )

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
