from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from app4_createview.models import Cstudent 


# Create your views here.
class StudentCreateView(CreateView):
    model = Cstudent
    fields = ['name','roll','course']
    # success_url = '/createview/'
    
class StudentCreateDetailView(DetailView):
    model = Cstudent