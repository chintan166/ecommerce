from django.shortcuts import render,redirect
from .forms import RegistrationForm
from .models import Accounts
from django.contrib import messages,auth
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            first_name=form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            phone_number = form.cleaned_data['phone_number']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            
            username = email.split("@")[0]
            user = Accounts.objects.create_user(first_name = first_name,last_name=last_name,email=email,username=username,password=password)
            user.phone_number = phone_number
            user.save()
            messages.success(request,'Registration success')
            return redirect('register')
    else:
        form = RegistrationForm()
    context = {
        'form':form,
    }
    return render(request,'accounts/register.html',context)

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
         
        user = authenticate(request,username=username,password=password)
        
        if user is not None:
            auth.login(request,user)
            messages.success(request, "you are now logged in")
            return redirect('dashboard')
        else:
            messages.error(request, "invalid login credential")
            return redirect('login')
    return render(request,'accounts/login.html')

@login_required(login_url = 'login')
def logout(request):
    auth.logout(request)
    messages.success(request,"you are loged out")
    return redirect('login')

@login_required(login_url = 'login')
def dashboard(request):
    return render(request,'accounts/dashboard.html')