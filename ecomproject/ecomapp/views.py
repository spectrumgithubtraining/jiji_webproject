from django.shortcuts import render
from django.contrib.auth.models import User
def index(request):
    # Your logic for the index view goes here
    return render(request, 'index.html')
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from .forms import LoginForm, ForgotPasswordForm, SignupForm

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                # Redirect to a success page
                return redirect('products')  # Change 'success_page' to your success page URL
            else:
                # Invalid login credentials, handle accordingly
                pass
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def forgot_password_view(request):
    if request.method == 'POST':
        form = ForgotPasswordForm(request.POST)
        if form.is_valid():
            # Process the form data, send email, etc.
            pass
    else:
        form = ForgotPasswordForm()
    return render(request, 'forgotpassword.html', {'form': form})

def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            User.objects.create_user(username=username, email=email, password=password)
            # Redirect to the login page after successful signup
            return redirect('login')  # Change 'login' to your login page URL
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})


def product_view(request):
    # Your logic for the product view goes here
    return render(request, 'product.html')
