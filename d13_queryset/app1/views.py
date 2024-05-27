from django.shortcuts import render
from app1.models import Student

# Create your views here.
def home(request):
    # data = Student.objects.all()
    # data = Student.objects.filter(marks = 99,name='Ram')
    # data = Student.objects.exclude(marks = 99,name='Ram')
    # data = Student.objects.order_by('marks','-name')
    # data = Student.objects.order_by('id').reverse()[:4]
    # data = Student.objects.values()
    # data = Student.objects.values('name','city','pass_date')
    # data = Student.objects.distinct()
    # data = Student.objects.values_list('name','city',named=True)
    # data = Student.objects.using('default')
    data = Student.objects.dates('pass_date','week')

    print("---Return Data:", data)
    print("---Query:",data.query)
    return render(request,'app1/home.html',{'data':data})
    