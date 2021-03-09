from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from app.models import TelemetryMessage
from app.serializers import TelemetryMessageSerializer


# Create your views here.
class TelemetryMessageViewSet(ModelViewSet):

    queryset = TelemetryMessage.objects.all()
    serializer_class = TelemetryMessageSerializer
