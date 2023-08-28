from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import Staff

def staff_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('Staff')
        else:
            return render(request, 'staff/login.html', {'error': 'Invalid login credentials'})
    return render(request, 'staff/login.html')

@login_required
def staff_profile(request):
    staff = request.user
    staff = Staff.objects.get(username=request.user.username)
    return render(request, 'staff/profile.html', {'staff': staff})
