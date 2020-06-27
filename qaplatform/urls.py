from django.urls import path

from . import views

urlpatterns = [
    path('', views.ask_question, name='home'),
    path('home/', views.list_of_questions, name='home0'),
]