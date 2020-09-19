from django.shortcuts import render
from django.http import JsonResponse, HttpResponseBadRequest
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from qaplatform.models import Question, Answer, Comment
from qaauth.models import Profile
from rest_framework.decorators import permission_classes, api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
import json
import copy
import requests

def bodyUnicodeHelper(req):
    body_unicode = req.body.decode('utf-8')
    return json.loads(body_unicode)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def question_list(request):
    question_list = list(Question.objects.all().values())
    return Response({'questions': question_list})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def question_with_answer(request, question_id):
    answers = list(Answer.objects.filter(question=question_id).values())
    answer_with_comment = [
       {'comment': list(Comment.objects.filter(answer=ans['id']).values()), **ans} for ans in answers 
    ]
    question = list(Question.objects.filter(pk=question_id).values())[0]
    return Response({'question': question, 'answers': answer_with_comment})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def post_answer(request):
    answer_date = timezone.now()
    try:
        body = request.data
        question_id = body['question_id']
        answer = body['answer']
        user_id = body['user_id']
        question = Question.objects.get(pk=question_id)
        user = User.objects.get(pk=user_id)
        a = Answer(answer=answer, answer_date=answer_date, question=question, user=user)
        a.save()
        # return question_with_answer(request, question_id)
        r = requests.get(f'http://localhost:8000/api/question-answer-list/{question_id}', headers={'Authorization': f'{request.authenticators[0].keyword} {request.auth.key}'}).json()
        return Response(r)
    except:
        return HttpResponseBadRequest()

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def post_question(request):
    try:
        question_date = timezone.now()
        body = request.data
        question = body['question']
        user_id = body['user_id']
        user = User.objects.get(pk=user_id)
        q = Question(question=question, question_date=question_date, user=user)
        q.save()
        r = requests.get('http://localhost:8000/api/question-list', headers={'Authorization': f'{request.authenticators[0].keyword} {request.auth.key}'}).json()
        return Response(r)
    except:
        return HttpResponseBadRequest()

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def post_comment(request):
    try:
        comment_date = timezone.now()
        body = request.data
        comment = body['comment']
        user_id = body['user_id']
        answer_id = body['answer_id']
        question_id = body['question_id']
        user = User.objects.get(pk=user_id)
        answer = Answer.objects.get(pk=answer_id)
        c = Comment(comment_date=comment_date, answer=answer, user=user, comment=comment)
        c.save()
        r = requests.get(f'http://localhost:8000/api/question-answer-list/{question_id}', headers={'Authorization': f'{request.authenticators[0].keyword} {request.auth.key}'}).json()
        return Response(r)
    except:
        return HttpResponseBadRequest()


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_question_answer(request, user_id):
    try: 
        user_questions = list(Question.objects.filter(user=user_id).values())
        user_answers = list(Answer.objects.filter(user=user_id).values())
        return Response({
            'questions': user_questions,
            'answers': user_answers
            })
    except:
        return HttpResponseBadRequest()
