from django.contrib import admin

from tasks.models import Task, Tag


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_filter = ["content", "datetime", "deadline", "is_done", "tags"]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_filter = ["name"]
