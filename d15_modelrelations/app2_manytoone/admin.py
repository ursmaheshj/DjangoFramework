from django.contrib import admin
from app2_manytoone.models import User,Post

# Register your models here.
admin.site.register(User)
# admin.site.register(Post)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title','description','user','publish']