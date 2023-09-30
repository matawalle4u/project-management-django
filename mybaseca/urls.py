"""mybaseca URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from register import views as v
from project import views as project_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("register/", v.register, name="register"),
    path("projects/", project_views.get_user_project, name="get_user_project"),
    path("project/new", project_views.new, name="new"),
    path("accounts/login", v.login_view, name="login_view"),
    path('accounts/logout', v.logout_view, name="logout_view"),
    path('project/edit/<int:pk>/', project_views.edit_project, name="edit_project"),
    path('project/delete/<int:pk>/', project_views.delete_project, name="delete_project"),
   

    
]
