from django.contrib import admin
from api.models import Post,Like


@admin.register(Post)
class AdminPost(admin.ModelAdmin):
    list_display=['id','title','post','created','updated','user']
    
@admin.register(Like)
class AdminLike(admin.ModelAdmin):
    list_display=['liked_by','post_by']
    