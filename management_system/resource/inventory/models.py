from django.utils import timezone
from django.db import models

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    quantity = models.PositiveBigIntegerField()
    price = models.DecimalField(max_digits=8,decimal_places=2)
    total_price = models.DecimalField(max_digits=10, decimal_places=2,null=True,editable=False)
    last_purchase = models.DateTimeField(default=timezone.now, editable=False)
    

    def __str__ (self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.total_price = self.price * self.quantity
        super().save(*args, **kwargs)

      
 