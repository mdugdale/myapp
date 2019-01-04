"""Defines URL patterns for myapp."""

from django.urls import path

from . import views

app_name = 'myapp'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
]
