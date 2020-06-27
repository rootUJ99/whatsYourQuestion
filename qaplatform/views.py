from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.utils import timezone
from .models import Question, Answer
from .form import QuestionForm, AnswerForm
from django.views.decorators.csrf import csrf_protect
# Create your views here.

@csrf_protect
def ask_question(request):
  if request.method == 'POST':
    form = QuestionForm(request.POST)
    if form.is_valid():
        question = form.cleaned_data['question']
        question_date = timezone.now()
        print(question)
        q = Question(question=question, question_date=question_date)
        q.save()
  else:
    form = QuestionForm()
  return render(request, 'qaplatform/form.html', {'form': form})

def list_of_questions(request):
  qlist = list(Question.objects.all())
  print(qlist)

  return render(request, 'qaplatform/list.html', {'qlist': qlist})