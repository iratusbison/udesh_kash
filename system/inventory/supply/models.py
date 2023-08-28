from django.db import models
from resource.models import Product
#from login_system.models import CustomUser

class Supply(models.Model):
    resource = models.ForeignKey(Product, on_delete=models.CASCADE)
    #price = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity_supplied = models.PositiveIntegerField()
    date_supplied = models.DateField(auto_now_add=True)
    #user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='supplies')
    #resource = models.ForeignKey(Product, on_delete=models.CASCADE,related_name='supplies')

    def __str__ (self):
        return f"{self.quantity_supplied} {self.resource.name} worth of {self.resource.price} supplied on {self.date_supplied}"