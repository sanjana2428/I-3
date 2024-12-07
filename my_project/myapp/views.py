from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from .forms import RegistrationForm

def homepage(request):
    return render(request, 'homepage.html')

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('loginpage')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})

def loginpage(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('homepage')
    else:
        form = AuthenticationForm()
    return render(request, 'loginpage.html', {'form': form})
