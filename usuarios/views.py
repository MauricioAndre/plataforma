from .forms import CustomUserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.shortcuts import render, redirect
from .models import CustomUser
from django.http.response import HttpResponse

def cadastro (request):
    if request.method == "POST":
          user_form = CustomUserCreationForm(request.POST)
          if user_form.is_valid():
               user_form.save()
               return redirect('login')
    else:
        user_form = CustomUserCreationForm()
    return render(request, 'cadastro.html', {'user_form': user_form} )


def login (request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            #redirect('lojaslebes')
            return HttpResponse("Você está Logado") 
        else:
            login_form = AuthenticationForm()      
    else:
        login_form = AuthenticationForm()
    return render(request, 'login.html', {'login_form': login_form} ) 

def logout(request):
    auth_logout(request)
    #redirect('lojaslebes')
    return HttpResponse("Você saiu") 