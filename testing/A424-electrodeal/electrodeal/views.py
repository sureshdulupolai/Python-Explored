
from django.shortcuts import render,redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages


def home(request):
    return render(request,"index.html")

def register(request):
    if request.method=="GET":
        print("===========================",request.user)
        form=CustomUserCreationForm()
        context={
            "form":form
        }
        return render(request,"register.html",context)
    elif request.method=="POST":
        form=CustomUserCreationForm(request.POST)
        context={
            "form":form
        }
        if form.is_valid():
            form.save()
        return render(request,"register.html",context)

def user_login(request):
    if request.method=="GET":
       context={}
       return render(request,"login.html",context)
    elif request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect("products")

        messages.error(request,"Login Failed")     
        return render(request,"login.html")

def user_logout(request):
    logout(request)
    return redirect("login")


def about(request):
    context={}
    return render(request,"about.html",context)

def contact(request):
    context={}
    return render(request,"contact.html",context)