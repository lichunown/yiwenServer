from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'getpassage$',views.getpassage,name='getpassage'),
    url(r'getpassagelist$',views.getpassagelist,name='getpassagelist'),
    url(r'savepassage$',views.savepassage,name='savepassage'),
    url(r'changepassage$',views.changepassage,name='changepassage'),
]
