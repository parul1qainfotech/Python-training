from django.shortcuts import render,HttpResponseRedirect
from enroll.forms import StudentRegistration
from .models import User
from datetime import datetime,timedelta

def add_show(request):
    if request.method =='POST':
        fm=StudentRegistration(request.POST)
        if fm.is_valid():
            fm.save()
            fm=StudentRegistration()
            
    else:
        fm=StudentRegistration()
    stu=User.objects.all()
    return render(request,"enroll/add.html",{'form': fm ,'student':stu })


def deletedata(request,id):
    if request.method == 'POST':
        data=User.objects.get(pk=id)
        data.delete()
        return HttpResponseRedirect('/')

def updatedata(request,id):
    if request.method =='POST':
        data=User.objects.get(pk=id)
        fm=StudentRegistration(request.POST,instance=data)
        if(fm.is_valid()):
            fm.save()
    else:
        data=User.objects.get(pk=id)
        fm=StudentRegistration(instance=data)
    return render(request,'enroll/update.html',{'newdata':fm})

def setcookies(request):
    response=render(request,"enroll/cookies.html")
    user=request.user
    response.set_cookie('name',user,expires=datetime.utcnow()+timedelta(days=2))
    return response

def getcookies(request):
    name=request.COOKIES.get('name','Guest')
    return render(request,"enroll/cookies.html",{'get':name})


def deletecookies(request):
    response=render(request,"enroll/cookies.html")
    names=request.COOKIES('name')
    response.delete_cookie(name=names)
    return response
    
    #sessions
def setsession(request):
    request.session['name']="parul"
    return render(request,'enroll/sessions.html')

def getsession(request):
    # get=request.session['name']
    get=request.session.get('name',"guest")
    return render(request,'enroll/sessions.html',{'get':get})

def delsession(request):
    request.session.flush()
    # if 'name' in request.session:
    #     del request.session['name']
    return render(request,'enroll/sessions.html')
        
        
        