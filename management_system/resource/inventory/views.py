from django.shortcuts import render, redirect
from resource.inventory.models import Product


def product_list(request):
    products = Product.objects.all()
    return render(request, 'inventory/product_list.html',{'products':products})

