from django.shortcuts import render
from django.views.generic.detail import DetailView
from app2_detailview.models import Dstudent

# Create your views here.
class StudentDetailView(DetailView):
    model = Dstudent