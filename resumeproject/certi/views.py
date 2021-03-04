from django.shortcuts import render

# Create your views here.

def certificates(request):
    context={'certificates':'active'}
    return render(request,"certi/certificates.html",context)
