from django.shortcuts import render
from .models import FixedDeposit
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin

@login_required(login_url='base') 
def fixed_deposit_list(request):
    accounts = FixedDeposit.objects.all()
    return render(request, 'users/dashboard.html',{'accounts':accounts})

def base(request):
    return render(request, 'base.html')


'''
def portfolio_list(request):
    portfolios = Portfolio.objects.all()
    return render(request, 'portfolio/portfolio_list.html', {'portfolios': portfolios})

def portfolio_detail(request, pk):
    portfolio = Portfolio.objects.get(pk=pk)
    return render(request, 'portfolio/portfolio_detail.html', {'portfolio': portfolio})
'''


