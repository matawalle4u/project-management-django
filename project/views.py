from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Project

from .forms import ProjectForm


# Create your views here.

@login_required
def new(response):
    if response.method == "POST":
        form = ProjectForm(response.POST)
        if form.is_valid():
            saving = form.save(commit=False)
            saving.owner = response.user
            saving.save()
        return redirect("/projects")
    else:
        form = ProjectForm()

    return render(response, "project/new.html", {"form":form})

@login_required
def get_user_project(request):
    
    user_projects = Project.objects.filter(owner=request.user)
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            saving = form.save(commit=False)
            saving.owner = request.user
            
            saving.save()
        return redirect("/project/new")
    else:
        form = ProjectForm()

    return render(request, "project/project_lists.html", {'user_projects':user_projects})

    

@login_required
def projects(request):
    all_projects = Project.objects.all()
    return render(request, 'project/new.html', {'all_projects': all_projects})


@login_required
def edit_project(request, pk):
    project = Project.objects.get(pk=pk)
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('/project/new')
    else:
        form = ProjectForm(instance=project)
    return render(request, 'project/new.html', {'form': form, 'task': project})

@login_required
def delete_project(request, pk):
    project = Project.objects.get(pk=pk)
    project.delete()
    return redirect('/project/new')