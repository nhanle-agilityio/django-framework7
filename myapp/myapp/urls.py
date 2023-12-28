"""
URL configuration for myapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.task, name='task')
Class-based views
    1. Add an import:  from other_app.views import Task
    2. Add a URL to urlpatterns:  path('', Task.as_view(), name='task')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from task.views.task.create_task import CreateTaskView
from task.views.task.delete_task import DeleteTaskView
from task.views.task.task_detail import TaskDetailView
from task.views.task.task_list import TaskListView
from task.views.task.update_task import UpdateTaskView

urlpatterns = [
    path('admin/', admin.site.urls),
    # Task
    path('task/', TaskListView.as_view(), name='task-list'),
    path('task/<int:pk>', TaskDetailView.as_view(), name='task-detail'),
    path('task/create', CreateTaskView.as_view(), name="create-task"),
    path('task/<int:pk>/delete', DeleteTaskView.as_view(), name="delete-task"),
    path('task/<int:pk>/update', UpdateTaskView.as_view(), name="update-task"),
]
