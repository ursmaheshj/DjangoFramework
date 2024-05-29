from django.shortcuts import render
from app3.models import Student

# Create your views here.
def home3(request):
    students = Student.objects.all()


    print("---Return Data:", students)
    print("---Query:",students.query) #only used with queryset with list
    return render(request,'app3/home3.html',{'students':students})
