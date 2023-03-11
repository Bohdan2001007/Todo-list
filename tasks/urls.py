from django.urls import path

from tasks.views import TaskListView, TaskCreateView, TaskUpdateView, TaskDeleteView, TagListView, TagCreateView, \
    TagUpdateView, TagDeleteView, TaskStatusUpdateView

urlpatterns = [
    path("", TaskListView.as_view(), name="TaskListView"),
    path(
        "tasks/create/",
        TaskCreateView.as_view(),
        name="task-create",
    ),
    path(
        "tasks/<int:pk>/update/",
        TaskUpdateView.as_view(),
        name="task-update"
    ),
    path(
        "tasks/<int:pk>/delete/",
        TaskDeleteView.as_view(),
        name="task-delete"
    ),
    path("task-status/<int:pk>/", TaskStatusUpdateView.as_view(), name="change-task"),
    path("tags/", TagListView.as_view(), name="TagListView"),
    path(
        "tags/create/",
        TagCreateView.as_view(),
        name="tag-create",
    ),
    path(
        "tags/<int:pk>/update/",
        TagUpdateView.as_view(),
        name="tag-update"
    ),
    path(
        "tags/<int:pk>/delete/",
        TagDeleteView.as_view(),
        name="tag-delete"
    ),
]

app_name = "tasks"
