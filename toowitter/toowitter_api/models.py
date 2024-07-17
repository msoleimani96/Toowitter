from django.db import models
import datetime


class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    username = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=40)
    bio = models.CharField(max_length=128)

    def __str__(self):
        return self.email


class Tweet(models.Model):
    id = models.AutoField(primary_key=True)
    text = models.CharField(max_length=512)
    date = models.DateField(default=datetime.date.today)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.text[:20]


class View(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE)


class Like(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE)
