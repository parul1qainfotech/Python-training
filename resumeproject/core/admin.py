from django.contrib import admin
from core.models import Contact
# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display=('id','name','email','subject','message')
    

admin.site.register(Contact,ContactAdmin)