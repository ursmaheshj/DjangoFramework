from django.db import models

# Create your models here.
class CommonInfo(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    date = models.DateField()
    class Meta:        
        abstract = True        #Makes this class abstract and wont show in admin dashboard

class Student(CommonInfo):
    fees = models.IntegerField()
    date = None               #Wont inherit from parent

class Teacher(CommonInfo):
    salary = models.IntegerField()

class Contractor(CommonInfo):
    payment = models.IntegerField()
    date = models.DateTimeField()   #override from parent