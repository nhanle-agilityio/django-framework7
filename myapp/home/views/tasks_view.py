from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from home.models.task import Task
from home.forms.add_task_form import AddTaskForm


# Create your views here.
class TasksView(ListView):
    model = Task
    template_name = 'task_app/index.html'
    context_object_name = 'home'


class TaskCreateView(CreateView):
    template_name = 'task_app/task_add.html'
    form_class = AddTaskForm
    success_url = "/"

    def form_invalid(self, form: BaseModelForm) -> HttpResponse:
        return super().form_invalid(form)


class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'task_app/task_confirm_delete.html'
    success_url = "/"


class TaskEditView(UpdateView):
    model = Task
    template_name = 'task_app/task_edit.html'
    fields = ["name", "description", "status", "due_date"]
    success_url = "/"
