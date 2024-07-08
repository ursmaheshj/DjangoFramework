from django.contrib import admin

# Register your models here.
from app1_listview.models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id','name','roll','course']