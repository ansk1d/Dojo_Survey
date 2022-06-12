from django import views
from django.shortcuts import redirect, render, HttpResponse

def index(request):
    return render(request, "index.html")

def result(request):
    return render(request,'result.index',context)