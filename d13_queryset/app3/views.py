from django.shortcuts import render
from app3.models import Student
from datetime import date, time
from django.db.models import Avg,Sum,Min,Max,Count,StdDev,Variance
from django.db.models import Q

# Create your views here.
def home3(request):
    # students = Student.objects.all()
    # students = Student.objects.all()[:5]
    # students = Student.objects.all()[2:7]
    # students = Student.objects.all()[2:10:2]
    # students = Student.objects.filter(name__exact='Rutuja')  #Case sensitive
    # students = Student.objects.filter(name__iexact='ruTuja')  #Case insensitive
    # students = Student.objects.filter(name__contains='ru')  #Case sensitive
    # students = Student.objects.filter(name__icontains='ru')  #Case insensitive
    # students = Student.objects.filter(marks__in=[12,90,70])
    # students = Student.objects.filter(marks__gt=50)
    # students = Student.objects.filter(marks__gte=50)
    # students = Student.objects.filter(marks__lt=70)
    # students = Student.objects.filter(marks__lte=70)
    # students = Student.objects.filter(name__startswith='ru')
    # students = Student.objects.filter(name__istartswith='ru')
    # students = Student.objects.filter(name__endswith='H')
    # students = Student.objects.filter(name__iendswith='H')
    # students = Student.objects.filter(passdate__range=('2024-03-05','2024-05-10'))
    # students = Student.objects.filter(admdatetime__date=date(2024,3,6))
    # students = Student.objects.filter(admdatetime__year=2023)
    # students = Student.objects.filter(passdate__year=2023)
    # students = Student.objects.filter(passdate__year__gt=2023)
    # students = Student.objects.filter(passdate__year__gte=2023)
    # students = Student.objects.filter(passdate__month=5)
    # students = Student.objects.filter(passdate__month__gt=2)
    # students = Student.objects.filter(passdate__day=2)
    # students = Student.objects.filter(passdate__day__gt=15)
    # students = Student.objects.filter(passdate__week=1)  #52 weeks
    # students = Student.objects.filter(passdate__week__lt=4)
    # students = Student.objects.filter(passdate__week_day=3)
    # students = Student.objects.filter(passdate__quarter=2)
    # students = Student.objects.filter(admdatetime__time=time(9,45,34))
    # students = Student.objects.filter(admdatetime__time__gt=time(10,45,34))
    # students = Student.objects.filter(admdatetime__hour__gt=10)
    # students = Student.objects.filter(admdatetime__minute__gt=15)
    # students = Student.objects.filter(admdatetime__second__gt=30)
    # students = Student.objects.filter(name__isnull=True)
    students = Student.objects.filter(city__regex='^.a')

    #------------------- Q objects for conditioning---------------------
    # q_results = Student.objects.filter(Q(name='Ram'),Q(marks=80))
    # q_results = Student.objects.filter(Q(name='Ram') & Q(marks=80))
    q_results = Student.objects.filter(Q(name='Ram') | Q(marks=80))
    # q_results = Student.objects.filter(Q(name='Ram') & ~ Q(marks=80))
    

    #------------------# Aggregate Functions in Django------------------
    avg = Student.objects.aggregate(Avg('marks'))
    sum = Student.objects.aggregate(Sum('marks'))
    min = Student.objects.aggregate(Min('marks'))
    max = Student.objects.aggregate(Max('marks'))
    count = Student.objects.aggregate(Count('marks'))
    std = Student.objects.aggregate(StdDev('marks'))
    var = Student.objects.aggregate(Variance('marks'))
    min_max = Student.objects.aggregate(Min('marks'),Max('marks'))
    

    context = {
        'students':students,
        'q_results':q_results,
        'avg':avg,
        'sum':sum,
        'min':min,
        'max':max,
        'count':count,
        'std':std,
        'var':var,
        'min_max':min_max,

    }
    print("---Return Data:", students)
    # print("---Query:",students.query) #only used with queryset list
    print("---Query:",q_results.query) #only used with queryset list
    return render(request,'app3/home3.html',context)
