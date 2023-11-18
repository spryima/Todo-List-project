from django import forms
from django.forms import DateInput

from todo.models import Task, Tag


class AddTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = "__all__"
        widgets = {
            'deadline': DateInput(attrs={'type': 'date'}),
        }


class AddTagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = "__all__"
