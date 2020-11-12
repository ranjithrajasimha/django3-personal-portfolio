from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate

from .models import Project

# Create your views here.
def home(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/home.html', {'projects':projects})

def loginuser(request):
    if request.method == "GET":
        return render(request, 'portfolio/loginuser.html', {'form': AuthenticationForm()})

    else:
        user = authenticate(request, username = request.POST["username"], password = request.POST["password"])
        if user is None:
            return render(request, 'portfolio/loginuser.html', {'form': AuthenticationForm()}, {'error': 'username and password did not match!'})
        else:
            login(request, user)
            return redirect('home')


def logoutuser(request):
    if request.method == "POST":
        logout(request)
        return redirect('home')