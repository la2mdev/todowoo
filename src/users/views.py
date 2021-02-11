from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib import messages
from .forms import SignUpForm, LoginForm


def signup_view(request):
    if request.user.is_authenticated:
        return redirect('index')
    
    form = SignUpForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        user = form.save()

        if user:
            login(request, user)
            messages.success(request, 'Usuario creado exitosamente!')
            return redirect('index')

    context = {'form': form}
    return render(request, 'users/authentication_form.html', context)


def login_view(request):
    if request.user.is_authenticated:
        return redirect('index')

    form = LoginForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        user = form.save()

        if user:
            login(request, user)
            messages.success(request, 'Sesion iniciada correctamente!')
            return redirect('index')
    
    context = {'form': form}
    return render(request, 'users/authentication_form.html', context)


def logout_view(request):
    if not request.user.is_authenticated:
        return redirect('index')
    
    if request.method == 'POST':
        logout(request)
        return redirect('index')
