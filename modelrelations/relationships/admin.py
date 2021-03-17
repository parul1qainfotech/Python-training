from django.contrib import admin
from .models import Page
# Register your models here.

# @admin.register(Page)
# class PageAdmin(admin.ModelAdmin):
#     list_display=['page_name','page_cat','page_publish_date','user']
    

# @admin.register(Like)
# class LikeAdmin(admin.ModelAdmin):
#     list_display=['newpage','page_name','page_cat','page_publish_date','user','likes']

@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display=['user','page_no','pages_title','page_publish_date']