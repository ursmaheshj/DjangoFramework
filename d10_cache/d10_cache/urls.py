"""
URL configuration for d10_cache project.

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
from app1.views import home
from app2.views import perviewhome
from app3.views import fragmenthome
from app4.views import lowlevelhome,lowlevelgethome
from django.views.decorators.cache import cache_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home),
    # path('perviewhome/', perviewhome),
    path('perviewhome/', cache_page(20)(perviewhome),name='perviewhome'),
    path('fragmenthome/', fragmenthome),
    path('lowlevelhome/', lowlevelhome),
    path('lowlevelgethome/', lowlevelgethome),
]
