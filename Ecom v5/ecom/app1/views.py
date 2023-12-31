from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.
def home(request):
    return render(request,'home.html')
def login1(request):
    if(request.method=="POST"):
        name = request.POST['name']
        password = request.POST['password']
        user = authenticate(username=name,password=password)
        if user:
            login(request,user)
            return home(request)
        else:
            return HttpResponse("User Not Found!!")
    return render(request,'login.html')
def logout1(request):
    logout(request)
    return login1(request)
def signup1(request):
    if request.user.is_authenticated:
        return home(request)
    else:
        if request.method == 'POST':
            name=request.POST.get('name')
            email=request.POST.get('email')
            password=request.POST.get('password')
            cpassword=request.POST.get('cpassword')
            if password==cpassword:
                if User.objects.filter(username=name,email=email).exists():
                    messages.info(request,'usename already exists')
                    print('Already have')
                else:
                    new = User.objects.create_user(username=name,password=password,email=email)
                    new.set_password(password)
                    new.save()
                    return redirect(login1)
            else:
                print("Wrong password")
    return render(request,'signup.html')
