# -*- coding: utf-8 -*-
import uuid
from django.db import models
from django.core.validators import URLValidator


class OnUser(models.Model):
    """ On User Model, based on WeChat User API
        http://admin.wechat.com/wiki/index.php?title=User_Profile
    """
    SEX_CHOICES = (
        (0, 'Not Set'),
        (1, 'Male'),
        (2, 'Female'),
    )

    # Unique user ID for the official account, e.g.: "o6_bmjrPTlm6_2sgVt7hMZOPfL2M"
    openid = models.CharField(max_length=255)
    # User nickname, e.g.: "Band"
    nickname = models.CharField(max_length=255)
    # Shows whether the user has followed the official account. 0: The user is not a follower, and you cannot obtain other information about this user.

    subscribe = models.BooleanField(default=False)
    # The timestamp when the user follows the official account or the last time if the user has followed several times
    # e.g.: "subscribe_time": 1382694957
    subscribe_time = models.IntegerField()

    # 1: Male; 2: Female; 0: Not Set
    sex = models.IntegerField(choices=SEX_CHOICES, default=0)
    # e.g.: "city": "Guangzhou", "province": "Guangdong", "country": "China"
    city = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    province = models.CharField(max_length=255)
    # zh_CN: Simplified Chinese, zh_TW: Traditional Chinese, en: English
    language = models.CharField(max_length=255)
    # Profile photo URL. The last number in the URL shows the size of the square image, which can be 0 (640*640), 46, 64, 96 and 132. This parameter is null if the user hasn't set a profile photo
    # e.g.: "http://wx.qlogo.cn/mmopen/g3MonUZtNHkdmzicIlibx6iaFqAc56vxLSUfpb6n5WKSYVY0ChQKkiaJSgQ1dZuTOgvLLrhJbERQQ4eMsv84eavHiaiceqxibJxCfHe/0"
    headimgurl = models.CharField(max_length=300, validators=[URLValidator()])

    # ================== For On Platform ==================
    # 活动押金
    deposit = models.DecimalField(max_digits=12, decimal_places=2)
    # 活动积分
    points = models.DecimalField(max_digits=12, decimal_places=2)
    # 余额
    balance = models.DecimalField(max_digits=12, decimal_places=2)
    # For Virtual Currencies, such as bitcoin, 图币
    virtual_balance = models.DecimalField(max_digits=12, decimal_places=2)
    remark = models.TextField()


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
    user = models.ForeignKey(OnUser, related_name="tasks", on_delete=models.PROTECT)
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
