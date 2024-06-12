from django.contrib import admin
from app4_examples.models import User,Page,Post,Song

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username']

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title','publish','publish_in','user']

@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ['pagename','publish','user']

@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ['name','duration','sung_by']

