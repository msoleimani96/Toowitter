from toowitter_api.views import *
from django.urls import path


urlpatterns = [
    path('', TweetApiView.as_view()),
]
