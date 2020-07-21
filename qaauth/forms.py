from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from django import forms

class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(AuthenticationForm, self).__init__(*args, **kwargs)
    
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'login_form', 'placeholder': 'Enter USername',}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'login_form', 'placeholder': 'Enter Password',}))

class RegisterForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
    
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'login_form', 'placeholder': 'Enter USername',}))
    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'login_form', 'placeholder': 'Enter Password',}))
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'login_form', 'placeholder': 'Confirm Password',}))