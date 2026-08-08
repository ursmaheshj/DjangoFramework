from django.urls import path
from genericcbv.views import UserListView,UserDetailView,UserCreateView,UserUpdateView,UserDeleteView
from django.views.generic.base import RedirectView

urlpatterns = [
    path('',RedirectView.as_view(pattern_name='listuser'),name='home'),
    path('listuser/',UserListView.as_view(),name='listuser'),
    path('createuser/',UserCreateView.as_view(),name='createuser'),
    path('detailuser/<int:pk>',UserDetailView.as_view(),name='detailuser'),
    path('updateuser/<int:pk>',UserUpdateView.as_view(),name='updateuser'),
    path('deleteuser/<int:pk>',UserDeleteView.as_view(),name='deleteuser'), 
]
