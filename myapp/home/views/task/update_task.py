from home.models.task import Task
from django.views.generic import UpdateView


class UpdateTaskView(UpdateView):
    model = Task
    template_name = 'task/update_task.html'
    fields = ["name", "description", "status", "due_date"]
    success_url = "/task"
