from django.urls import include
from app1.routing import app1_routings
from app2.routing import app2_routings

ws_urlpatterns = [
    *app1_routings,
    *app2_routings
]