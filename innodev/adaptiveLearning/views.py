from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import EmailMessage

# Create your views here.
from adaptiveLearning.models import profile, Addition


def home(request):
    return render(request, 'home.html')


def topics(request):
    return render(request, 'topics.html')


def signup(request):
    if request.user.is_authenticated:
        return redirect("home")
    if request.method == "POST":
        userN = request.POST.get("userName", "")
        try:
            pro = profile.objects.get(username=userN)
            messages.info(request, 'User Name Already Taken')
            return redirect("home")
        except profile.DoesNotExist:
            email = request.POST.get("email", "")
            passwor = request.POST.get("password", "")
            cpasswor = request.POST.get("cpassword", "")
            if passwor == cpasswor:
                Profile = profile()
                Profile.username = userN
                Profile.email = email
                Profile.password = passwor
                Profile.save()
                messages.info(request, 'Registration Successful!')
                return redirect("home")
            else:
                messages.info(request, 'Password didn\'t Match')
                return redirect("home")
    return render(request, 'home.html')


def Login(request):
    if request.user.is_authenticated:
        return redirect("home")
    if request.method == "POST":
        uname = request.POST.get("loginuserName", "")
        paswo = request.POST.get("loginpass", "")
        try:
            pro = profile.objects.get(username=uname)
            if pro.password == paswo:
                messages.info(request, 'Log In Successful!')
                return render(request, "topics.html")
            else:
                messages.info(request, 'Invalid Credentials!')
                return redirect("home")
        except profile.DoesNotExist:
            messages.info(request, 'Sign Up first!')
            return render(request, "home.html")
    return render(request, "home.html")


def password_reset(request):
    return render(request, 'password_reset.html')


def addition(request):
    qu = Addition.objects.get()
    return render(request, 'question_page.html', {'q': qu})


def index(request):
    return render(request, 'index.html')
