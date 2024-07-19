from toowitter_api.views import *
from django.urls import path
from rest_framework.authtoken import views


urlpatterns = [
    path('', TweetApiView.as_view()),
    path('register', register),
    path('login', login)
]
