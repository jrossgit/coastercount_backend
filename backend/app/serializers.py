from rest_framework import serializers

from app.models import TelemetryMessage

class TelemetryMessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = TelemetryMessage
        fields = "__all__"
