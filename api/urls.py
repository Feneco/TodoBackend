from django.urls import path
from .views import TodoView, ProjectView, CreateTodoView

urlpatterns = [
    path('todo/', TodoView.as_view()),
    path('todo/add', CreateTodoView.as_view()),
    path("project/", ProjectView.as_view())
]
