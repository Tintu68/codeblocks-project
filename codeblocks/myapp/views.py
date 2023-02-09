from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from . models import *

# Create your views here.

def home(request):
    domain = Domain.objects.all()
    context = {'domain':domain}
    return render(request,"home.html",context)


def register(request):
    if request.method=="POST":
        
        first_name=request.POST['firstname']
        last_name=request.POST['lastname']
        username=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email taken")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
                user.save()
                messages.info(request,"user created")
                return redirect('/')
               
        else:
            messages.info(request,"password not matching..") 
            return redirect('register')  
            
    else:
        return render(request,'register.html')
    
    
    
def login(request):
    if request.method=="POST":
        username= request.POST['username']
        password= request.POST['password']
        
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect("/")
        else:
            messages.info(request,"invalid...")
            return redirect("register--")    
    else:
        return render(request,'login.html')