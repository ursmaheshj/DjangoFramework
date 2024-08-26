from django.urls import path
from .consumers import MySyncConsumer,MyAsyncConsumer

app1_routings = [
    path('ws/sc/',MySyncConsumer.as_asgi()),
    path('ws/ac/',MyAsyncConsumer.as_asgi())
]