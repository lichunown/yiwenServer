from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'send$',views.send,name='send'),
    url(r'history$',views.history,name='history'),
]
