# todo_app/tests/test_serializers.py
from django.test import TestCase
from ..serializers import TaskSerializer
from ..models import Task, Category
from django.contrib.auth.models import User

class TaskSerializerTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.category = Category.objects.create(name='Work')
        self.task_data = {
            'title': 'Test Task',
            'description': 'Test Description',
            'status': 'pending',
            'user': self.user,
            'category': self.category
        }

    def test_serializer_valid(self):
        serializer = TaskSerializer(data=self.task_data)
        self.assertTrue(serializer.is_valid())