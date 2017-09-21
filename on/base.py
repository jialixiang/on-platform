# -*- coding: utf-8 -*-
import uuid

from django.db import models
from django.contrib.auth.models import User
from django.core.validators import URLValidator


class Activity(models.Model):
    """ Model for Activities within On! Platform, such as Running, Sleeping, etc
        Activity is composed of several users' tasks
    """
    activity_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)

    start_time = models.DateTimeField(null=False)
    end_time = models.DateTimeField(null=True)
    # Activity status, pending, active, paused, complete
    status = models.CharField(max_length=255)

    coefficient = models.DecimalField(max_digits=12, decimal_places=2)
    active_participants = models.IntegerField(default=0)
    max_participants = models.IntegerField(default=0)

    # Each activity has its own logo
    logoimgurl = models.CharField(max_length=300, validators=[URLValidator()])
    description = models.TextField()


class Task(models.Model):
    """ Abstract Model for user tasks within On! Platform
        User has his/her own objective for each task

        Detailed objectives will be defined in each specific task
    """
    task_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, related_name="tasks", on_delete=models.PROTECT)
    activity = models.ForeignKey(Activity, related_name="tasks", on_delete=models.PROTECT)

    start_time = models.DateTimeField(null=False)
    end_time = models.DateTimeField(null=True)
    # Task status, pending, active, paused, complete
    status = models.CharField(max_length=255)
    # User selected task mode, 普通, 学生, 尝试, etc
    mode = models.CharField(max_length=255)

    # 保证金
    guaranty = models.DecimalField(max_digits=12, decimal_places=2)
    # 底金
    down_payment = models.DecimalField(max_digits=12, decimal_places=2)

    # 系数
    coefficient = models.DecimalField(max_digits=12, decimal_places=2)
    balance = models.DecimalField(max_digits=12, decimal_places=2)
    description = models.TextField()

    class Meta:
        abstract = True


class TaskRecord(models.Model):
    """ Abstract Daily / Hourly Record for User Task
        Such as time for sleep and get up, etc

        Details will be defined in each specific task record
    """
    # Time when user creates the record
    record_time = models.DateTimeField(null=False)

    # Bonus can be -/+, depends on user complete the task or not
    bonus = models.DecimalField(max_digits=12, decimal_places=2)

    class Meta:
        abstract = True
