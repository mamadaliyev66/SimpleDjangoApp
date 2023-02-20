from django.shortcuts import render
from django.http import HttpResponse
from . import models


def home(request):
    return render(request,'index.html',{'text':request.path})


def About(request):
    return render(request,'index.html',{'text':request.path})

def Contact(request):
    return render(request,'index.html',{'text':request.path})




