from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm, CustomAuthenticationForm

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
        
        else:
            form = CustomUserCreationForm()
        return render(request, 'signup.html',{'form':form})
    
def user_login(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None :
                login(request, user)
                return redirect('products')
            else: 
                form.add_error(None, 'Invalid Username or Password')

    else:
        form = CustomAuthenticationForm()
    return render(request, 'login.html',{'form':form})
