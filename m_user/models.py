# -*- coding:utf-8 -*-
from __future__ import unicode_literals
# from django.utils.encoding import smart_unicode
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils import timezone




USERCHOICES = (
    ('0','normal'),
    ('1','craftsman'),
)
SEXCHOICES = (
    ('M','Male'),
    ('F','Female'),
)


class m_User(models.Model):
    username = models.CharField(max_length=50)
    pwd = models.CharField(max_length=33)
    isvip = models.CharField(max_length=1,choices=USERCHOICES, default='0')
    nickname = models.CharField(max_length=30,blank=True,default=None,null=True)
    truename = models.CharField(max_length=20,blank=True,default=None,null=True)
    birthday = models.DateField(default=timezone.now)
    sex = models.CharField(max_length=1,default=None,choices=SEXCHOICES,null=True,blank=True)
    tel = models.CharField(max_length=11,blank=True,default=None,null=True)
    email = models.CharField(max_length=40,blank=True,default=None,null=True)
    address = models.CharField(max_length=100,blank=True,default=None,null=True)
    page = models.CharField(max_length=100,blank=True,default=None,null = True)
    information = models.TextField(blank=True,default=None,null=True)
    bindQQ = models.CharField(max_length=20,blank=True,default=None,null=True)
    bindMobilephone = models.CharField(max_length=11,blank=True,default=None,null=True)
    agreenum = models.IntegerField(default = 0)
    opposenum = models.IntegerField(default = 0)
    focusPeople = models.ManyToManyField('m_User',blank=True,default=None)
    focusColumn = models.ManyToManyField('passage.Column',blank=True,default=None)
    # def __unicode__(self):
    #     return smart_unicode(self.username)



