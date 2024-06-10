from django.db import models
from app4_modelmanager.customManagers import CustomManager

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=50)
    roll = models.IntegerField()
    modelManager = models.Manager()

class Teacher(models.Model):
    name = models.CharField(max_length=50)
    salary = models.IntegerField()
    teachers = CustomManager()
    objects = models.Manager()

class ExamCenter(models.Model):
    name = models.CharField(max_length=50)
    city = models.CharField(max_length=50)

class MyExamCenter(ExamCenter):
    examManager = CustomManager()
    class Meta:
        proxy = True
        ordering = ['name']