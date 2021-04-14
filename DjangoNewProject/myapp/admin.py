from django.contrib import admin
from myapp.models import Update

@admin.register(Update)
class AdminUpdate(admin.ModelAdmin):
    list_display=['id','user','image','content','updated','timestamp']
