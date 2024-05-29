from django.contrib import admin
from app3.models import Student
# Register your models here.
# admin.site.register(Student)

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id','name','city','marks','passdate','admdatetime']