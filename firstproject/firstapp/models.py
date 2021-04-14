from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    product_id=models.AutoField(primary_key=True)
    product_name=models.CharField(ma_length=255)
    price=models.FloatField()
    
    def __str__(self):
        return self.product_name
    
class Cart(models.Model):
    cart_id=models.AutoField(primary_key=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    created_on=models.DateTimeField()
    
class ProductInCart(models.Model):
    class Meta:
        unique_together=(('cart','product'),)
        product_in_cart_id=models.AutoField(priary_key=True)
        cart=models.ForeignKey(Cart,on_delete=models.CASCADE)
        quantity=models.PositiveIntegerField()