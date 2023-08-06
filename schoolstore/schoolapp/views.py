from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render,redirect

# Create your views here.

def home(request):
    return render(request,'home.html')

def commerce(request):

    return render(request,'commerce.html')
def science(request):

    return render(request,'science.html')
def architecture(request):

    return render(request,'architecture.html')
def fashion_design(request):

    return render(request,'fashion_design.html')
def inf_technology(request):

    return render(request,'inf_technology.html')


def login (request):
    if request.method=='POST':
        username=request.POST['username']
        pswd=request.POST['password']
        user = User.objects.create_user(username=username, password=pswd)
        user.save();


    return render(request,'login.html')

def register (request):
    if request.method=='POST':
        usrname=request.POST['usrname']
        password=request.POST['password']
        cnfpswd=request.POST['cnfpswd']

        user = User.objects.create_user(username=usrname, password=password,cnfpswd=cnfpswd)
        user.save();



    return render(request,'register.html')

def requirements (request):

    return render(request, 'form_requirements.html')

def logout(request):
    return redirect('/')

def ordconfirm(request):
    return render(request,'ordconfirm.html')


