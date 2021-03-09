This repo demonstrates the various methods for allowing a Caesium Django
service to consume messages from a RabbitMQ queue. A short writeup of these
methods are given [here](https://oxbotica.atlassian.net/wiki/spaces/CAES/pages/2822373464/Investigation+into+Methods+for+Django+Rabbit+Consumption?focusedCommentId=2837643304&src=mail&src.mail.timestamp=1615204102089&src.mail.notification=com.atlassian.confluence.plugins.confluence-notifications-batch-plugin%3Abatching-notification&src.mail.recipient=8a7f80896f48b470016f65cd0b480425&src.mail.action=view#comment-2837643304).

## Running The Code

In order to run this app, clone this repo, install the dependencies using Poetry,
and run the docker containers:

```bash
poetry shell
poetry install

docker-compose build
docker-compose up
```

The app itself is a Django app with one table (`telemetry_message`),
one POST endpoint and one GET endpoint.

## Methods of Message Consumption

The simplest way of interacting with this app is externally by using HTTP
requests. For example, use the following cURL request to POST some telemetry:

```bash
curl --request GET \
  --url http://localhost:8000/telemetry_message/ \
  --header 'Content-Type: application/json' \
  --data '{"value": 0.3}'
```

However, we're more interested in the app's interaction with the Rabbit service.
The script `scripts/send_telemetry_messages.py` sends 10,000 messages to the
Rabbit queue, which is consumed by one of two scripts:

    - `scripts/rabbit_consumer.py` takes messages and sends them to the app via POST requests
    - `app/management/commands/consume_telemetry.py` takes messages and inserts them directly into the database via the Django ORM

The choice of which to run can be set in `entrypoint.sh`.
