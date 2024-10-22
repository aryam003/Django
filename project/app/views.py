from django.shortcuts import render,redirect
from django.http import HttpResponse
todo=[{'id':'1','task':'task'},{'id':'2','task':'task1'}]

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

def form1(request):
    if request.method=='POST':
        id=request.POST['id']
        task=request.POST['task']
        todo.append({'id':id,'task':task})
        print(todo)
        return redirect(form1)
    
    return render(request,'form1.html',{'todo':todo})

def ediy_form(req,id):
    task=''
    for i in todo:
        if i['id']==id:
            task=i
        if req.method=='POST':
            id=req.POST['id']
            task1=req.POST['task']
            task['id']=id
            task['task']=task1
            return redirect(form1)

    return render(req,'edit_form1.html',{'data':task})

def delete_form1(req,id):
    for i in todo:
        if i['id']==id:
            todo.remove(i)
    return redirect(form1)        