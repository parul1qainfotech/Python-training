from django import forms

class AddSkills(forms.Form):
    
    skill=forms.CharField(label="Add Skills")
    percent=forms.IntegerField(label="How much do you know about this")
    # hidden=forms.CharField(widget=forms.HiddenInput())
    