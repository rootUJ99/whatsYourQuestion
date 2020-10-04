from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import CustomTokenObtainPairSerializer


@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'},
                        status=HTTP_404_NOT_FOUND)
    token = CustomTokenObtainPairSerializer(user).get_token(user)
    
    # token, _ = Token.objects.get_or_create(user=user)
    return Response({
        'token': str(token.access_token),
        'refreshToken': str(token),
        }, status=HTTP_200_OK)


@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def register(request):
    email = request.data.get("email")
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None or email is None:
        return Response({'error': 'Please Enter the registration details'},
                        status=HTTP_400_BAD_REQUEST)
    user = User.objects.create_user(username=username, email=email, password=password)
    token = CustomTokenObtainPairSerializer(user).get_token(user)
    return Response({
        'token': str(token.access_token),
        'refreshToken': str(token),
        }, status=HTTP_200_OK)