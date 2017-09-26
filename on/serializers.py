from rest_framework import serializers
from django.contrib.auth.models import User

from on.models import Profile, Activity
from on.models import RunningTask, RunningTaskRecord


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(many=False, read_only=True)
    class Meta:
        model = User
        fields = '__all__'


class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = '__all__'


class RunningTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = RunningTask
        fields = '__all__'


class RunningTaskRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = RunningTaskRecord
        fields = '__all__'
