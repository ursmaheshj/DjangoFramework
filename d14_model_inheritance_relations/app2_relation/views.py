from django.shortcuts import render,HttpResponse
from app2_relation.models import ExamCenter,Student
# Create your views here.

def home(request):
    centers = ExamCenter.objects.all().values_list()
    students = Student.objects.all().values_list()
    print(centers)
    print(students)
    return HttpResponse('ce')