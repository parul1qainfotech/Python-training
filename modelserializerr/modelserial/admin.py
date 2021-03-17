from django.contrib import admin
from modelserial.models import Details
# Register your models here.

class AdminDetail(admin.ModelAdmin):
    list_display=['id','name','age','roll','city']
    
    
admin.site.register(Details,AdminDetail)
