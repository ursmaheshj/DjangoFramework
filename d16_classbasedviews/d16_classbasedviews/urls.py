"""
URL configuration for d16_classbasedviews project.

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
from app1_classview.views import Demo, DemoChild, Demotemplate, ContactView, NewsChannel    
from django.views.generic.base import TemplateView
from app2_templateview.views import MyTemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    
    #----------------------app1 VIEW URLS-------------------------------
    # path('demo/', Demo.as_view(),name='demo'),    
    path('demo/', Demo.as_view(name='RAM'),name='demo'), # we can pass name as argument to as_view() method
    path('demochild/', DemoChild.as_view(),name='demochild'),
    path('demotemplate/', Demotemplate.as_view(),name='demotemplate'),
    path('contact/', ContactView.as_view(),name='contact'),
    # path('news/', NewsChannel.as_view(template_name='app1/newschannel1.html'),name='news'),
    path('news/', NewsChannel.as_view(template_name='app1/newschannel2.html'),name='news'),
    
    #-----------------------app2 TEMPLATEVIEW URLS-----------------------
    path('templateview/', TemplateView.as_view(template_name='app2/home.html'),name='templateview'),
    path('mytemplateview/', MyTemplateView.as_view(),name='mytemplateview'),
    path('mytemplateviewextra/', MyTemplateView.as_view(extra_context={'wife':'Sita'}),name='mytemplateviewextra'),
    path('mytemplateviewextrakwargs/<int:cl>', MyTemplateView.as_view(extra_context={'wife':'Sita'}),name='mytemplateviewextrakwargs'),
]