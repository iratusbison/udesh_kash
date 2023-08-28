from django.contrib import admin
from .models import Product, ReplenishmentOrder, Profile, Supply

admin.site.register(Product)
admin.site.register(ReplenishmentOrder)
admin.site.register(Profile)
admin.site.register(Supply)


