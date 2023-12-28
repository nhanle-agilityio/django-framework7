import datetime
from django.db import models


class Task(models.Model):
    """Task model"""
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=100)
    due_date = models.DateTimeField(default=datetime.datetime.now, blank=True)

    def __str__(self) -> str:
        return self.name
