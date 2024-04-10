"""
URL configuration for d8_cookies project.

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
from app1.views import setcookie,getcookie,deletecookie
from app2.views import ssetcookie,sgetcookie,sdeletecookie

urlpatterns = [
    path('admin/', admin.site.urls),
    path('setcookie/', setcookie),
    path('getcookie/', getcookie),
    path('deletecookie/', deletecookie),

    path('ssetcookie/', ssetcookie),
    path('sgetcookie/', sgetcookie),
    path('sdeletecookie/', sdeletecookie),
]
