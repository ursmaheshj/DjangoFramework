"""
URL configuration for d18_defaultauthenticationviews project.

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
from django.urls import path
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView

urlpatterns = [
 path('',TemplateView.as_view(template_name='myapp/home.html'),name='home'),
 path('dashboard/',TemplateView.as_view(template_name='myapp/dashboard.html'),name='dashboard'),
 path('login/',auth_views.LoginView.as_view(template_name='myapp/login.html'),name='login'),
]