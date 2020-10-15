from django.shortcuts import render
from django.http import JsonResponse, HttpResponseBadRequest
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict
from qaplatform.models import Question, Answer, Comment
from qaauth.models import Profile, UserFollowing
from rest_framework.decorators import permission_classes, api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
import json
import copy
import requests
from enum import Enum
from .serializers import CurrentUserSerializer 

# class FollowUnfollow(Enum):
#     UNFOLLOW = 'unfollow'
#     FOLLOW = 'follow'

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def question_list(request):
    question_list = [{**i, 'username': User.objects.get(pk=i['user_id']).username} for i in Question.objects.all().values()]
    return Response({'questions': question_list})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def question_with_answer(request, question_id):
    answers = list(Answer.objects.filter(question=question_id).values())
    answer_with_comment = [
       {
           'comment': [{**comm, 'username': User.objects.get(pk=comm['user_id']).username} for comm in Comment.objects.filter(answer=ans['id']).values()],
           'username': User.objects.get(pk=ans['user_id']).username,
            **ans
        }for ans in answers 
    ]
    question = [{**que, 'username': User.objects.get(pk=que['user_id']).username} for que in Question.objects.filter().values()][0]

    return Response({'question': question, 'answers': answer_with_comment})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def post_answer(request):
    try:
        body = request.data
        question_id = body['question_id']
        answer = body['answer']
        user_id = body['user_id']
        question = Question.objects.get(pk=question_id)
        user = User.objects.get(pk=user_id)
        a = Answer(answer=answer, question=question, user=user)
        a.save()
        # return question_with_answer(request, question_id)
        r = requests.get(f'http://localhost:8000/api/question-answer-list/{question_id}', 
        headers={'Authorization': f'Bearer {request.auth.token.decode()}'}).json()
        return Response(r)
    except:
        return HttpResponseBadRequest()

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def post_question(request):
    try:
        body = request.data
        question = body['question']
        user_id = body['user_id']
        user = User.objects.get(pk=user_id)
        q = Question(question=question, user=user)
        q.save()
        r = requests.get('http://localhost:8000/api/question-list', 
        headers={'Authorization': f'Bearer {request.auth.token.decode()}'}).json()
        return Response(r)
    except:
        return HttpResponseBadRequest()

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def post_comment(request):
    try:
        body = request.data
        comment = body['comment']
        user_id = body['user_id']
        answer_id = body['answer_id']
        question_id = body['question_id']
        user = User.objects.get(pk=user_id)
        answer = Answer.objects.get(pk=answer_id)
        c = Comment(answer=answer, user=user, comment=comment)
        c.save()
        r = requests.get(f'http://localhost:8000/api/question-answer-list/{question_id}', 
        headers={'Authorization': f'Bearer {request.auth.token.decode()}'}).json()
        return Response(r)
    except:
        return HttpResponseBadRequest()


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_profile(request, user_id):
    try: 
        user = User.objects.get(id=user_id)
        profile = Profile.objects.get(pk=user_id)
        following = list(profile.following.all().values())
        follower = list(profile.followers.all().values())
        serialized_user = CurrentUserSerializer(user)
        user_questions = list(Question.objects.filter(user=user_id).values())
        user_answers = list(Answer.objects.filter(user=user_id).values())
        return Response({
            'user': serialized_user.data,
            'questions': user_questions,
            'answers': user_answers,
            'follower': follower,
            'following': following,
            })
    except:
        return HttpResponseBadRequest()


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def follow_unfollow(request):
    try:
        flag, user_id = request.data.values()
        current_user = Profile.objects.get(pk=user_id) 
        loggedin_user = Profile.objects.get(pk=request.auth['user_id'])
        
        if flag == 'FOLLOW':
            UserFollowing.objects.create(profile=loggedin_user,
            profile_following=current_user)
            r = requests.get(f'http://localhost:8000/api/profile-info/{user_id}/', 
            headers={'Authorization': f'Bearer {request.auth.token.decode()}'}).json()
            return Response(r)
        if flag == 'UNFOLLOW':
            UserFollowing.objects.get(profile=loggedin_user,
            profile_following=current_user).delete()
            r = requests.get(f'http://localhost:8000/api/profile-info/{user_id}/', 
            headers={'Authorization': f'Bearer {request.auth.token.decode()}'}).json()
            return Response(r)
    except:
        return HttpResponseBadRequest()


    @api_view(['POST'])
    @permission_classes([IsAuthenticated])
    def upvote_downvote(request):
        def section_checker(section, section_id):
            # Question.objects.get(pk=section_id).upvote=User.objects.get(pk=request.auth['user_id'])
            return {
                'question': 'question',
                'answer': 'answer',
                'comment': 'comment',
            }[section]
        try:
            flag, section, section_id = request.data.value()
            if flag == 'UPVOTE':
                section_checker(section, section_id)
            if flag == 'DOWNVOTE':
                section_checker(section, section_id)
        except:
            pass