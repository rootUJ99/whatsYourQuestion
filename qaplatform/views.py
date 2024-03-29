from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse, HttpResponseBadRequest
from django.contrib.admin.views.decorators import staff_member_required
from django.utils import timezone
from .models import Question, Answer
from .form import QuestionForm, AnswerForm, SearchQuestion
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.contrib.auth.models import User
import json
# Create your views here.


@csrf_protect
def ask_question(request):
    print(request.method)
    qlist = list(Question.objects.all().values())
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

@staff_member_required(login_url='/uaa/login')
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



# rest apis

def question_list(request):
    print(request.method)
    question_list = list(Question.objects.all().values())
    return JsonResponse({'questions': question_list})


def question_with_answer(request, question_id):
    answers = list(Answer.objects.filter(question=question_id).values())
    question = list(Question.objects.filter(pk=question_id).values())[0]
    return JsonResponse({'question': question, 'answers': answers})

@csrf_exempt
def post_answer(request):
    if request.method == 'POST':
        answer_date = timezone.now()
        try:
            body_unicode = request.body.decode('utf-8')
            body = json.loads(body_unicode)
            question_id = body['question_id']
            answer = body['answer']
            user_id = body['user_id']
            question = Question.objects.get(pk=question_id)
            user = User.objects.get(pk=user_id)
            a = Answer(answer=answer, answer_date=answer_date, question=question, user=user)
            a.save()
            return question_with_answer(request, question_id)
        except:
            return HttpResponseBadRequest()
@csrf_exempt
def post_question(request):
    if request.method == 'POST':
        try:
            question_date = timezone.now()
            body_unicode = request.body.decode('utf-8')
            body = json.loads(body_unicode)
            question = body['question']
            user_id = body['user_id']
            user = User.objects.get(pk=user_id)
            q = Question(question=question, question_date=question_date, user=user)
            q.save()
            return question_list(request)
        except:
            return HttpResponseBadRequest()
