from django.shortcuts import render,HttpResponse
from app4_modelmanager.models import Student,Teacher

# Create your views here.
def modelmanager(request):
    students = Student.modelManager.values() #using our own manger name defined in models.py
    return HttpResponse(students)

def custommodelmanager(request):
    # teachers = Teacher.objects.all().values()
    teachers = Teacher.teachers.all().values()
    return HttpResponse(teachers)