from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def inicio(_req):
    return render(_req, 'veterinaria/index.html')