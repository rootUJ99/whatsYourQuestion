from django.shortcuts import render
from .models import Question, Answer
from .form import QuestionForm, AnswerForm
import pdb
# Create your views here.

def index(req):

  context = {
    'question_form' : QuestionForm(req.POST),
    'answer_form' : AnswerForm(req.POST),
  }
  if req.method == 'POST':
    # form = QuestionForm(req.POST)
    if context['question_form'].is_valid():
      print(context['question_form'])
  else:
    form = QuestionForm()
  return render(req, 'qaplatform/index.html', { 'form': context})