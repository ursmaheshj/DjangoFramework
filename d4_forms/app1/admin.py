from django.contrib import admin
from app1.models import Student

# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Student._meta.get_fields()]
    # list_display = Student._meta.get_fields.__getattribute__()