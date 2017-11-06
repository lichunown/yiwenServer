#encoding:utf-8
from django.shortcuts import render
from django.utils import timezone
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
# Create your views here.
from m_user.token import userToken
import json
import hashlib,random  
from .models import m_User

class Encode(object):
    def __init__(self):
        pass
        #self.md5 = hashlib.md5()
    def encode(self,string):
        #self.md5.update(str)
        return string
        
encodePwd = Encode()

@csrf_exempt
def login(request):
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if len(m_User.objects.filter(username=username)):
            user = m_User.objects.get(username=username)
            pwd = encodePwd.encode(str(password))
            if str(user.pwd) == pwd:
                token = userToken.createToken(user)
                return HttpResponse(json.dumps({
                        'action':'signin',
                        'result':'succeed',
                        'token':token,
                    })) 
            else:
                return HttpResponse(json.dumps({
                        'action':'signin',
                        'result':'error',
                        'errorResult':'passwordError',
                    }))                
        else:
            return HttpResponse(json.dumps({
                    'action':'signin',
                    'result':'error',
                    'errorResult':'usernameNotExist',
                }))            



@csrf_exempt
def logout(request):
    if request.method=='POST':
        token = request.POST.get('token')
        r = userToken.dropToken(token)
        if r == None:
            return HttpResponse(json.dumps({
                    'action':'logout',
                    'result':'error',
                    'errorResult':'keyError',
                }))  
        else:
            return HttpResponse(json.dumps({
                    'action':'logout',
                    'result':'succeed',
                    'username':r.username,
                }))                  

@csrf_exempt
def signup(request):
    if request.method=='POST':
        username = request.POST.get('username')
        if not len(m_User.objects.filter(username=username)):
            password = request.POST.get('password')
            pwd = encodePwd.encode(str(password))
            user = m_User()
            user.username = username
            user.pwd = pwd
            user.save()
            return HttpResponse(json.dumps({
                    'action':'signup',
                    'result':'succeed',
                    'username':'usernameExist',
                }))
        else: # username have exist
            return HttpResponse(json.dumps({
                    'action':'signup',
                    'result':'error',
                    'errorResult':'usernameExist',
                }))
    else:
        return HttpResponse(json.dumps({
            'action':'signup',
            'result':'error',
            'errorResult':'requestGET',
        }))

@csrf_exempt
def modify(request):
    if request.method=='POST':
        if request.POST.get('token'):
            user = userToken.getUser(request.POST.get('token'))
            if not user:
                return HttpResponse(json.dumps({
                    'action':'modify',
                    'result':'error',
                    'errorResult':'userDoNotExist',
                }))                
            modifyData = request.POST.get('modifydata')
            try:
                if modifyData:
                    modifyData = json.loads(modifyData)
                else:
                    return HttpResponse(json.dumps({
                        'action':'modify',
                        'result':'error',
                        'errorResult':'modifyDataDoNotExists',
                    }))                     
            except Exception as e:
                return HttpResponse(json.dumps({
                    'action':'modify',
                    'result':'error',
                    'errorResult':e,
                }))                
            if modifyData.get('nickname'):
                user.nickname = modifyData.get('nickname')
            if modifyData.get('truename'):
                user.truename = modifyData.get('truename')
            if modifyData.get('tel'):
                user.tel = modifyData.get('tel')
            if modifyData.get('email'):
                user.email = modifyData.get('email')
            if modifyData.get('address'):
                user.address = modifyData.get('address')
            if modifyData.get('page'):
                user.page = modifyData.get('page')  
            if modifyData.get('information'):
                user.information = modifyData.get('information')                                                           
            user.save()
            return HttpResponse(json.dumps({
                'action':'modify',
                'result':'succeed',
            }))
        else:
            return HttpResponse(json.dumps({
                'action':'modify',
                'result':'error',
                'errorResult':'tokenDoNotExist',
            }))



@csrf_exempt
def getdata(request):
    if request.method=='POST':
        getdatausername = request.POST.get('getdatausername')
        token = request.POST.get('token')
        user = userToken.getUser(token)
        if user:
            if user.username == getdatausername:
                return HttpResponse(json.dumps({
                    'action':'getuserdata',
                    'result':'succeed',
                    'data':{
                        'college':user.college,
                        'studentid':user.studentid,
                        'truename':user.truename,
                        'iscar':user.iscar,
                    },
                }))
        # not user himself
        user = m_User.objects.filter(username = getdatausername)
        if user:
            user = user[0]           
            return HttpResponse(json.dumps({
                'action':'getuserdata',
                'result':'succeed',
                'data':{
                    'college':user.college,
                    'truename':user.truename,
                    'iscar':user.iscar,
                },
            }))
        else:
            return HttpResponse(json.dumps({
                'action':'getuserdata',
                'result':'error',
                'errorResult':'usernameDoNotExist',
            }))





# 
# def index(request):
#     projects=Project.objects.order_by('startdate').reverse()[:10]    
#     tutors=Tutor.objects.order_by('?').reverse()[:10] 
#     context={
#         'projects':projects,
#         'tutors':tutors,
#     }
#     a={
#         'edde':'dfbgd',
#         'vdv':['dfhr','gedgfs'],
#     }
#     json.dump(a)
#     return render(request,'main/index.html',context)

