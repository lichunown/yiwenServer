from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from passage.models import Passage
from m_user.token import userToken
import json
# Create your views here.
@csrf_exempt
def getpassagelist(request):
    if request.method=='POST':
        passagelist = Passage.objects.all()
        resultlist = []
        for item in passagelist:
            resultlist.append({
                    'title':item.title,
                    'time':str(item.time),
                    'id':item.id,
                })
        return HttpResponse(json.dumps({
            'action':'getpassagelist',
            'result':'succeed',
            'lists':resultlist,
        }))  

@csrf_exempt
def getpassage(request):
    if request.method=='POST':
        passageid = request.POST.get('id')
        passage = Passage.objects.filter(id=passageid)
        if passage:
            passage = passage[0]
            return HttpResponse(json.dumps({
                'action':'getpassage',
                'result':'succeed',
                'passage':{
                    'id':passage.id,
                    'title':passage.title,
                    'body':passage.body,
                    'time':str(passage.time),
                },
            }))  
        else:
            return HttpResponse(json.dumps({
                'action':'getpassage',
                'result':'error',
                'errorResult':'PassageNotFound',
            }))      


@csrf_exempt
def savepassage(request):
    if request.method=='POST':
        token = request.POST.get('token')
        user = userToken.getUser(token)
        if user:
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
                'action':'savepassage',
                'result':'error',
                'errorResult':'TokenDoNotMatch',
            })) 
    else:
        return HttpResponse('''Please use POST to visit. ''') 



@csrf_exempt
def changepassage(request):
    if request.method=='POST':
        token = request.POST.get('token')
        user = userToken.getUser(token)
        if user:
            passageid = request.POST.get('id')
            passage = Passage.objects.filter(id=passageid)
            if passage:# passage exists
                passage = passage[0]
                if passage.m_user == user:
                    passage.title = request.POST.get('title')
                    passage.body = request.POST.get('body')
                    passage.save()
                    return HttpResponse(json.dumps({
                        'action':'changepassage',
                        'result':'succeed',
                        'id':passageid,
                    }))                     
                else:# passage is not this user post
                    return HttpResponse(json.dumps({
                        'action':'changepassage',
                        'result':'error',
                        'errorResult':'PermissionDenied',
                        'id':passageid,
                    }))  
            else:# passage doesn't exists
                return HttpResponse(json.dumps({
                    'action':'changepassage',
                    'result':'error',
                    'errorResult':'PassageDoNotExists',
                    'id':passageid,
                }))  
        else:# user don't login
            return HttpResponse(json.dumps({
                'action':'savepassage',
                'result':'error',
                'errorResult':'TokenDoNotMatch',
            })) 
    else:
        return HttpResponse('''Please use POST to visit. ''') 