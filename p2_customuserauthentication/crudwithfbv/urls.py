from django.urls import path
from crudwithfbv.views import home,loginview,register,activate_account,dashboard
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('home/', home, name='home'),
    path('dashboard/', dashboard, name='dashboard'),
    path('login/', loginview, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', register, name='register'),
    path('activate/<str:uidb64>/<str:token>', activate_account, name='activate'),
]