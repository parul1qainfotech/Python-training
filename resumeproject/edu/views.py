from django.shortcuts import render
from .forms import AddSkills
from .models import Skill

# Create your views here.
def skills(request):
    context={'skills':'active'}
    return render(request,"edu/skills.html",context)

def addskills(request):
    addskill=AddSkills(auto_id=True,label_suffix=" =>",initial={'skill':'Add your skill here'})
    return render(request,"edu/addskills.html",{"addskills":addskill})

def addSkillToDB(request):
    #error in this code (need to fix)
    if request.method =='POST':
        fm=AddSkills(request.POST)
        if fm.is_valid():
            s=fm.cleaned_data['skill']
            p=fm.cleaned_data['percent']
            res=Skill(skill=s,percent=p)
            res.save()
        
        else:
            fm=AddSkills()
            return render(request,"edu/addskills.html",{"data":fm})