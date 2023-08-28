from django.shortcuts import redirect, render
from .forms import SupplyForm
from resource.models import Product
from .models import Supply

def supply_resource(request):
    if request.method == 'POST':
        form = SupplyForm(request.POST)
        if form.is_valid():
            supply = form.save()
            resource = supply.resource 
            resource.quantity -= supply.quantity_supplied
            resource.save()
            return redirect('supply_list')
    else:
        form = SupplyForm()
    return render(request, 'supply_form.html',{'form':form})

def supply_list(request):
    supplies = Supply.objects.all
    return render(request,'supply_list.html',{'supplies':supplies})
