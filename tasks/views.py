from django.urls import reverse_lazy
from django.views import generic

from tasks.models import Task


class TaskListView(generic.ListView):
    model = Task
    template_name = "tasks/ToDoHomePage.html"
    context_object_name = "tasks_list"


class TaskCreateView(generic.CreateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("tasks:TaskListView")
    template_name = "tasks/task_form.html"
