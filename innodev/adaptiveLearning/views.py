from django.shortcuts import render,redirect
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.
from adaptiveLearning.models import profile

def home(request):
    return render(request,'home.html')


def signup(request):
    if request.user.is_authenticated:
        return redirect("home")
    if request.method == "POST":
        userN = request.POST.get("userName", "")
        email = request.POST.get("email", "")
        passwor = request.POST.get("password", "")
        cpasswor = request.POST.get("cpassword", "")

        if passwor == cpasswor:
            p, created = User.objects.get_or_create(username=userN, email=email)
            p.set_password(passwor)
            p.save()
            
            messages.info(request,'Registration Successful!')
            return redirect("home")

        else:
            messages.info(request, 'Password didn\'t Match')   
            return redirect("home")

    return render(request, 'home.html')





def Login(request):
    if request.user.is_authenticated:
        return redirect("home")
    if request.method == "POST":
        uname = request.POST.get("loginUsername", "")
        paswo = request.POST.get("loginpass", "")
        user = authenticate(username = uname, password = paswo)
        print('output')
        print(user)
        if user is not None:
            login(request, user)
            messages.info(request, 'Log In Successful!')
            return redirect("home")
        else:
            messages.info(request, 'Invalid Credentials!')
 
            return redirect("home")
 
 
    return render(request, "home.html")







