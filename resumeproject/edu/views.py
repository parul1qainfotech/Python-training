from django.shortcuts import render
from .forms import AddSkills
# Create your views here.
def skills(request):
    context={'skills':'active'}
    return render(request,"edu/skills.html",context)

def addskills(request):
    addskill=AddSkills(auto_id=True,label_suffix=" =>",initial={'skill':'Add your skill here'})
    return render(request,"edu/addskills.html",{"addskills":addskill})