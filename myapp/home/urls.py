from django.urls import path
from home.views import (TaskDetailView, TasksView)
from home.views.tasks_view import TaskCreateView, TaskDeleteView, TaskEditView


urlpatterns = [
    path('', TasksView.as_view(), name='index'),
    path('<int:pk>', TaskDetailView.as_view(), name='task-detail'),
    path('add', TaskCreateView.as_view(), name="task-add"),
    path('<int:pk>/delete', TaskDeleteView.as_view(), name="task-delete"),
    path('<int:pk>/edit', TaskEditView.as_view(), name="task-edit"),
]
