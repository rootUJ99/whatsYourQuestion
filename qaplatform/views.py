from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.utils import timezone
from .models import Question, Answer
from .form import QuestionForm, AnswerForm
from django.views.decorators.csrf import csrf_protect
# Create your views here.

@csrf_protect
def ask_question(request):
    print(request.method)
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.cleaned_data['question']
            question_date = timezone.now()
            print(question)
            q = Question(question=question, question_date=question_date)
            q.save()
            return HttpResponseRedirect('/questions/')
    else:
        form = QuestionForm()
    return render(request, 'qaplatform/form.html', {'form': form})

def list_of_questions(request):
    qlist = list(Question.objects.all())
    print(qlist)
    return render(request, 'qaplatform/list.html', {'qlist': qlist})

@csrf_protect
def answer_for_question(request, question_id):
    print(question_id, request.method)
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.cleaned_data['answer']
            answer_date = timezone.now()
            question = Question.objects.get(pk=question_id)
            print(answer, answer_date, question)
            a = Answer(answer=answer, answer_date=answer_date, question=question)
            a.save()
            return HttpResponseRedirect('/questions/')
    else:
        form = AnswerForm()
    return render(request, 'qaplatform/answer.html', {'form': form, 'question_id':question_id})