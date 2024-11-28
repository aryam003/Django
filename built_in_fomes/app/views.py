from django.shortcuts import render,redirect
from . models import *
from . forms import *
# Create your views here.
def Normal_form_fun(req):
    if req.method=='POST':
        form1=Normal_form(req.POST)
        if form1.is_valid():
            Name=form1.cleaned_data['Name']
            Age=form1.cleaned_data['Age']
            Email=form1.cleaned_data['Email']
            Place=form1.cleaned_data['Place']
            data=project_user.objects.create(Name=Name,Age=Age,Email=Email,Place=Place)
            data.save()
            return redirect(Normal_form_fun)
    form=Normal_form()
    return render(req,'normal_form.html',{'form':form})

def Model_form_fun(req):
    if req.method=='POST':
       form1=Model_form(req.POST)
       if form1.is_valid():
           form1.save()
           return redirect(Model_form_fun)
    form=Model_form()
    return render(req,'model_form.html',{'form':form})
