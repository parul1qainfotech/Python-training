from django.db import models

# Create your models here.
class Details(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    roll=models.IntegerField()
    city=models.CharField(max_length=100)
    
    