from django.shortcuts import redirect, render
from .models import Product
from .forms import ProductForm

def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html',{'products':products})

def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
        
    else:
        form = ProductForm()
    return render(request, 'create_product.html',{'form':form})

def update_product(request, pk):
    product = Product.objects.get(pk=pk)
    if request.method =='POST':
        form = ProductForm(request.POST, instance= product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
        
    else:
        form = ProductForm(instance = product)
    return render(request,'update_product.html',{'form':form,'product':product})

def delete_product(request, pk):
    product = Product.objects.get(pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'delete_product.html',{'product': product})


