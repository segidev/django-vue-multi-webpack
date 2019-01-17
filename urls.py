from django.urls import path, include
from rest_framework import routers

from modules.events.views import MyEventViewset
from modules.person.views import MyUserViewset

router = routers.DefaultRouter()
router.register(r'myusers', MyUserViewset)
router.register(r'myevents', MyEventViewset)

urlpatterns = [
    path('', include(router.urls)),
    path('api/', include('rest_framework.urls')),
]
