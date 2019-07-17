from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User


def register(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username already taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email already taken")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, first_name= first_name, last_name=last_name, password=password1)
                user.save()
                messages.info(request,"User Created successfully!!")
        else:
            messages.info(request,"Password not matching!!")
            return redirect('register')
        return redirect('/')
    
    else:
        return render(request, 'register.html')


def login(request):
    
    username1 = request.POST['username']
    passwordtest = request.POST['password']

    if User.objects.filter(username=username1).exists() and  User.objects.filter(password=passwordtest).exists():
        return redirect('/')
    else:
        messages.info("username/ password incorrect")
        return redirect('login')