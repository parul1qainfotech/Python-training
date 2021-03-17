from django.db import models
from django.contrib.auth.models import User
# Create your models here.

#one to one 
# class Page(models.Model):
#     user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True,limit_choices_to={'is_staff':True})
#     page_name=models.CharField(max_length=70)
#     page_cat=models.CharField(max_length=70)
#     page_publish_date=models.DateField()
    
# class Like(models.Model):
#     newpage=models.OneToOneField(Page,on_delete=models.CASCADE,primary_key=True,parent_link=True)
#     likes=models.IntegerField()


#many to one 

class Page(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    page_no=models.IntegerField()
    page_title=models.CharField(max_length=70)
    page_publish_date=models.DateTimeField()
    
    