"""Defines URL patterns for myapp."""

from django.urls import path

from . import views

app_name = 'myapp'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),

    # Show all projects
    path('projects/', views.projects, name='projects'),

    # Detail page for a single project
    path('projects/<int:project_id>/', views.project, name='project'),
]
