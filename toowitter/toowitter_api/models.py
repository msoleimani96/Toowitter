from django.db import models


class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    username = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=40)
    bio = models.CharField(max_length=128)


class Tweet(models.Model):
    text = models.CharField(max_length=512)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class View(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE)


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE)
