# controllers/auth_controller.py
from django.shortcuts import render, redirect
from crm.BL.auth_service import AuthService

def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        if AuthService.login_user(request, email, password):
            return redirect('dashboard')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')

def logout_view(request):
    AuthService.logout_user(request)
    return redirect('login')

def register_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = AuthService.register_user(email, password)
        if user:
            return redirect('login')
        else:
            return render(request, 'register.html', {'error': 'User already exists'})
    return render(request, 'register.html')
