from django.contrib import admin
from resource.inventory.models import Product
from resource.staff.models import Staff

admin.site.register(Product)
admin.site.register(Staff)
# Register your models here.
