from django.http import HttpResponse
from django.shortcuts import redirect, render

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .decorators import *

# Create your views here.


def landing(request):
    return render(request, "app/landing.html")


@login_required(login_url="landing")
def index(request):
    return render(request, "app/index.html")


@unauthenticatedUser
def loginUser(request):
    if request.method == "POST":
        us = request.POST["usernamelogin"]
        pa = request.POST["password"]

        user = authenticate(request, username=us, password=pa)
        
        if user is not None:
            print("User is not none")
            login(request, user)
            return redirect("index")
        else:
            messages.warning(request, "Username or password are incorrect.")
    return render(request, "app/login.html")

def logoutUser(request):
    logout(request)
    return redirect('landing')