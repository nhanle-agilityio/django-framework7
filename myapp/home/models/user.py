from django.db import models
from home.models.task import Task


class User(models.Model):
    """User model"""

    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    tasks = models.ManyToManyField(Task, through="TaskAssignment", related_name='users', blank=True)

    def __str__(self) -> str:
        return self.name
