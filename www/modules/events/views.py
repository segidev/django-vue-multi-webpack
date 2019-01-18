from rest_framework import viewsets

from modules.events.models import MyEvent
from modules.events.serializers import MyEventSerializer


class MyEventViewset(viewsets.ModelViewSet):
    queryset = MyEvent.objects.all()
    serializer_class = MyEventSerializer
