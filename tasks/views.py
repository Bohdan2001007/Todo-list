from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import generic

from tasks.models import Task, Tag


class TaskListView(generic.ListView):
    model = Task
    template_name = "tasks/ToDoHomePage.html"
    context_object_name = "tasks_list"


class TaskCreateView(generic.CreateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("tasks:TaskListView")
    template_name = "tasks/task_form.html"


class TaskUpdateView(generic.UpdateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("tasks:TaskListView")
    template_name = "tasks/task_form.html"


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("tasks:TaskListView")
    template_name = "tasks/task_form_confirm_delete.html"


class TagListView(generic.ListView):
    model = Tag
    template_name = "tasks/tag_list.html"
    context_object_name = "tags_list"


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("tasks:TagListView")
    template_name = "tasks/tag_form.html"


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("tasks:TagListView")
    template_name = "tasks/tag_form.html"


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("tasks:TagListView")
    template_name = "tasks/tag_form_confirm_delete.html"


def change_task(request, pk):
    task = Task.objects.get(id=pk)
    if task.is_done is True:
        task.is_done = False
    else:
        task.is_done = True
    task.save()
    return HttpResponseRedirect(reverse_lazy("tasks:TaskListView"))
