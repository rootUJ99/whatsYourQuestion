from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect

# Create your views here.
def sign_in(request):
    if request.user.is_authenticated == True:
        return redirect('/')
    if request.method == 'POST':
        form = LoginForm(request=request, data=request.POST)
        print(form.is_valid())
        if form.is_valid():
            print(form.cleaned_data)
            username, password = form.cleaned_data.values()
            print(authenticate(username=username, password=password), username, password)
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
        return redirect('qaauth:register')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def register(request):
    if request.user.is_authenticated == True:
        return redirect('/')
    form = RegisterForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            print(form.cleaned_data)
            return redirect('/')
    else:
        form = RegisterForm()

    return render(request, 'register.html', {'form': form})

def profile(request):
    if request.user.is_authenticated == False:
        return redirect('/uaa/login')
    print('auth', User.is_authenticated)
    return render(request, 'profile.html')

def logout_user(request):
    logout(request)
    return redirect('/')
