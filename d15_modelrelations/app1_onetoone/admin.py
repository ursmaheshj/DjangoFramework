from django.contrib import admin
from app1_onetoone.models import Husband,Wife,UserModel,Page,Like

# Register your models here.
admin.site.register(Husband)
admin.site.register(Wife)
admin.site.register(UserModel)
admin.site.register(Page)
admin.site.register(Like)
