from django.shortcuts import render
from app1.models import Student,Teacher

# Create your views here.
def home(request):
    data = Student.objects.all()
    # data = Student.objects.filter(marks = 99,name='Ram')
    # data = Student.objects.exclude(marks = 99,name='Ram')
    # data = Student.objects.order_by('marks','-name')
    # data = Student.objects.order_by('id').reverse()[:4]
    # data = Student.objects.values()
    # data = Student.objects.values('name','city','pass_date')
    # data = Student.objects.distinct()
    # data = Student.objects.values_list('name','city',named=True)
    # data = Student.objects.using('default')
    # data = Student.objects.dates('pass_date','week')
    # data = Student.objects.union(Teacher.objects.all(),all=True)
    # q1 = Student.objects.values_list('name','marks',named=True)
    # q2 = Teacher.objects.values_list('name','salary',named=True)
    # data = q1.union(q2,all=True)
    # data = q1.intersection(q2)
    # data = q2.difference(q1)
    # data = Student.objects.filter(id=1) & Student.objects.filter(name='Mahesh')
    # data = Student.objects.filter(id=1) | Student.objects.filter(name='Rutuja')

    print("---Return Data:", data)
    print("---Query:",data.query)
    return render(request,'app1/home.html',{'data':data})
    