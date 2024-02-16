from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.contrib.auth.models import User, auth
from django.contrib import messages
import re

# Create your views here.

def index(request):
    return render(request, 'main.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')
        password2 = request.POST.get('password2', '')

        if len(password) >= 6:
            if password == password2:
                if User.objects.filter(username = username).exists():
                    messages.info(request, 'Username already exists!')
                    return redirect('signup')
                
                elif User.objects.filter(email = email).exists():
                    messages.info(request, 'Email already exists!')
                    return redirect('signup')
                
                else:
                    user = User.objects.create_user(username=username, email=email, password=password)
                    user.save()
                    return redirect('login')
            
            else:
                messages.info(request, 'Invalid password!')
                return redirect('signup')

        else:
            messages.info(request, 'There should be alteast 7 speacial characters in password')
            return redirect('signup')    

    else:
        return render(request, 'signup.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(username = username, password = password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid credentials! please try again')
            return redirect('login')
    else:
        return render(request, 'login.html')
    

def logout(request):
    auth.logout(request)
    return redirect('/')

