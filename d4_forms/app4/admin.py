from django.contrib import admin
from app4.models import User
# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['student_name','teacher_name','email','password']