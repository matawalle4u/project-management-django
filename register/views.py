from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User, Group

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
            return redirect('/projects')
    else:
        # Display an empty AuthenticationForm for GET requests
        form = AuthenticationForm()
    
    return render(request, 'accounts/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('/accounts/login')
    # Redirect to a success page.
            

    

# Define a custom user check function to restrict admin role assignment to certain users (e.g., superusers).
def is_superuser(user):
    return user.is_superuser

@login_required
@user_passes_test(is_superuser)  # Use the custom user check function.
def toggle_admin_role(request, user_id):
    try:
        user = User.objects.get(id=user_id)

        # Check if the user is currently an admin.
        if user.groups.filter(name='Admin').exists():
            # Remove the user from the 'Admin' group.
            admin_group = Group.objects.get(name='Admin')
            user.groups.remove(admin_group)
            messages.success(request, f'{user.username} is no longer an admin.')
        else:
            # Add the user to the 'Admin' group.
            admin_group = Group.objects.get(name='Admin')
            user.groups.add(admin_group)
            messages.success(request, f'{user.username} is now an admin.')

        return redirect('admin_dashboard')  # Redirect to an admin dashboard or user list page.
    except User.DoesNotExist:
        messages.error(request, 'User not found.')
        return redirect('admin_dashboard')  # Redirect to an admin dashboard or user list page.
