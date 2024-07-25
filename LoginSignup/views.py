from allauth.socialaccount.views import SignupView
from django.http import HttpResponse

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import MemberRegistrationForm
from django.contrib import messages

def signup(request):
    if request.method == 'POST':
        form = MemberRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')

            return redirect('login')  # Redirect to the home page or any other page
    else:
        form = MemberRegistrationForm()
    return render(request, 'LoginSignup/signup.html', {'form': form})


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

class CustomSignupView(SignupView):
    template_name = 'accounts/signup.html'  # Replace with your signup template

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/')  # Redirect authenticated users away from signup
        return super().dispatch(request, *args, **kwargs)


