from django.shortcuts import render
from .forms import AddSkills
# Create your views here.
def skills(request):
    context={'skills':'active'}
    return render(request,"edu/skills.html",context)

def addskills(request):
    addskill=AddSkills()
    return render(request,"edu/addskills.html",{"skills":addskill})