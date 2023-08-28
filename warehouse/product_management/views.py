
from django.shortcuts import redirect, render
from  .models import Product, ReplenishmentOrder, Profile
#from .tasks import monitor_stock_levels, trigger_replenishment
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required


@login_required
def product_list (request):
    products = Product.objects.all()
    return render(request,'product_list.html',{'products':products})

@login_required
def replenishment_order_list(request):
    orders = ReplenishmentOrder.objects.all()
    return render (request,'replenishment_order_list.html',{'orders':orders})

@login_required
def create_replenishment_order(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        profile_id = request.user.profile.id
        #trigger_replenishment.delay(product_id, profile_id)
        return redirect('replenishment_order_list')
    
    products = Product.objects.all()
    return render(request, 'create_replenishment_order.html',{'products':products})
        

def profile_detail(request):
    profile = request.user.profile
    return render(request,'profile_detail.html',{'profile':profile})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username = username, password = password)
            if user is not None :
                login(request, user)
                return redirect (get_redirect_url(user))
            else:
                return render(request, 'login.html',{'form':form,'error_message':'Invalid credentials'})
        else:
            return render(request, 'login.html',{'form':form , 'error_message':'invalid form data'})
    else:
        form = AuthenticationForm()
        return render(request,'login.html',{'form':form})
    
def get_redirect_url(user):
    if user.profile.role == 'replenishment_order_list':
        return 'replenishment_order_list'
    elif user.profile.role == 'create_replenishment_order':
        return 'create_replenishment_order'
    elif user.profile.role == 'product_list':
        return 'product_list'
    else : return profile_detail
