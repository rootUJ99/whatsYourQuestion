from django.shortcuts import render
from django.http import JsonResponse, HttpResponseBadRequest
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from qaplatform.models import Question, Answer, Comment
from rest_framework.decorators import permission_classes, api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
import json

def bodyUnicodeHelper(req):
    body_unicode = req.body.decode('utf-8')
    return json.loads(body_unicode)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def question_list(request):
    print(request.method)
    question_list = list(Question.objects.all().values())
    return Response({'questions': question_list})


def question_with_answer(request, question_id):
    answers = list(Answer.objects.filter(question=question_id).values())
    answer_with_comment = [
       {'comment': list(Comment.objects.filter(answer=ans['id']).values()), **ans} for ans in answers 
    ]
    question = list(Question.objects.filter(pk=question_id).values())[0]
    return JsonResponse({'question': question, 'answers': answer_with_comment})

@csrf_exempt
def post_answer(request):
    if request.method == 'POST':
        answer_date = timezone.now()
        try:
            body = bodyUnicodeHelper(request)
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
            body = bodyUnicodeHelper(request)
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
        try:
            comment_date = timezone.now()
            body = bodyUnicodeHelper(request)
            comment = body['comment']
            user_id = body['user_id']
            answer_id = body['answer_id']
            question_id = body['question_id']
            user = User.objects.get(pk=user_id)
            answer = Answer.objects.get(pk=answer_id)
            c = Comment(comment_date=comment_date, answer=answer, user=user, comment=comment)
            c.save()
            return question_with_answer(request, question_id)
        except:
            return HttpResponseBadRequest()