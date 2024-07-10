from django.shortcuts import render
from django.views.generic.edit import CreateView,UpdateView
from app5_updateview.models import Ustudent

# Create your views here.
class StudentUpdateCreateView(CreateView):
    model = Ustudent
    fields = ['name','roll','course']
    success_url = '/updatecreateview/'