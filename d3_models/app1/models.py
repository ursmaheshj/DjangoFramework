from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length = 20)
    division = models.CharField(max_length=10)
    about = models.TextField()

class Teacher(models.Model):
    teacher_code = models.IntegerField(primary_key=True)
    name = models.CharField(max_length = 20)
    subject = models.CharField(max_length = 10)
    

class Subject(models.Model):
    name = models.CharField(max_length = 10)
    code = models.IntegerField()