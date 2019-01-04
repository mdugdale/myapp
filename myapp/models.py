from django.db import models


# Create your models here.
class Project(models.Model):
    """A project that the user is working on"""
    title = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
