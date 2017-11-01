from django.db import models
from m_user.models import m_User
from django.utils import timezone
# from django.utils.encoding import smart_unicode

# Create your models here.

class Passage(models.Model):
    m_user = models.ForeignKey(m_User)
    title = models.CharField(max_length=100)
    body = models.TextField()
    time = models.DateTimeField(default=timezone.now)
    # def __unicode__(self):
    #     return smart_unicode(self.title)    

