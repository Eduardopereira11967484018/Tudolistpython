# todo_app/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import TaskSerializer, CategorySerializer
from .services import TaskService, CategoryService
from .permissions import IsOwner
from rest_framework.permissions import AllowAny
import jwt
from django.conf import settings
from typing import Any

class LoginView(APIView):
    permission_classes = [AllowAny]
    
    def post(self, request: Any) -> Response:
        from django.contrib.auth import authenticate
        user = authenticate(username=request.data['username'], 
                          password=request.data['password'])
        if user:
            token = jwt.encode({'user_id': user.id}, settings.JWT_SECRET, algorithm='HS256')
            return Response({'token': token})
        return Response({'error': 'Invalid credentials'}, status=401)

class TaskListView(APIView):
    def get(self, request: Any) -> Response:
        filters = {
            'status': request.query_params.get('status'),
            'category_id': request.query_params.get('category_id')
        }
        tasks = TaskService.get_all_tasks(request.user, filters)
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    def post(self, request: Any) -> Response:
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            task = TaskService.create_task(serializer.validated_data, request.user)
            return Response(TaskSerializer(task).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TaskDetailView(APIView):
    permission_classes = [IsOwner]

    def get(self, request: Any, pk: int) -> Response:
        task = TaskService.get_task_by_id(pk, request.user)
        serializer = TaskSerializer(task)
        return Response(serializer.data)

    def put(self, request: Any, pk: int) -> Response:
        task = TaskService.get_task_by_id(pk, request.user)
        serializer = TaskSerializer(task, data=request.data, partial=True)
        if serializer.is_valid():
            updated_task = TaskService.update_task(task, serializer.validated_data)
            return Response(TaskSerializer(updated_task).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request: Any, pk: int) -> Response:
        task = TaskService.get_task_by_id(pk, request.user)
        TaskService.delete_task(task)
        return Response(status=status.HTTP_204_NO_CONTENT)

class CategoryListView(APIView):
    def get(self, request: Any) -> Response:
        categories = CategoryService.get_all_categories()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

    def post(self, request: Any) -> Response:
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            category = CategoryService.create_category(serializer.validated_data)
            return Response(CategorySerializer(category).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)