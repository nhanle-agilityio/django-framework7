from django.forms import BaseModelForm
from django.http import HttpResponse
from django.views.generic import CreateView
from home.forms.task_form import TaskForm


class CreateTaskView(CreateView):
    template_name = 'task/create_task.html'
    form_class = TaskForm
    success_url = "/task"

    def form_invalid(self, form: BaseModelForm) -> HttpResponse:
        return super().form_invalid(form)
