from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, DeleteView

from todo.forms import AddTaskForm, AddTagForm
from todo.models import Task, Tag


class TagListView(ListView):
    model = Tag
    context_object_name = "tags"
    template_name = "todo/tags.html"


class TaskListView(ListView):
    model = Task
    context_object_name = "tasks"
    template_name = "todo/index.html"


class TaskCreateView(CreateView):
    model = Task
    form_class = AddTaskForm
    success_url = reverse_lazy("todo:task-list")


class TaskDoneView(View):
    def post(self, request, pk):
        tag = get_object_or_404(Task, pk=pk)
        tag.status = True
        tag.save()
        return redirect('todo:task-list')

class TaskUnDoneView(View):
    def post(self, request, pk):
        tag = get_object_or_404(Task, pk=pk)
        tag.status = False
        tag.save()
        return redirect('todo:task-list')


class TagCreateView(CreateView):
    model = Tag
    form_class = AddTagForm
    success_url = reverse_lazy("todo:tag-list")


class TagDeleteView(View):

    def post(self, request, pk):
        tag = get_object_or_404(Tag, pk=pk)
        tag.delete()
        return redirect('todo:tag-list')
