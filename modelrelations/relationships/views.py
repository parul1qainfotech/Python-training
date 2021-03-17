from django.shortcuts import render

# Create your views here.
def one_to_one(request):
    return render(request,'relationships/one_to_one.html')

def one_to_many(request):
    return render(request,'relationships/one_to_many.html')

def many_to_one(request):
    return render(request,'relationships/many_to_one.html')

def many_to_many(request):
    return render(request,'relationships/many_to_many.html')