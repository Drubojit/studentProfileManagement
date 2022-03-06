# from secrets import choice
# from django import forms
# from .models import StudentProfileModel


# class AddStudentForm(forms.ModelForm):
   
#     class Meta:
    
#        model = StudentProfileModel
#        fields=("name","dateofbirth","gender","note") 
#        gender=forms.CheckboxInput
#        widgets={
           
#            'name':forms.TextInput(attrs={'class':'form-control'}),
#            'dateofbirth':forms.DateInput(attrs={'class':'form-control'}),
#            'gender':forms.TextInput(attrs={'class':'form-control'}),
#             'note':forms.Textarea(attrs={'class':'form-control'})
#        }



from secrets import choice
from django import forms
from .models import StudentProfileModel
from datetime import date


CHOICES= [
    ('male', 'Male'),
    ('female', 'Female'),
    ('others', 'Others'),
    ]

class AddStudentForm(forms.ModelForm):
   
    class Meta:
    
       model = StudentProfileModel
    #    fields = ['name','dateofbirth','gender','note']
       fields = '__all__'
       widgets={
           
           'name':forms.TextInput(attrs={'class':'form-control'}),
           'dateofbirth':forms.DateInput(attrs={'class':'form-control'}),
           'gender':forms.Select(choices=CHOICES),
           'note':forms.Textarea(attrs={'class':'form-control'})
       }
    
    def clean_name(self):
        name = self.cleaned_data['name']

        for n in name:
            if n.isdigit():
                msg = 'Enter a valid name'
                self.add_error('name', msg)
                break 

        return name

    
    def clean_dateofbirth(self):
        dateofbirth = self.cleaned_data['dateofbirth']
        today = date.today()
        if dateofbirth>=today:
            msg = 'Enter a valid birthdate'
            self.add_error('name', msg)   

        return dateofbirth



       

