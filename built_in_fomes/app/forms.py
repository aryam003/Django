from django import forms
from . models import *
class Normal_form(forms.Form):
    Name=forms.CharField()
    Age=forms.IntegerField()
    Email=forms.EmailField()
    Place=forms.CharField()

class Model_form(forms.ModelForm):
    class Meta:
        model=project_user
        fields='__all__'