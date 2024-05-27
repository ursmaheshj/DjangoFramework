from django.shortcuts import render
from app1.models import Student

# Create your views here.
def home(request):
    data = Student.objects.all()
    print("---Return Data:", data)
    print("---Query:",data.query)
    return render(request,'app1/home.html',{'data':data})
    