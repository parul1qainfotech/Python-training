from django import forms

class AddSkills(forms.Form):
    
    skill=forms.CharField(label="Add Skills",min_length=2,max_length=20)
    percent=forms.IntegerField(label="How much do you know about this")
    # hidden=forms.CharField(widget=forms.HiddenInput())
    