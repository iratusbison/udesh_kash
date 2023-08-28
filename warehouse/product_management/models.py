from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    supply_level = models.PositiveIntegerField(default=0)
    role = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.user.username
    
    
    
class Product(models.Model):
    name = models.CharField(max_length=100)
    sku = models.CharField(max_length=50)
    description = models.TextField()
    stock_level = models.PositiveIntegerField()

class ReplenishmentOrder(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    supplier = models.CharField(max_length=100)
    status = models.CharField(max_length=50)

class Supply (models.Model):
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    supply_date = models.DateTimeField(auto_now_add = True)
