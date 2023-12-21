from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login

# Create your views here.

def signupPage(request):
    if request.method == "POST":
        uname=request.POST.get("username")
        email=request.POST.get("email")
        pass1=request.POST.get("password1")
        pass2=request.POST.get("password2")
        
        if pass1!=pass2:
            return HttpResponse("Your Password and Confirm Password is not same !!")
        
        else:
            myuser = User.objects.create_user(uname,email,pass1)
            myuser.save()
            return redirect("loginPage")
           
    return render(request, "signup.html")

def loginPage(request):
    if request.method == "POST":
        username=request.POST.get("username")
        pass1=request.POST.get("password")
        my_user=authenticate(request,username=username,password=pass1)
        
        if my_user is not None:
            login(request,my_user)
            return HttpResponse("User login successfull!!!")
        
        else:
            return HttpResponse("Username or Password is not correct!!")
    
    return render(request, "login.html")

