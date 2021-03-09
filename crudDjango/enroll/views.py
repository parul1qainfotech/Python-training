from django.shortcuts import render,HttpResponseRedirect
from enroll.forms import StudentRegistration
from .models import User

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
        