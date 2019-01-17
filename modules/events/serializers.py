from rest_framework import serializers

from modules.events.models import MyEvent


class MyEventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MyEvent
        fields = ('id', 'name', 'date')
