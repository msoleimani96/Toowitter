from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import permissions, status
from rest_framework.response import Response
from serializers import TweetSerializer, UserSerializer
from .models import *
from django.core.paginator import Paginator


class TweetApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = request.user
        tweets = Tweet.objects.filter(user=user)
        serializer = TweetSerializer(tweets, many=True)
        paginated_data = Paginator(serializer.data, 10)
        return Response(paginated_data)
