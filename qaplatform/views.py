from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.utils import timezone
from .models import Question, Answer
from .form import QuestionForm, AnswerForm
from django.views.decorators.csrf import csrf_protect
import pdb
# Create your views here.

@csrf_protect
def ask_question(request):
  if request.method == 'POST':
    # create a form instance and populate it with data from the request:
    form = QuestionForm(request.POST)
    # check whether it's valid:
    if form.is_valid():
        # process the data in form.cleaned_data as required
        # ...
        # redirect to a new URL:
        question = form.cleaned_data['question']
        question_date = timezone.now()
        print(question)
        q = Question(question=question, question_date=question_date)
        q.save()
      # return 

    # if a GET (or any other method) we'll create a blank form
  else:
    form = QuestionForm()
  return render(request, 'qaplatform/form.html', { 'form': form})