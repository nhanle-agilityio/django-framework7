from django import forms
from home.models.task import Task

TASK_STATUS_CHOICES = [("to-do", "To-Do"), ("in-progress", "In-Progress"),
                       ("ready-for-test", "Ready for test"), ("done", "Done")]


class AddTaskForm(forms.ModelForm):
    name = forms.CharField(required=True, widget=forms.widgets.Input(
        attrs={"class": "form-control", "type": "text"}))
    description = forms.CharField(
        required=False, widget=forms.Textarea(attrs={'rows': 3}))
    status = forms.ChoiceField(choices=TASK_STATUS_CHOICES)
    due_date = forms.DateField(required=False,
                               widget=forms.NumberInput(attrs={'type': 'date'}))

    class Meta:
        model = Task
        fields = ["name", "description", "status", "due_date"]
