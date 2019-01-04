from django.db import models


# Create your models here.
class Project(models.Model):
    """A project that the user is working on"""
    title = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)


class Task(models.Model):
    """A task for a project"""
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'tasks'

    def __str__(self):
        """Return a string representation of the task."""
        return self.text[:50] + "..."
