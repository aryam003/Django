from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import *
mod=[]
# Create your views here.
def fun1(request):
    return HttpResponse("welcome")

def disp_std(req):
    data=Student.objects.all()
    return render(req,'display_std.html',{'data':data})

def mdl(request):
    if request.method=='POST':
        roll_no=request.POST['roll_no']
        name=request.POST['name']
        email=request.POST['email']
        ph_no=request.POST['ph_no']
        mod.append({'roll_no':roll_no,'name':name,'email':email,'ph_no':ph_no})
        print(mod)
        return redirect(mdl)
    
    return render(request,'add_std.html',{'todo':mod})