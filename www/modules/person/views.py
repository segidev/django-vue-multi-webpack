from rest_framework import viewsets

from modules.person.models import MyUser
from modules.person.serializers import MyUserSerializer


class MyUserViewset(viewsets.ModelViewSet):
    queryset = MyUser.objects.all()
    serializer_class = MyUserSerializer
