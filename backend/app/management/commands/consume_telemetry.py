from django.core.management.base import BaseCommand, CommandError
import pika, sys, os, requests
from app.models import TelemetryMessage

def send_telemetry_to_backend(ch, method, properties, body):
    if "." in body.decode():
        value = float(body)
    else:
        value = int(body)

    TelemetryMessage.objects.create(value=value)
    return True

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


class Command(BaseCommand):
    help = 'Opens a rabbit consumer'

    def handle(self, *args, **options):
        try:
            main()
        except KeyboardInterrupt:
            print('Interrupted')
            try:
                sys.exit(0)
            except SystemExit:
                os._exit(0)
