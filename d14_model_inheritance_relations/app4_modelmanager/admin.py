from django.contrib import admin
from app4_modelmanager.models import Student,Teacher,ExamCenter,MyExamCenter
# Register your models here.
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(ExamCenter)
admin.site.register(MyExamCenter)