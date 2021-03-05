from django.shortcuts import render
from core.models import Contact
# Create your views here.
def home(request):
    context={'home':'active'}
    return render(request,"core/home.html",context)

def contact(request):
    context={'contact':'active'}
    return render(request,"core/contact.html",context)


def showcontact(request):
    cont=Contact.objects.all()
    print(cont)
    return render(request,"core/showdata.html",{"showdata":"active","contact":cont})