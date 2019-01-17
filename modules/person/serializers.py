from rest_framework import serializers

from modules.person.models import MyUser


class MyUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MyUser
        fields = ('id', 'name', 'email')
