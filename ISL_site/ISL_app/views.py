from django.shortcuts import render
from .models import *


# Create your views here.
def camera(request):
    return render(request, "camera.html")
def index(request):
    return render(request, "index.html")
def inner(request):
    return render(request, "inner-page.html")

