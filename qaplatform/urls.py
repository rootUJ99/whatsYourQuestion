from django.urls import path

from . import views

urlpatterns = [
    path('', views.ask_question, name='question'),
    path('questions/', views.list_of_questions, name='home'),
    path('answer/<int:question_id>/', views.answer_for_question, name='answer'),
    path('search/<param>/', views.search_questions, name='search'),
]