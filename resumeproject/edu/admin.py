from django.contrib import admin
from edu.models import Skill
# Register your models here.

@admin.register(Skill)
class AdminSkills(admin.ModelAdmin):
    list_display=('id','skill','percent')