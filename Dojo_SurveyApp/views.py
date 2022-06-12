from django import views
from django.shortcuts import redirect, render, HttpResponse

def index(request):
    return render(request, "index.html")

def result(request):
    context = {'name':request.POST["name"],
    'location':request.POST['loction'],
    'favlang':request.POST['Language'],
    'comment':request.POST['comment']
    }
    return render(request,'result.html',context)

