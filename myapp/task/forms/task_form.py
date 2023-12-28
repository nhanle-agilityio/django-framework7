from django import forms
from task.models.task import Task

# Task status
TO_DO, IN_PROGRESS, READY_FOR_TEST, DONE = ('to-do', 'in-progress', 'ready-for-test', 'done')
TASK_STATUS = (
    (TO_DO, 'To-Do'),
    (IN_PROGRESS, 'In Progress'),
    (READY_FOR_TEST, 'Ready For Test'),
    (DONE, 'Done'),
)


class TaskForm(forms.ModelForm):
    name = forms.CharField(required=True, widget=forms.widgets.Input(
        attrs={"class": "form-control", "type": "text"}))
    description = forms.CharField(
        required=False, widget=forms.Textarea(attrs={'rows': 3}))
    status = forms.ChoiceField(choices=TASK_STATUS)
    due_date = forms.DateField(required=False,
                               widget=forms.NumberInput(attrs={'type': 'date'}))

    class Meta:
        model = Task
        fields = ["name", "description", "status", "due_date"]
