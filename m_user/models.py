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
    # def __unicode__(self):
    #     return smart_unicode(self.username)



# # Create your models here.

# PROJECT_STATUS=(
#     ('1','准备中'),
#     ('2','初期'),
#     ('3','中期'),
#     ('4','后期'),
#     ('5','已结束'),
# )
# INVITATION_STATUS=(
#     ('1','未阅读'),#students send to tutors
#     ('2','已阅读'),#students send to tutors
#     ('3','已接受'),
#     ('4','未接受'),
#     ('a','未阅读'),#student&tutors send to students
#     ('b','已阅读'),
#     ('c','已接受'),
#     ('d','未接受'),
# )
# TAG_CHOICE=(
#     ('gc','国创'),
#     ('yjs','研究生'),
#     ('qt','其他'),
# )
# TITLE_CHOICE=(
#     ('js','教授'),
#     ('fj','副教授'),
#     ('qt','其他'),
# )
# class Student(models.Model):
#     username=models.OneToOneField(User)
#     sid=models.CharField(max_length=11)
#     truename=models.CharField(max_length=50)
#     birthday=models.DateField(timezone.now,blank=True,null=True)
#     college=models.CharField(max_length=50,choices=COLLEGES)#need add limit
#     major=models.CharField(max_length=50,blank=True,null=True)#need add limit
#     introduction=models.TextField(blank=True,null=True)
#     img = models.ImageField(upload_to = 'media/', default = 'media/default/no-img.jpg')
#     def __unicode__(self):
#         return smart_unicode(self.sid)


# class Tutor(models.Model):
#     username=models.OneToOneField(User)
#     truename=models.CharField(max_length=50,blank=True,null=True)
#     jobtitle=models.CharField(max_length=3,choices=TITLE_CHOICE,blank=True,null=True)
#     college=models.CharField(max_length=50,blank=True,choices=COLLEGES)#need add limit
#     introduction=models.TextField(blank=True,null=True)
#     def __unicode__(self):
#         return smart_unicode(self.truename)

# class Project(models.Model):
#     name=models.CharField(max_length=50,blank=True,null=True)
#     status=models.CharField(max_length=10,choices=PROJECT_STATUS)
#     startdate=models.DateField(timezone.now)   
#     students=models.ManyToManyField(Student)
#     tutors=models.ManyToManyField(Tutor,blank=True,null=True)
#     introduction=models.TextField()

#     def __unicode__(self):
#         return smart_unicode(self.name)

# class Invitation(models.Model):
#     student=models.OneToOneField('Student')
#     tutor=models.OneToOneField('Tutor',blank=True,null=True)
#     project=models.OneToOneField('Project')    
#     tag=models.CharField(max_length=3,choices=TAG_CHOICE)
#     status=models.CharField(max_length=10,choices=INVITATION_STATUS)
#     invitetext=models.TextField(blank=True,null=True)


