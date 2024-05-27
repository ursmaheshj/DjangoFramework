from django.contrib import admin
from app1.models import Student

# Register your models here.
admin.site.register(Student)

# @admin.register(Student)
# class StudentAdmin(admin.ModelAdmin):
#     list_display = ['roll','name']