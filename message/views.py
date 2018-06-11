from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from .message import tmpMessages, MessageData, historydata
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
                tmpMessages.addmessage(to, user.username, data)
                return HttpResponse(json.dumps({
                    'action':'sendmassage',
                    'result':'succeed',
                })) 
            elif action=='get':
                getfrom = request.POST.get('froms')
                r = tmpMessages.getmeaages(user.username, getfrom)
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
            elif action=='list':
                r = tmpMessages.listsender(user.username)
                return HttpResponse(json.dumps({
                    'action':'cleanmessage',
                    'result':'succeed',
                    'data':r,
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

@csrf_exempt
def history(request):
    if request.method=='POST':
        username = request.POST.get('username')
        data = request.POST.get('data')
        action = request.POST.get('action')
        if not username:
            return HttpResponse(json.dumps({
                'action':'history',
                'result':'error',
                'errorResult':'usernameDoNotExist',
            })) 

    if action == "send":
        historydata.adddata(username, data)
        return HttpResponse(json.dumps({
            'action':'addhistory',
            'result':'succeed',
        })) 
    elif action == "get":
        r = historydata.getdata(username)
        return HttpResponse(json.dumps({
            'action':'gethistory',
            'result':'succeed',
            'data':r
        })) 
    else:
        return HttpResponse(json.dumps({
            'action':'history',
            'result':'error',
            'errorResult':'actionNotExist',
        }))