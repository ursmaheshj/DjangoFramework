from django.shortcuts import render
from app1.models import Student

# Create your views here.
def home(request):
    # data = Student.objects.all()
    # data = Student.objects.filter(marks = 99,name='Ram')
    # data = Student.objects.exclude(marks = 99,name='Ram')
    data = Student.objects.order_by('marks','-name')

    print("---Return Data:", data)
    print("---Query:",data.query)
    return render(request,'app1/home.html',{'data':data})
    