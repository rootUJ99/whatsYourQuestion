from django.shortcuts import render
from .models import Question, Answer
# Create your views here.

def index(req):

  context = {
    'qList' : Question.objects.values(),
    'aList' : Answer.objects.values()
  }
  print('context', context);
  return render(req, 'qaplatform/index.html', context )