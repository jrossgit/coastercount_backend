FROM rabbitmq:3.8.2-management-alpine

ENV RABBITMQ_PLUGINS_DIR=/opt/rabbitmq/plugins

ADD ./config/rabbitmq.conf /etc/rabbitmq/
ADD ./config/definitions.json /etc/rabbitmq/

RUN apk --no-cache add curl
RUN apk --no-cache add bash

RUN mkdir -p $RABBITMQ_PLUGINS_DIR
RUN curl -Lo $RABBITMQ_PLUGINS_DIR/rabbitmq_message_timestamp.ez https://github.com/rabbitmq/rabbitmq-message-timestamp/releases/download/v3.8.0/rabbitmq_message_timestamp-3.8.0.ez

ENV PLUGIN_MESSAGE_TIMESTAMP_HASH="ac015bd6831039f506a356d2a5e5dba787ddd2025a481f0d7ec68db6d9c506a4  $RABBITMQ_PLUGINS_DIR/rabbitmq_message_timestamp.ez"

RUN bash -c 'if [ "$PLUGIN_MESSAGE_TIMESTAMP_HASH" != "$(sha256sum $RABBITMQ_PLUGINS_DIR/rabbitmq_message_timestamp.ez)" ]; then echo "rabbitmq_message_timestamp plugin hash did not match" && exit 1; fi'
RUN rabbitmq-plugins enable rabbitmq_message_timestamp