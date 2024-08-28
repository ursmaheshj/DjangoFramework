from django.urls import path
from app2.consumers import MySyncConsumer

app2_routings = [
    path('app2/sc/',MySyncConsumer.as_asgi())
]