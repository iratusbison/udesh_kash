'''
from celery import shared_task
from .models import Product, ReplenishmentOrder, Profile

@shared_task
def monitor_stock_levels():
    products = Product.objects.all()

    for product in products :
        if product.stock_level < 10:
            trigger_replenishment.delay(product.id)

@shared_task
def trigger_replenishment(product_id, profile_id):
    product = Product.objects.get(id=product_id)
    supplier = "supplier name"
    order_quantity = 100

    replenishment_order = ReplenishmentOrder.objects.create(
        product = product,
        supplier = supplier,
        status = "pending"
    )

    product.stock_level += order_quantity
    product.save()

    profile = Profile.objects.get(id= profile_id)
    profile.supply_level += order_quantity
    profile.save()

    return replenishment_order.id
'''
