from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from crudwithfbv.models import User
# Register your models here.

class UserModelAdmin(UserAdmin):
    model = User
    list_display = ['id','email','city','is_active',
                    'is_superuser','is_staff','is_customer',
                    'is_seller']
    list_filter = ['is_superuser']
    fieldsets = [
        ("User Creds",{"fields":["email","password"]}),
        ("Personal details",{"fields":["city"]}),
        ("Permissions",{"fields":["is_active","is_staff",
                                  "is_seller","is_customer","is_superuser"]}),
    ]
    add_fieldsets = [
        (None,{
            'classes':['wide'],
            'fields':['email','password1','password2']
        })
    ]
    search_fields = ['email','city']
    ordering = ['email','id']
    filter_horizontal = []

admin.site.register(User,UserModelAdmin)