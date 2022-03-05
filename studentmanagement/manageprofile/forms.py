from secrets import choice
from django import forms
from .models import StudentProfileModel


class AddStudentForm(forms.ModelForm):
   
    class Meta:
    
       model = StudentProfileModel
       fields=("name","dateofbirth","gender","note") 
       gender=forms.CheckboxInput
       widgets={
           
           'name':forms.TextInput(attrs={'class':'form-control'}),
           'dateofbirth':forms.DateInput(attrs={'class':'form-control'}),
           'gender':forms.TextInput(attrs={'class':'form-control'}),
            'note':forms.Textarea(attrs={'class':'form-control'})
       }
