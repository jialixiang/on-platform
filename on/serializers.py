from rest_framework import serializers

from .models import OnUser, Activity, Task, TaskRecord


class OnUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = OnUser
        fields = '__all__'


class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = '__all__'


class RunningTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


class RunningTaskRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskRecord
        fields = '__all__'
