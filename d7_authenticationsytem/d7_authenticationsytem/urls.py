"""
URL configuration for d7_authenticationsytem project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app1.views import sign_up
from app2.views import login_user,profile,logout_user,changepass,changepassold,userdetail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', sign_up,name='signup'),
    path('login/', login_user,name='login'),
    path('profile/', profile,name='profile'),
    path('logout/', logout_user,name='logout'),
    path('changepassold/', changepassold,name='changepassold'),
    path('changepass/', changepass,name='changepass'),
    path('userdetail/<int:id>', userdetail,name='userdetail'),
]
