
from rest_framework import serializers
from toowitter_api.models import Tweet, View, Like, User


class TweetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tweet
        fields = ['id', 'text', 'user', ]


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'username', 'email', 'bio', ]
