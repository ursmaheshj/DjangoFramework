from django.shortcuts import render,HttpResponse
from app4_modelmanager.models import Student

# Create your views here.
def modelmanager(request):
    students = Student.modelManager.values() #using our own manger name defined in models.py
    return HttpResponse(students)