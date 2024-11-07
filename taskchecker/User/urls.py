from django.urls import path, include
from rest_framework import routers

from .views import *

router = routers.SimpleRouter()
router.register(r'user', UserViewSet)

urlpatterns = [
    path('', include(router.urls)) # http://127.0.0.1:8000/api/v1/user/

]