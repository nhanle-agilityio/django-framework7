from django.db import models
from django.contrib.auth.models import User
from home.models.task import Task


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    tasks = models.ManyToManyField(Task, through="TaskAssignment", related_name='users', blank=True)

    def __str__(self):
        return "@{}".format(self.user.name)
