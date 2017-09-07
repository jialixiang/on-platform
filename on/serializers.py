from rest_framework import serializers

from .models import Activity, Task, TaskRecord


class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = '__all__'


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


class TaskRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskRecord
        fields = '__all__'
