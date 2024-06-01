from django.shortcuts import render
from app3.models import Student
from datetime import date, time

# Create your views here.
def home3(request):
    # students = Student.objects.all()
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
    students = Student.objects.filter(admdatetime__minute__gt=15)
    


    print("---Return Data:", students)
    print("---Query:",students.query) #only used with queryset with list
    return render(request,'app3/home3.html',{'students':students})
