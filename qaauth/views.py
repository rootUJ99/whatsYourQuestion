from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

# Create your views here.
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            user = authenticate(username='john', password='secret')
    else:
        form = AuthenticationForm()
    return render(request, 'qaplatform/login.html', {'form': form})

def register(request):
    form = UserCreationForm()
    if request.method == 'POST':
        if form.is_valid():
            user = User.objects.create_user()
            user.save()
        
    return render(request, 'qaplatform/register.html', {'form': form})