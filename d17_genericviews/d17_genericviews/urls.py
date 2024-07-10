"""
URL configuration for d17_genericviews project.

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
from app1_listview.views import StudentListView
from app2_detailview.views import StudentDetailView
from app3_formview.views import StudentFormView,ThankYouTemplateView
from app4_createview.views import StudentCreateView,StudentCreateDetailView
from app5_updateview.views import StudentUpdateCreateView,StudentUpdateView
from app6_deleteview.views import StudentDeleteView

urlpatterns = [
    path('admin/', admin.site.urls),
    #ListView URLs
    path('studentlist/', StudentListView.as_view(),name='studentlist'),
    #DetailView URLs
    path('studentdetail/<int:pk>', StudentDetailView.as_view(),name='studentdetail'),
    #FormView URLs
    path('studentform/', StudentFormView.as_view(),name='studentform'),
    path('thankyou/', ThankYouTemplateView.as_view(),name='thankyou'),
    #CreateView URLs
    path('createview/', StudentCreateView.as_view(),name='createview'),
    path('createdetailview/<int:pk>', StudentCreateDetailView.as_view(),name='createdetailview'),
    #UpdateView URLs
    path('updatecreateview/', StudentUpdateCreateView.as_view(),name='updatecreateview'),
    path('updateview/<int:pk>', StudentUpdateView.as_view(),name='updateview'),
    #DeleteView URLs
    path('deleteview/<int:pk>', StudentDeleteView.as_view(),name='deleteview'),
    # path('updateview/<int:pk>', StudentUpdateView.as_view(),name='updateview'),
]
