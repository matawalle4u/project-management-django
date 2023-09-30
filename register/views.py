from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages

from .forms import RegisterForm


# Create your views here.
def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
        return redirect("/")
    else:
        form = RegisterForm()

    return render(response, "register/register.html", {"form":form})

def login_view(request):
    if request.method == 'POST':
        # Create an instance of the AuthenticationForm with POST data
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # Log in the user if the form is valid
            login(request, form.get_user())
            # Redirect to a success page, e.g., the user's profile page
            return redirect('/project/new')
    else:
        # Display an empty AuthenticationForm for GET requests
        form = AuthenticationForm()
    
    return render(request, 'accounts/login.html', {'form': form})


            

    
