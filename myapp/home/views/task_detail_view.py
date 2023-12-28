from django.views.generic import DetailView
from home.models.task import Task


# Create your views here.
class TaskDetailView(DetailView):
    model = Task
    template_name = 'task_detail/index.html'
    context_object_name = 'detail'
