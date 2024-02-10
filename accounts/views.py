from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate
from django.contrib import messages

from accounts.models import CustomUserCreationForm

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        # Check if username and password are not empty
        if not username or not password:
            messages.error(request, 'Please provide both username and password.')
            return redirect('login')

        # Authenticate user
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to the home page after successful login
        else:
            messages.error(request, 'Invalid username or password.')  # Set error message
            return redirect('login')  # Redirect back to the login page if authentication fails
    else:
        return render(request, 'registration/login.html', {})

def signup_view(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')  # Redirect to the login page after successful signup
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})
