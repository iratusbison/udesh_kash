from django.shortcuts import redirect, render
from .forms import SupplyForm
from resource.models import Product
from .models import Restock

def restock_resource(request):
    if request.method == 'POST':
        form = SupplyForm(request.POST)
        if form.is_valid():
            supply = form.save()
            resource = supply.resource 
            resource.quantity += supply.quantity_refilled
            #total_cost = Product.price * Product.qunatity
            #resource.price += total_cost
            resource.save()
            return redirect('restock_list')
    else:
        form = SupplyForm()
    return render(request, 'restock_form.html',{'form':form})

def restock_list(request):
    supplies = Restock.objects.all
    return render(request,'restock_list.html',{'supplies':supplies})
