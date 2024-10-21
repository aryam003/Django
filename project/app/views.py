from django.shortcuts import render,redirect
from django.http import HttpResponse
todo=[]
# Create your views here.
def fun1(request):
    return HttpResponse("welcome")

def fun2(request):
    return HttpResponse("hello")

def fun3(req,a,b):
    return HttpResponse(a)

def fun4(req,a):
    print(type(a))
    return HttpResponse(a)

def fun5(req,a,b,c):
    if a>b and a>c:
        return HttpResponse(a)
    elif b>a and b>c:
        return HttpResponse(b)
    else:
        return HttpResponse(c)

def index_page(req):
    name="Anu"
    age=20
    place="kannur"
    return render(req,'index.html',{'name':name,'age':age,'place':place})

def demo(req):
    # l=[1,2,3,4,5]            #list
    # l={'name':'anu','age':20}  
    l=[{'name':'anu','age':20},{'name':'A','age':21},{'name':'B','age':20}]
    d={'name':'anu','age':20}
    return render(req,"demo.html",{"data":l,'data1':d})

def snd(req):
    return render(req,'second.html')

def form(request):
    if request.method=='POST':
        id=request.POST['id']
        task=request.POST['task']
        todo.append({'id':id,'task':task})
        print(todo)
        return redirect(form)
    
    return render(request,'todo.html',{'todo':todo})

