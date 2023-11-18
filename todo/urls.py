from django.urls import path

from todo.views import (
    TagListView,
    TaskListView,
    TaskCreateView,
    TagCreateView,
    TagDeleteView,
    TaskDoneView,
    TaskUnDoneView,
    TagUpdateView
)

urlpatterns = [
    path("", TaskListView.as_view(), name="task-list"),
    path("tags/", TagListView.as_view(), name="tag-list"),
    path("task/create/", TaskCreateView.as_view(), name="task-create"),
    path("tag/create/", TagCreateView.as_view(), name="tag-create"),
    path("task/<int:pk>/done/", TaskDoneView.as_view(), name="task-done"),
    path("task/<int:pk>/undone/", TaskUnDoneView.as_view(), name="task-undone"),
    path("tag/<int:pk>/delete/", TagDeleteView.as_view(), name="tag-delete"),
    path("tag/<int:pk>/update/", TagUpdateView.as_view(), name="tag-update"),

]

app_name = "todo"
