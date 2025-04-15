# todo_app/services.py
from .models import Task, Category
from rest_framework.exceptions import NotFound, ValidationError
from django.contrib.auth.models import User
from typing import Optional, Dict, Any

class TaskService:
    @staticmethod
    def get_all_tasks(user: User, filters: Optional[Dict[str, Any]] = None) -> models.QuerySet:
        queryset = Task.objects.filter(user=user)
        if filters:
            if 'status' in filters:
                queryset = queryset.filter(status=filters['status'])
            if 'category_id' in filters:
                queryset = queryset.filter(category_id=filters['category_id'])
        return queryset

    @staticmethod
    def get_task_by_id(task_id: int, user: User) -> Task:
        try:
            return Task.objects.get(id=task_id, user=user)
        except Task.DoesNotExist:
            raise NotFound("Task not found")

    @staticmethod
    def create_task(data: Dict[str, Any], user: User) -> Task:
        category_id = data.pop('category_id', None)
        if category_id:
            try:
                data['category'] = Category.objects.get(id=category_id)
            except Category.DoesNotExist:
                raise ValidationError("Invalid category ID")
        return Task.objects.create(user=user, **data)

    @staticmethod
    def update_task(task: Task, data: Dict[str, Any]) -> Task:
        category_id = data.pop('category_id', None)
        if category_id:
            try:
                task.category = Category.objects.get(id=category_id)
            except Category.DoesNotExist:
                raise ValidationError("Invalid category ID")
        for attr, value in data.items():
            setattr(task, attr, value)
        task.save()
        return task

    @staticmethod
    def delete_task(task: Task) -> None:
        task.delete()

class CategoryService:
    @staticmethod
    def get_all_categories() -> models.QuerySet:
        return Category.objects.all()

    @staticmethod
    def create_category(data: Dict[str, Any]) -> Category:
        return Category.objects.create(**data)