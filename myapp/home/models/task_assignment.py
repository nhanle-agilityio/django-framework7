from django.db import models
from home.models.task import Task
from home.models.user import UserProfile


class TaskAssignment(models.Model):
    """Task Assignment model - Intermediate table between Task and User"""

    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name="task_assignments")
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="task_assignments")
