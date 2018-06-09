from django.db import models

# Create your models here.

from django.utils import timezone


        

class Data(models.Model):
    # createuser = models.ForeignKey('m_user.m_User')
    # createdate = models.DateTimeField(default=timezone.now)
    name = models.CharField(max_length=100)
    data = models.TextField(blank=True,null=True)
    def __unicode__(self):
        return self.name