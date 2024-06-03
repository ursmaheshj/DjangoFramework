from django.contrib import admin
from app1_inheritance.models import CommonInfo,Student,Teacher,Contractor

# Register your models here.
# admin.site.register(CommonInfo)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Contractor)
