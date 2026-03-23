from django.urls import path, include
from rest_framework import routers
from .api import *

router = routers.DefaultRouter()

router.register('api/projects', ProjectViewSet, 'projects')

urlpatterns = [
    path('', include(router.urls)),
]