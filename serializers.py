# todo_app/serializers.py
from rest_framework import serializers
from .models import Task, Category
from typing import Dict, Any

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'created_at']

class TaskSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        source='category',
        write_only=True,
        required=False
    )

    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'status', 'due_date',
                 'created_at', 'updated_at', 'category', 'category_id']

    def validate(self, data: Dict[str, Any]) -> Dict[str, Any]:
        if 'title' not in data or len(data['title']) < 3:
            raise serializers.ValidationError({"title": "Title must be at least 3 characters long"})
        if 'status' in data and data['status'] not in dict(Task.STATUS_CHOICES):
            raise serializers.ValidationError({"status": "Invalid status value"})
        return data