from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from . models import *
# Create your views here.
def index(req):
    data=Movie.objects.all()
    return render(req,'bookmyshow.html',{'data':data})

def view_movie(req,id):
    data=Movie.objects.get(pk=id)
    return render(req,'ARM.html',{'data':data})