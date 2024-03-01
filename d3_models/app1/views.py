from django.shortcuts import render

from app1.models import Student

# Create your views here.

def home(request):
    students = Student.objects.all()
    pk=1
    student = Student.objects.get(id=pk)
    context = {
        'students':students,
        'student':student
    }
    return render(request,'app1/home.html',context)