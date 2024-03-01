from django.contrib import admin
from .models import Student,Teacher,Subject

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ['name','division','about']

admin.site.register(Student,StudentAdmin)
admin.site.register(Teacher)
admin.site.register(Subject)
