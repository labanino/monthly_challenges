from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def january(request):
    return HttpResponse('Learn React as soon as possible!') 

def february(request):
    return HttpResponse('Need to start going to the gym again!')