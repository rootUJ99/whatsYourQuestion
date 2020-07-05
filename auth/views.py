from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm 

# Create your views here.
def login(request):
    form = AuthenticationForm()
    return render(request, 'qaplatform/login.html', {'form': form})

def register(request):
    form = UserCreationForm()
    return render(request, 'qaplatform/register.html', {'form': form})