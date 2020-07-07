from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect

# Create your views here.
def sign_in(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        print(form.is_valid())
        if form.is_valid():
            print(form.cleaned_data)
            username, password = form.cleaned_data
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
            return redirect('/')
        return redirect('auth:register')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def register(request):
    form = UserCreationForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            print(form.cleaned_data)
            return redirect('/')
    else:
        form = UserCreationForm()  
        
    return render(request, 'register.html', {'form': form})