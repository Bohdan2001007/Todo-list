from django.test import TestCase
from django.urls import reverse
from datetime import datetime
from tasks.models import Tag, Task


TASK_URL = reverse("tasks:TaskListView")
TAG_URL = reverse("tasks:TagListView")


class ModelsTests(TestCase):
    def test_tag_str(self):
        tag = Tag.objects.create(name="Test")

        self.assertEqual(
            str(tag),
            f"{tag.name}",
        )


class DataTasksTests(TestCase):
    def test_get_tasks_data(self):
        response = self.client.get(TASK_URL)

        self.assertEqual(response.status_code, 200)


class CreateTaskTests(TestCase):
    def test_create_task(self):
        self.task = Task.objects.create(
            content="test",
            datetime=datetime.now(),
        )
        response = self.client.get(TASK_URL)

        all_tasks = Task.objects.all()
        self.assertEqual(response.status_code, 200)
        self.assertEqual((list(all_tasks)), list(all_tasks))


class DataTagsTests(TestCase):
    def test_get_tags_data(self):
        response = self.client.get(TAG_URL)

        self.assertEqual(response.status_code, 200)


class CreateTagTests(TestCase):
    def test_create_tag(self):
        self.tag = Tag.objects.create(
            name="test",
        )
        response = self.client.get(TAG_URL)

        all_tags = Tag.objects.all()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(list(all_tags), list(all_tags))
