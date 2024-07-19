from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import permissions, status
from rest_framework.response import Response
from toowitter_api.serializers import TweetSerializer, UserSerializer
from toowitter_api.models import *
from rest_framework.decorators import api_view, schema
from django.contrib.auth.hashers import make_password


class TweetApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = request.user
        tweets = Tweet.objects.filter(user=user)
        serializer = TweetSerializer(tweets, many=True)
        return Response(serializer.data)


@api_view(['POST'])
def register(request):
    name = request.data.get('name')
    email = request.data.get('email')
    password = request.data.get('password')
    username = request.data.get('username')
    bio = request.data.get('bio')

    user = User.objects.create_user(
        name=name, email=email, password=password, username=username, bio=bio)
    return Response({"token": Token.objects.get_or_create(user=user)[0].key})


@api_view(['POST'])
def login(request):
    email = request.data.get('email')
    password = request.data.get('password')
    username = request.data.get('username')

    if username is not None:
        user = User.objects.get(username=username)
    elif email is not None:
        user = User.objects.get(email=email)
    else:
        return Response({"message": "You should provide your email or username to login."})

    if password is not None and user.check_password(password):
        return Response({"token": Token.objects.get_or_create(user=user)[0].key})
    else:
        if password is None:
            return Response({"message": "You should provide your password to login."})
        else:
            return Response({"message": "Password is incorrect."})
