from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

# Create your views here.
def views_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home-page')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

def views_signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home-page')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})

def views_logout(request):
    if request.method == 'POST':
        logout(request)
    return redirect('home-page')