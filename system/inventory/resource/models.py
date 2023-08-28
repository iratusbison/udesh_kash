from django.db import models
#from login_system.models import CustomUser

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    #created_by = models.ForeignKey(CustomUser, on_delete = models.SET_NULL, null = True, related_name = 'created_products')
    
    def __str__(self):
        return self.name
