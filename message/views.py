from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from .message import tmpMessages, MessageData


# Create your views here.
@csrf_exempt
def send(request):
    if request.method=='POST':
        token = request.POST.get('token')
        user = userToken.getUser(token)
        if user:
            data = request.POST.get('data')
            to = request.POST.get('toname')
            
            tmpMessages.addmessage()
            newPassage = Passage()
            newPassage.m_user = user
            newPassage.title = request.POST.get('title')
            newPassage.body = request.POST.get('body')
            newPassage.save()
            return HttpResponse(json.dumps({
                'action':'savepassage',
                'result':'succeed',
                'id':newPassage.id,
            }))       
        else:
            return HttpResponse(json.dumps({
                'action':'send',
                'result':'error',
                'errorResult':'TokenDoNotMatch',
            })) 
    else:
        return HttpResponse('''Please use POST to visit. ''') 