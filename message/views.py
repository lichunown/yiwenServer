from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from .message import tmpMessages, MessageData
from m_user.token import userToken
import json
# Create your views here.
@csrf_exempt
def send(request):
    if request.method=='POST':
        token = request.POST.get('token')
        user = userToken.getUser(token)
        if user:
            data = request.POST.get('data')
            action = request.POST.get('action')
            to = request.POST.get('toname')
            if action=='send':
                tmpMessages.addmessage(to, data)
                return HttpResponse(json.dumps({
                    'action':'sendmassage',
                    'result':'succeed',
                })) 
            elif action=='get':
                r = tmpMessages.getmeaages(user.username)
                return HttpResponse(json.dumps({
                    'action':'getmessage',
                    'result':'succeed',
                    'data':r,
                })) 
            elif action=='clean':
                tmpMessages.cleanmessages(user.username)
                return HttpResponse(json.dumps({
                    'action':'cleanmessage',
                    'result':'succeed',
                }))
            else:
                return HttpResponse(json.dumps({
                    'action':'message',
                    'result':'error',
                    'errorResult':'actionNotExist',
                }))
        else:
            return HttpResponse(json.dumps({
                'action':'message',
                'result':'error',
                'errorResult':'TokenDoNotMatch',
            })) 
    else:
        return HttpResponse('''Please use POST to visit. ''') 