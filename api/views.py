from django.shortcuts import render
from rest_framework import generics
from .models import Todo, Project
from .serializers import TodoSerializer, ProjectSerializer


# Create your views here.
class TodoView(generics.ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class CreateTodoView(generics.CreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class ProjectView(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
