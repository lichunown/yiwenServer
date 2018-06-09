from django.shortcuts import render
from .models import Data
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import json
# Create your views here.
@csrf_exempt
def getData(request):
    if request.method=='POST':
        name = request.POST.get('name')
        if len(Data.objects.filter(name=name)):
            data = Data.objects.get(name=name)
            return HttpResponse(json.dumps({
                    'action':'getData',
                    'result':'succeed',
                    'name':name,
                    'data':data.data,
            })) 
        else:
            return HttpResponse(json.dumps({
                    'action':'getData',
                    'result':'error',
                    'name':name,
                    'errorResult':'NameNotExist',
            })) 