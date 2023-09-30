from django import forms
#from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
# from django.contrib.auth.models import User
from .models import Project


class ProjectForm(ModelForm):

    class Meta:
        model = Project
        fields = ["name", "description"]