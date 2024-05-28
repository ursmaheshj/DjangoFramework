from django.shortcuts import render
from app1.models import Student,Teacher

# Create your views here.
def home2(request):
    # data = Student.objects.get(pk=1)
    # data = Student.objects.get(name='Rutuja') # should be uniquely identifiable
    # data = Student.objects.first()
    # data = Student.objects.order_by('name').first()
    # data = Student.objects.last()
    # data = Student.objects.latest('pass_date')
    # data = Student.objects.earliest('pass_date')
    # data = Student.objects.exists()
    data = Student.objects.filter(name='Mahesh').exists()

    print("---Return Data:", data)
    # print("---Query:",data.query) #only used with queryset with list
    return render(request,'app2/home2.html',{'data':data})
    