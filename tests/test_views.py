# todo_app/tests/test_views.py
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework import status
import jwt
from django.conf import settings

class TaskViewTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.token = jwt.encode({'user_id': self.user.id}, settings.JWT_SECRET, algorithm='HS256')
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')

    def test_create_task(self):
        data = {'title': 'Test Task', 'description': 'Test Description'}
        response = self.client.post('/api/tasks/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], 'Test Task')