# def signin(request,before='index'):
#     if request.method=='POST':
#         sf = SigninForm(request.POST)
#         if sf.is_valid():
#             username = sf.cleaned_data['username']
#             password = sf.cleaned_data['password']
#             user = authenticate(username=username, password=password)
#             if user is not None and user.is_active:
#                 login(request, user)
#                 return render(request,'main/signin.html',{'result':'succeed','before':before})
#         #form doesn't true
#             else:
#                 return render(request, 'main/signin.html', {'result':'error','form':sf})        
#         else:
#             return render(request,'main/signin.html',{'result':'error'})
#             # Return an error message.
#     else:
#         print 'signin2'
#         sf = SigninForm()
#         return render(request,'main/signin.html',{'form':sf,'before':before})

# def signout(request,before='index'):
#     logout(request)
#     return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
# def signup2(request):
#     if request.method=='POST':
#         suf = SigninForm(request.POST)
#         print request.POST               
#         username = request.POST['username']
#         password = request.POST['password'] 
#         if not len(User.objects.filter(username=username)):
#             if request.POST['password']==request.POST['passwordagain']:
#                 user=User()
#                 user.username=username
#                 user.set_password(password)
#                 user.save()
#                 student=Student()
#                 student.username=user
#                 student.sid=request.POST['sid']
#                 student.truename=request.POST['truename']
#                 student.birthday=timezone.now()
#                 student.save()
#                 user = authenticate(username=username, password=password)
#                 if user is not None and user.is_active:
#                     login(request, user)
#                     return render(request,'main/signin.html',{'result':'succeed'}) 
#                 else:
#                     pass #something wrong
#             else:
#                  return render(request,'main/signup2.html',{'form':suf,'error':'passwordagain'})    
#         else:
#             return render(request,'main/signup2.html',{'form':suf,'error':'usernamerepeat'})                 
#     else:
#         suf=SignupForm()
#         return render(request,'main/signup2.html',{'form':suf})

# def signup(request):
#     if request.method=='POST':
#         suf=SignupForm()
#         if suf.is_valid():
#             pass
#         else:
#             return render(request,'main/signup.html',{'error':'1','form':suf})
#     else:
#         suf=SignupForm()
#         return render(request,'main/signup.html',{'form':suf})

# def modifyaccount(request):
#     if request.user.is_authenticated():
#         if request.method=='POST':
#             f=ModifyAccountForm(request.POST,instance=Student.objects.get(username=request.user))           
#             if f.is_valid():
#                 f.save()
#                 return render(request,'main/modifyaccount.html',{'success':'1','form':f})
#             else:
#                 return render(request,'main/modifyaccount.html',{'error':'1','form':f})
#         else:
#             student=Student.objects.get(username=request.user)
#             projects=student.project_set.all()
#             f=ModifyAccountForm(instance=Student.objects.get(username=request.user))
#             return render(request,'main/modifyaccount.html',{'projects':projects,'form':f})
#     else:
#         return render(request,'main/signup2.html',{'form':suf})

# def showtutors(request,page):
#     pass
# def showtutor(request,id):
#     try:
#         student=Tutor.objects.get(id=id)  
#     except:
#         return render(request,'main/tutor.html',{'error':'none'})
#     f=ShowTutorForm(instance=student)
#     return render(request,'main/tutor.html',{'form':f})

# def showprojects(request,page):
#     page=int(page)
#     projects=Project.objects.order_by('startdate').reverse()[1*page-1:30*page-1]
#     return render(request,'main/projects.html',{'page':page,'projects':projects})
# def showproject(request,id):
#     p=Project.objects.get(id=id)
#     students=p.students.all()
#     tutors=p.tutors.all()
#     allstudents=p.students.all()
#     for s in allstudents:#应该可以优化一下
#         if request.user==s.username:
#             return render(request,'main/project.html',{'project':p,'students':students,'tutors':tutors,'edit':'1'})
#     return render(request,'main/project.html',{'project':p,'students':students,'tutors':tutors})

# def createproject(request):
#     if request.user.is_authenticated():        
#         if request.method=='POST':
#             f=CreateProjectForm(request.POST)
#             if f.is_valid():
#                 stu=Student.objects.get(username=request.user)  
#                 project=Project()
#                 project.name=f.cleaned_data['name']                
#                 allprojects=stu.project_set.all()  
#                 for p in allprojects:
#                     if p.name==project.name:
#                         return render(request,'main/createproject.html',{'error':'repeat','form':f})
#                 project.status=f.cleaned_data['status']
#                 project.introduction=f.cleaned_data['introduction']
#                 project.startdate=timezone.now()                     
#                 project.save()  
#                 project.students.add(stu)    
#                 project.save()  
#                 return showproject(request,project.id)      #why this doesn't work!!!!

#             else:
#                 return render(request,'main/createproject.html',{'error':'1','form':f})
#         else:
#             f=CreateProjectForm()
#             return render(request,'main/createproject.html',{'form':f})
#     else:
#         return signin(request)


# def showstudent(request,id):
#     try:
#         student=Student.objects.get(id=id)  
#     except:
#         return render(request,'main/student.html',{'error':'none'})
#     f=ShowStudentForm(instance=student)
#     return render(request,'main/student.html',{'form':f})


# def invitetutor(request):
#     pass
# def invitestudent(request):
#     pass