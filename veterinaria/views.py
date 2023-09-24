from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def inicio(_req):
    return HttpResponse('<h1>Testing</h1>')