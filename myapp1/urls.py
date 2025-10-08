from django.urls import path
from .api import hello_world

urlpatterns = [
    path('api/hello/', hello_world, name='hello_world'),
]


