from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from django import forms

class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
    
    username = forms.CharField(label= '',widget=forms.TextInput(
        attrs={'class': 'form_input', 'placeholder': 'Enter USername', }))
    password = forms.CharField(label= '',widget=forms.PasswordInput(
        attrs={'class': 'form_input', 'placeholder': 'Enter Password',}))

class RegisterForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
    
    username = forms.CharField(label= '',widget=forms.TextInput(
        attrs={'class': 'form_input', 'placeholder': 'Enter USername', }))
    password1 = forms.CharField(label= '',widget=forms.PasswordInput(
        attrs={'class': 'form_input', 'placeholder': 'Enter Password',}))
    password2 = forms.CharField(label= '',widget=forms.PasswordInput(
        attrs={'class': 'form_input', 'placeholder': 'Confirm Password',}))