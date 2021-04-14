from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title=models.CharField(max_length=100)
    post=models.TextField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user)
    
class Like(models.Model):
    liked_by=models.ForeignKey(User,on_delete=models.CASCADE)
    post_by=models.ForeignKey(Post,on_delete=models.CASCADE)
