from django.db import models
#from login_system.models import CustomUser
from resource.models import Product

class Restock(models.Model):
    resource = models.ForeignKey(Product, on_delete=models.CASCADE)
    #price = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity_refilled = models.PositiveIntegerField()
    date_supplied = models.DateField(auto_now_add=True)
    #user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='restocks')
    #resource = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='restocks')

    def __str__ (self):
        return f"{self.quantity_refilled} {self.resource.name} worth of {self.resource.price} supplied on {self.date_supplied}"