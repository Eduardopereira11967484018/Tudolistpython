# todo_app/urls.py
from django.urls import path
from .views import TaskListView, TaskDetailView, CategoryListView, LoginView
from .docs import schema_view

urlpatterns = [
    path('tasks/', TaskListView.as_view(), name='task-list'),
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('login/', LoginView.as_view(), name='login'),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]