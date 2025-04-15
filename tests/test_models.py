# todo_app/tests/test_models.py
from django.test import TestCase
from django.contrib.auth.models import User
from ..models import Task, Category

class TaskModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.category = Category.objects.create(name='Work')

    def test_task_creation(self):
        task = Task.objects.create(
            title='Test Task',
            description='Test Description',
            user=self.user,
            category=self.category
        )
        self.assertEqual(str(task), 'Test/Task')
        self.assertEqual(task.status, 'pending')