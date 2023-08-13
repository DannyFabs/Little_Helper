from django import forms
from .models import Task


# forms


class CreateTask(forms.ModelForm):
    task_name = forms.CharField(label='Task Name')
    task_date = forms.DateField(label='Task Date', widget=forms.TextInput(attrs={'type': 'date', }))
    task_time = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}))
    task_description = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Describe task to your future self'}))

    class Meta:
        model = Task
        exclude = ('author', 'task_slug')
