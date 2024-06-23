
from django.http import HttpResponse

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login


def signup(request):
    return render(request, 'LoginSignup/signup.html')


def login_view(request):
    error_message = None
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, username=email, password=password)
        if user is not None:

            login(request, user)  # Ensure this line has `request` and `user`
            return redirect('index')  # Replace 'home' with your desired URL name
        else:
            error_message = "Invalid email or password."
    return render(request, 'LoginSignup/login.html')