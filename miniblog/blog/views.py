from django.shortcuts import render,HttpResponseRedirect
from blog.forms import SignUpForm,LoginForm,AddBlog
from django.contrib import messages
from .models import Blog
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import Group
from django.core.mail import send_mail
from django.conf import Settings
# Create your views here.

def home(request):
    data=Blog.objects.all()
    return render(request,"blog/home.html",{'data':data})

def about(request):
    return render(request,"blog/about.html")

def contact(request):
    if request.method =="POST":
        name=request.POST['name']
        email=request.POST['email']
        subject=request.POST['subject']
        message=request.POST['message']
        send_mail(
        subject,
        message,
        Settings.EMAIL_HOST_USER,
        ['to@example.com'],
        fail_silently=False,
)
        
        return HttpResponseRedirect('/home/')
    return render(request,"blog/contact.html")

def dashboard(request):
    if request.user.is_authenticated:
        reqUser=request.user
        full_name=reqUser.get_full_name()
        grps=reqUser.groups.all()
        data=Blog.objects.all()
        return render(request,"blog/dashboard.html",{'user':full_name,'data':data,'groups':grps})
    else:
        return HttpResponseRedirect('/login/')

def user_login(request):
    if not request.user.is_authenticated:
        
        if request.method=='POST':
            form=LoginForm(request=request,data=request.POST)
            if form.is_valid():
                uname=form.cleaned_data['username']
                upass=form.cleaned_data['password']
                user=authenticate(username=uname,password=upass)
            if user is not None:
                login(request,user)
                messages.success(request,'Congratulattions !! you have successfully logged in')
                return HttpResponseRedirect('/dashboard/')

        else:
            form=LoginForm()
            return render(request,"blog/login.html",{'form':form})
    else:
        return HttpResponseRedirect("/dashboard/")

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/home')

def user_signup(request):
    if request.method=='POST':
        form=SignUpForm(request.POST)
        if form.is_valid():
            user=form.save()
            messages.success(request,'Congratulattions !! you have successfully signed up')
            group=Group.objects.get(name="authors")
            user.groups.add(group)
    else: 
        form=SignUpForm()
    return render(request,"blog/signup.html",{'form':form})

def addBlog(request):
    if request.user.is_authenticated:
        if request.method=='POST':      
            blogs=AddBlog(request.POST)
            if blogs.is_valid():
                title=blogs.cleaned_data['title']
                description=blogs.cleaned_data['description']
                data=Blog(title=title,description=description)
                data.save()
                form=AddBlog()
                return render(request,'blog/addblog.html',{'form':form})
        else:
            data=AddBlog()
            return render(request,'blog/addblog.html',{'form':data})
    else:
        return HttpResponseRedirect("/login/")

def deleteBlog(request,id):
    if request.user.is_authenticated:
        data=Blog.objects.get(pk=id)
        data.delete()
        return HttpResponseRedirect('/dashboard/')
    else:
        return HttpResponseRedirect('/login/')
        

def UpdateBlog(request,id): 
    if request.user.is_authenticated:
        if request.method == 'POST':
            data=Blog.objects.get(pk=id)
            form=AddBlog(request.POST,instance=data)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/dashboard/')
        else:
            data=Blog.objects.get(pk=id)
            form=AddBlog(instance=data)
            return render(request,'blog/editblog.html',{'form':form})
    else:
        return HttpResponseRedirect('/login/')
            
    
    