from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import *

# Create your views here.
def fun1(request):
    return HttpResponse("welcome")

def disp_std(req):
    data=Student.objects.all()
    return render(req,'display_std.html',{'data':data})

def add_std(request):
    if request.method=='POST':
        roll=request.POST['roll_no']
        std_name=request.POST['name']
        std_email=request.POST['email']
        phno=request.POST['ph_no']
        data=Student.objects.create(roll_no=roll,name=std_name,email=std_email,ph_no=phno)
        # print(mod)
        data.save()
        return redirect(disp_std)
    else:
        return redirect(disp_std)
    
def edit_std(request,id):
    data=Student.objects.get(pk=id)
    if request.method=='POST':
        roll=request.POST['roll_no']
        std_name=request.POST['name']
        std_email=request.POST['email']
        phno=request.POST['ph_no']
        Student.objects.filter(pk=id).update(roll_no=roll,name=std_name,email=std_email,ph_no=phno)
        return redirect(disp_std)
    else:
        return render(request,'edit_std.html',{'data':data})

