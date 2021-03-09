from django.core import validators
from django import forms
from enroll.models import User


class StudentRegistration(forms.ModelForm):
    class Meta:
        model=User
        fields=['name','email','password']
        widgets={
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.TextInput(attrs={'class':'form-control'}),
            'password': forms.PasswordInput(render_value=True,attrs={'class':'form-control'}),
        }
        
    def clean(self):
        cleaned_data=super().clean()
        valname=self.cleaned_data['name']
        valemail=self.cleaned_data['email']
        valpass=self.cleaned_data['password']
        
        if(valname or valemail or valpass)== "":
            raise forms.ValidationError("Input field is required please fill this field")
        
        elif(len(valname))<2:
            raise forms.ValidationError("Name must be greater than 2")
        
        elif(len(valname))>10:
            raise forms.ValidationError("Name must not be greater than 10")
        