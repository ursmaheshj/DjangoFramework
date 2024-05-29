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
    # data = Student.objects.filter(name='Mahesh').exists()
    # data=Student.objects.create(name='Radha',city='Mathura',roll=51,marks=100,pass_date='2020-3-28')
    # data,created=Student.objects.get_or_create(name='Radha',city='Mathura',roll=31,marks=100,pass_date='2020-3-28') #crated will be true false based on object creation
    # data = Student.objects.filter(name='Radha').update(city='Mathura') 
    # data = Student.objects.filter(name='Radaha').update_or_create(name='Krishna',city='Mathura',roll=44,marks=44,pass_date='2024-3-28')
    # data,created = Student.objects.update_or_create(id=45,name='Ranga',defaults={'name':'Ranga','city':'mohpur','roll':19,'marks':44,'pass_date':'2024-3-28'})
    # objs = [
    #     Student(name='Zakir',city='Lucknow',roll=101,marks=50,pass_date='2020-3-28'),
    #     Student(name='Abhii',city='Pune',roll=102,marks=51,pass_date='2020-3-29'),
    #     Student(name='Samay',city='Mumbai',roll=103,marks=50,pass_date='2020-3-1')
    # ]
    # data = Student.objects.bulk_create(objs)
    # objs = Student.objects.filter(marks=99)
    # for obj in objs:
    #     obj.city = 'Pune'
    # data = Student.objects.bulk_update(objs,['city'])
    # data = Student.objects.in_bulk([1,4,5]) 
    # data = Student.objects.filter(marks=50).delete()
    # data = Student.objects.get(pk=3).delete()
    # data = Student.objects.filter(marks=99).count()
    data = Student.objects.filter(marks=99).explain()

    print("---Return Data:", data)
    # print("---Query:",data.query) #only used with queryset with list
    return render(request,'app2/home2.html',{'data':data})
    