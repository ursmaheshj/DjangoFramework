from django.urls import path
from app3.views import home,details,subdetails

urlpatterns = [
    path('',home,name='home'),
    path('details/<int:details_id>',details,name='details'),
    path('details/<int:details_id>/<int:subdetails_id>',subdetails,name='subdetails')
]