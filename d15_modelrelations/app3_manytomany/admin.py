from django.contrib import admin
from app3_manytomany.models import User,Song

# Register your models here.
admin.site.register(User)

@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ['title','duration','singer']