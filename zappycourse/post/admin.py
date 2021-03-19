from django.contrib import admin
from post.models import Post,Vote

# Register your models here.
@admin.register(Post)

class PostAdmin(admin.ModelAdmin):
    list_display=['id','title','url','poster','created']

@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    list_display=['id','voter','post']
    
    
