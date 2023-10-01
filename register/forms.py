from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

class EditUserForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2", "is_superuser"]

# class LoginForm(AuthenticationForm):
#     class Meta:
#         model = User
#         fields = ["username", "password1"]