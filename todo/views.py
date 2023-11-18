from django.shortcuts import render
from django.views.generic import ListView

from todo.models import Task, Tag


class TagListView(ListView):
    model = Tag
    context_object_name = "tags"


class TaskListView(ListView):
    model = Task
    context_object_name = "tasks"
    template_name = "todo/index.html"

