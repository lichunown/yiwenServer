from django.db import models
from django.utils import timezone


        

class Column(models.Model):
    createuser = models.ForeignKey('m_user.m_User')
    createdate = models.DateTimeField(default=timezone.now)
    infomation = models.TextField(blank=True,null=True)

class Passage(models.Model):
    m_user = models.ForeignKey('m_user.m_User')
    column = models.ForeignKey('Column',blank = True,default=None)
    title = models.CharField(max_length=100)
    body = models.TextField()
    time = models.DateTimeField(default=timezone.now)
    # def __unicode__(self):
    #     return smart_unicode(self.title)    


    
