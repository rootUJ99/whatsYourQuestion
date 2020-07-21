from django.urls import path

from . import views

app_name = 'qaauth'
urlpatterns = [
    path('login/', views.sign_in, name='login'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.logout_user, name='logout'),
]
