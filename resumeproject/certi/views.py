from django.shortcuts import render

# Create your views here.

def certificates(request):
    return render(request,"certi/certificates.html")
