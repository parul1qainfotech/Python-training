from django.db import models
from django.conf import settings

def upload_update_image(instance,filename):
    return "updates/{user}/{filename}".format(user=instance.user,filename=filename)
class Update(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    content=models.TextField()
    image=models.ImageField(upload_to="upload_update_image")
    updated=models.DateTimeField(auto_now_add=True)
    timestamp=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.user )
    