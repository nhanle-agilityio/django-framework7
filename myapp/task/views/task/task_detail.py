from django.views.generic import DetailView
from task.models.task import Task


# Create your views here.
class TaskDetailView(DetailView):
    model = Task
    template_name = 'task/task_detail.html'
    context_object_name = 'detail'
