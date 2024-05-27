from django.contrib import admin
from app1.models import Student,Teacher

# Register your models here.
admin.site.register(Student)
admin.site.register(Teacher)

# @admin.register(Student)
# class StudentAdmin(admin.ModelAdmin):
#     list_display = ['roll','name']