from django.shortcuts import render,redirect
from .models import UserCredentials
from django.contrib import messages
import os
# Create your views here.

def index(request):
    return render(request,'index.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['your-email']
        password = request.POST['password']
        created = UserCredentials.objects.filter(email=username, password=password)
        if created:
            return render(request,'createfolder.html')
        else:
            messages.error(request,'Enter Valid Credentials')
            return redirect('login')
                
    return render(request,'login.html')   

def register(request):
    if request.method == 'POST':
        username = request.POST['full-name']
        email = request.POST['your-email']
        password = request.POST['password']
        confirmPassword = request.POST['comfirm-password']
        if password!=confirmPassword:
            messages.error(request,'Passwords Mismatch')
            return redirect('register')
        userDataObj = UserCredentials.objects.create(username=username,email=email,password=password)
        return render(request,'login.html')
    return render(request,'register.html')

def detectPhising(request):
    if request.method== 'POST':
        url = request.POST['url']
        os.system('py DetectPhishing.py '+ url)
    return render(request,'index.html')
