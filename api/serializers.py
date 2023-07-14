from rest_framework import serializers
from .models import Todo, Project


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ("id", "name", "description", "pub_date", "to_date", "project", "blocking")


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ("id", "name", "description")