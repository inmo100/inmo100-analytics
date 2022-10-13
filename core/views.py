from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views.generic import View
from .forms import RegisterUserForm, LoginForm

def home(request):
    return render(request, 'core/home.html')

#class based view for login of user
class LoginUser(View):
    template_name = "core/login.html"
    form_class = LoginForm

    def get(self, request):
        form = self.form_class()
        context = {
            'form': form,
        }
        return  render(request, self.template_name, context)

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            remember_me = form.cleaned_data['remember_me']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    if remember_me:
                        request.session.set_expiry(259200)
                    messages.success(request, ("Login Successful"))
                    return redirect('home')
        messages.success(request, ("We could not authenticate you with the given credentials"))
        context = {
            'form': form,
        }
        return render(request, self.template_name, context)

# logout and redirect
def logout_user(request):
    logout(request)
    messages.success(request, ("You were logged out"))
    return redirect('home')

# process the registration form, create the new user and authenticate them
class RegisterUser(View):
    template_name = "core/register.html"
    form_class = RegisterUserForm

    def get(self, request):
        form = self.form_class()
        context = {
            'form': form,
        }
        return render(request, self.template_name, context)
    
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("Registration Successful!"))
            return redirect('home')
        else:
            context = {
            'form': form,
            }
            return render(request, self.template_name, context)