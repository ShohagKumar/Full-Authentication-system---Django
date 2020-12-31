from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.messages import constants as messages
from django.contrib import messages

# Create your views here.


def loginuser(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            messages.error(request, 'Invalid Credentials!!!!')
            return redirect('loginuser')
    else:
        return render(request, "login.html")


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:

            if User.objects.filter(username=username).exists():
                messages.info(
                    request, 'Username already exists. Try someting new!!')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(
                    request, 'Email already exists.Try someting new!!')
                return redirect('register')
            else:

                user = User.objects.create_user(
                    username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                user.save()
                return redirect('loginuser')
        else:
            messages.info(request, 'Password is not matched!!')
            return redirect('register')

    else:
        return render(request, 'register.html')


def logoutuser(request):
    logout(request)
    return redirect("/")
