from django.shortcuts import render

from .models import Project


# Create your views here.
def index(request):
    """The home page for myapp"""
    return render(request, 'myapp/index.html')


def projects(request):
    """Show all projects"""
    projects = Project.objects.order_by('date_added')
    context = {'projects': projects}
    return render(request, 'myapp/projects.html', context)


def project(request, project_id):
    """Show a single project and all of its tasks"""
    project = Project.objects.get(id=project_id)
    tasks = project.task_set.order_by('-date_added')
    context = {'project': project, 'tasks': tasks}
    return render(request, 'myapp/project.html', context)
