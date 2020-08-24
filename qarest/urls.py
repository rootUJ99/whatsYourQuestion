from django.urls import path

from . import views

urlpatterns = [
    path('question-list', views.question_list),
    path('question-answer-list/<int:question_id>/', views.question_with_answer),
    path('post-answer', views.post_answer),
    path('post-question', views.post_question),
    path('post-comment', views.post_comment),
]