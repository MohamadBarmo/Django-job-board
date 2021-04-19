from django import forms
from .models import Apply ,Job


class ApplyForm(forms.ModelForm):
    class  Meta:
       model=Apply
     #  fields = ['job','name','email','website','cv','cover_letter']
       fields = ['name','email','website','cv','cover_letter']

class JobForm(forms.ModelForm):
    class Meta:
        model= Job
        fields = '__all__'
        #exclude=('slug',)
        exclude=('owner','slug')