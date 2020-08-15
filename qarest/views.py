from django.shortcuts import render
from django.http import JsonResponse, HttpResponseBadRequest
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from qaplatform.models import Question, Answer
import json

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


@csrf_exempt
def post_comment(request):
    if request.method == 'POST':
        pass
            