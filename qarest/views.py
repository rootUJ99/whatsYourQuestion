from django.http.response import HttpResponseBadRequest
from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict
from qaplatform.models import Question, Answer, Comment, Vote
from qaauth.models import Profile, UserFollowing
from rest_framework.decorators import permission_classes, api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from operator import itemgetter
import json
import copy
import requests
from enum import Enum
from .serializers import CurrentUserSerializer 

def request_API(req, method, path, param=None):
    proto = req.is_secure() and 'https' or 'http'
    host = req.get_host()
    headers = {'Authorization': f'Bearer {req.auth.token.decode()}'}
    param = param and f'/{param}' or ''
    request_with_method = getattr(requests, method)
    r = request_with_method(f'{proto}://{host}/{path}{param}', headers=headers).json()
    return r

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def question_list(request):
    question_list = [{**i, 'username': User.objects.get(pk=i['user_id']).username} for i in Question.objects.order_by('-question_date').values()]
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
    question = [{**que, 'username': User.objects.get(pk=que['user_id']).username} for que in Question.objects.filter(pk=question_id).values()][0]

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
        r = request_API(request, 'get', 'api/question-answer-list', question_id)
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
        r = request_API(request, 'get', 'api/question-list')
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
        r = request_API(request, 'get', 'api/question-answer-list',question_id)
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
        dict_keys = ['flag', 'user_id']
        flag, user_id = itemgetter(*dict_keys)(request.data)
        current_user = Profile.objects.get(pk=user_id) 
        loggedin_user = Profile.objects.get(pk=request.auth['user_id'])
        
        if flag == 'FOLLOW':
            UserFollowing.objects.create(profile=current_user,
            profile_following=loggedin_user)
            r = request_API(request, 'get', 'api/profile-info',user_id)
            return Response(r)
        if flag == 'UNFOLLOW':
            UserFollowing.objects.get(profile=current_user,
            profile_following=loggedin_user).delete()
            r = request_API(request, 'get', 'api/profile-info',user_id)
            return Response(r)
    except KeyError:
            HttpResponseBadRequest('key error')
    except:
        return HttpResponseBadRequest()


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def vote(request):
    def section_checker(section):
        return {
            'question': Question,
            'answer': Answer,
            'comment': Comment,
        }[section]
    
    def vote_checker(flag, user):
        upvote_obj = {
            'upvote' : user
        }
        downvote_obj = {
            'downvote' : user
        }
        return {
            'UPVOTE': upvote_obj,
            'DOWNVOTE': downvote_obj,
        }[flag]
            
    try:
        dict_keys = ['flag', 'section', 'section_id', 'toggle']
        # flag, section, section_id, toggle = request.data.values()
        flag, section, section_id, toggle = itemgetter(*dict_keys)(request.data)
        user = User.objects.get(pk=request.auth['user_id'])
        section = section_checker(section)
        if toggle == True:
            vote_user = vote_checker(flag, user) 
            vote = Vote.objects.get_or_create(**vote_user)
            section_obj = getattr(section, 'objects')
            section_obj.get(pk=section_id).vote = vote[0]
            section_obj.save()
            r = request_API(request, 'get', 'api/question-answer-list', question_id)
            return Response(r)
        if toggle == False:
            section_obj = getattr(section, 'objects')
            vote = section_obj.get(pk=section_id).vote
            Vote.objects.delete(vote)
            r = request_API(request, 'get', 'api/question-answer-list', question_id)
            return Response(r)
    except:
        return HttpResponseBadRequest()