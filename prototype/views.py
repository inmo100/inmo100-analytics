from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterUserForm
from .models import Prototype, Project

# Create your views here.
def login_user(request):
    if request.method == "POST":
         print(request.POST)
         username = request.POST.get('username')
         password = request.POST.get('password')
         user = authenticate(request, username=username, password=password)
         if user is not None:
            login(request, user)
            return redirect('home')
         else:
            messages.success(request, ("there was an error login in"))
            return redirect('login')

    else:
        return render(request, 'authenticate/login.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, ("You were logged out"))
    return redirect('home')

def register_user(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("Registration Successful!"))
            return redirect('home')
    else:
        form = RegisterUserForm()

    return render(request, 'authenticate/register.html', {'form':form, })

def is_valid_queryparam(param):
    return param != '' and param is not None

def filter_view(request):
    qs = Prototype.objects.all().count()
    total_units_query=Prototype.objects.raw('SELECT total_units FROM prototype_prototype')
    sold_units_query=Prototype.objects.raw('SELECT sold_units FROM prototype_prototype')
    
    

    
