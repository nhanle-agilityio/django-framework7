from task.models.task import Task
from django.views.generic import DeleteView


class DeleteTaskView(DeleteView):
    model = Task
    template_name = 'task/delete_task.html'
    success_url = "/task"
