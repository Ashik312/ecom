from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required



# Create your views here.
def home(request):
    return render(request,'home.html')
def user_signup(request):
    if request.user.is_authenticated:
        return home(request)
    else:
        if request.method=='POST':
            name=request.POST.get('username')
            email=request.POST.get('email')
            password=request.POST.get('password')
            cfpassword=request.POST.get('cfpassword')
            if password==cfpassword:
                if User.objects.filter(username=name,email=email).exists():
                    messages.info(request,"username already Exists")
                    print('Already Have')
                else:
                    new_user=User.objects.create_user(username=name,password=password,email=email)
                    new_user.set_password(password)
                    new_user.save()
                    return redirect(user_login)
            else:
                print("Wrong password")        
    return render(request,'user_signup.html')
def user_login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect(home)
        else:
            HttpResponse("Invalid")
    return render(request,'user_login.html')
def user_logout(request):
    logout(request)
    return redirect(user_login)