import email
import password
import username
from django.contrib import auth
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponseRedirect, request, HttpResponse
from django.contrib.auth import logout, authenticate,login as dj_login
from django.contrib.auth.models import User
from passlib.handlers.pbkdf2 import pbkdf2_sha256
from django.contrib.auth import get_user_model

from .models import Signin


def hi(request):
    return render(request,'farmapp/home.html')


def inside(request):
    return render(request,'farmapp/dashboard.html')


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        User = authenticate(username=username, password=password)
        dj_login(request, User)
        if User is not None:
            if User.is_active:
                return render(request, 'farmapp/dashboard.html')
            else:
                print("Invalid login details: {0}, {1}".format(username, password))
                return HttpResponse("Invalid login details supplied.")

        else:
                return render(request, 'farmapp/home.html', {})





def signup(request):
        User = Signin()
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            email = request.POST.get('email')
            user = Signin.objects.create(username=username, first_name=first_name, last_name=last_name,email=email)
            user.set_password(raw_password = password)
            user.save()
            return render(request, 'farmapp/home.html')



def search(request):

    Users = Signin.objects.all()
    return render(request,"farmapp/search.html",{'User': Users})


def update(request):

    User = get_user_model()
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        user = User.objects.create(username=username, password=password, first_name=first_name, last_name=last_name,email=email)
        user.save()
        return render(request,"farmapp/update.html",{'User': User})

def delete(request):
    user = Signin.objects.get(id=request.user.id)
    if request.method == 'POST':
        user.delete()
        context = {'user': user}
        return render(request,'farmapp/delete.html',context)


def logout(request):
    if request.method == 'post':
      logout(request)
    return HttpResponseRedirect(reverse("hi"))
