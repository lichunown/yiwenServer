from django.db import models
from django.utils import timezone

# Create your models here.

class Question(models.Model):
    createuser = models.ForeignKey('m_user.m_User')
    title = models.CharField(max_length=200)
    body = models.TextField()
    time = models.DateTimeField(default=timezone.now)

class Answer(models.Model):
    createuser = models.ForeignKey('m_user.m_User')
    question = models.ForeignKey('Question')
    body = models.TextField()
    time = models.DateTimeField(default=timezone.now)

class AComment(models.Model):
    createuser = models.ForeignKey('m_user.m_User')
    answer = models.ForeignKey('Answer')
    body = models.TextField()
    time = models.DateTimeField(default=timezone.now)