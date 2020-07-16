from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.utils import timezone
from .models import Question, Answer
from .form import QuestionForm, AnswerForm, SearchQuestion
from django.views.decorators.csrf import csrf_protect

# Create your views here.


@csrf_protect
def ask_question(request):
    print(request.method)
    qlist = list(Question.objects.all())
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
    return render(request, 'question.html', {'form': form, 'qlist': qlist})


@csrf_protect
def answer_for_question(request, question_id):
    print(question_id, request.method)
    answers = Answer.objects.filter(question=question_id)
    question = Question.objects.get(pk=question_id)
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.cleaned_data['answer']
            answer_date = timezone.now()
            print(answer, answer_date, question)
            a = Answer(answer=answer, answer_date=answer_date, question=question)
            a.save()
            return HttpResponseRedirect('/questions/')
    else:
        form = AnswerForm()
    return render(
        request,
        'answer.html',
        {'form': form, 'question_id': question_id, 'answers': answers, 'question': question},
    )


def search_questions(request, param):
    print('param', param)
    if request.method == 'GET':
        if param:
            searched = list(Question.objects.filter(question__contains=param).values())
            # return render(request, 'list.html', {'qlist': searched, 'form': form})
            # return HttpResponseRedirect('/questions/')
            return JsonResponse({'searched': searched})
