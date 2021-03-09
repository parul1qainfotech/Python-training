from django.contrib import admin
from .models import Blog
# Register your models here.

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    display_list=['id','title','description']