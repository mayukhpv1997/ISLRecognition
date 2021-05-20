from django.shortcuts import render
from .models import *
from .signup import *
from .models import Signup
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth import get_user_model



# Create your views here.

def sample(request):
    return render(request, "sample.html")

def camera(request):
    return render(request, "camera.html")
def index(request):
    return render(request, "index.html")
def signin(request):
    return render(request, "signin.html")
def inner(request):
    return render(request, "inner-page.html")
def findhand(request):
       return request(request, "findhand.py")

def signup(request):
    if request.method == 'POST':
        var = Reg(request.POST)
        if var.is_valid():
            firstname = var.cleaned_data['firstname']
            email = var.cleaned_data['email']
            password = var.cleaned_data['password']
            confirmpassword = var.cleaned_data['confirmpassword']
            g = Signup(firstname=firstname, email=email, password=password, confirmpassword=confirmpassword)
            g.save()
            return render(request, 'signup.html', {'msg': 'successfully registered'})

        else:
            return render(request, 'signup.html', {'msg': 'technical error'})
    else:
        return render(request, 'signup.html', )


def log(request):

    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        #sign = Signup
        if Signup.objects.filter(email=email , password=password).exists():
            #return render(request,'signin.html', {'msg' : 'successfull'})
            return render(request, 'index.html', {'msg': 'logined successfully '})
        else:
            return render(request, 'signin.html', {'msg' : 'invalid credential'})
    else:
        return render(request, 'signin.html', )

def feedback(request):
    if request.method == 'POST' :
        var = Feedback(request.POST)
        if var.is_valid():
            name = var.cleaned_data['name']
            email = var.cleaned_data['email']
            subject = var.cleaned_data['subject']
            message = var.cleand_data['message']
            g = Feedback(name= name ,email=email,subject=subject,message=message)
            g.save()
            return render(request,'index.html',{'msg':'succesfull'})
        else:
            return render(request,'index.html',{'msg':' submission failed'})
    else:
        return render(request, 'index.html', {'msg': ' submission failed'})







