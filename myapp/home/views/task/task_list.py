from django.views.generic import ListView
from home.models.task import Task


class TaskListView(ListView):
    model = Task
    template_name = 'task/task_list.html'
    context_object_name = 'home'
