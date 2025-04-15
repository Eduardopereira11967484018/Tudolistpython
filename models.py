# todo_app/models.py
from django.db import models
from django.contrib.auth.models import User
from typing import Optional

class Category(models.Model):
    name: str = models.CharField(max_length=100, unique=True)
    created_at: models.DateTimeField = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name

rect

class Task(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    )
    
    title: str = models.CharField(max_length=200)
    description: str = models.TextField(blank=True)
    status: str = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    due_date: Optional[models.DateTimeField] = models.DateTimeField(null=True, blank=True)
    created_at: models.DateTimeField = models.DateTimeField(auto_now_add=True)
    updated_at: models.DateTimeField = models.DateTimeField(auto_now=True)
    user: models.ForeignKey = models.ForeignKey(User, on_delete=models.CASCADE)
    category: Optional[models.ForeignKey] = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True
    )

    def __str__(self) -> str:
        return self.title