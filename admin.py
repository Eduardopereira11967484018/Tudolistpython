# todo_app/admin.py
from django.contrib import admin
from .models import Task, Category

admin.site.register(Task)
admin.site.register(Category)