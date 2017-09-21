# -*- coding: utf-8 -*-
from django.db import models
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.core.validators import URLValidator


class Profile(models.Model):
    """ Extending Django User Model Using a One-To-One Link
        Profile Model, based on WeChat User API
        http://admin.wechat.com/wiki/index.php?title=User_Profile
    """
    SEX_CHOICES = (
        (0, 'Not Set'),
        (1, 'Male'),
        (2, 'Female'),
    )
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Unique user ID for the official account, e.g.: "o6_bmjrPTlm6_2sgVt7hMZOPfL2M"
    openid = models.CharField(max_length=255)
    # User nickname, e.g.: "Band"
    nickname = models.CharField(max_length=255)
    # Shows whether the user has followed the official account. 0: The user is not a follower, and you cannot obtain other information about this user.

    subscribe = models.BooleanField(default=False)
    # The timestamp when the user follows the official account or the last time if the user has followed several times
    # e.g.: "subscribe_time": 1382694957
    subscribe_time = models.IntegerField(null=True)

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
    deposit = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    # 活动积分
    points = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    # 余额
    balance = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    # For Virtual Currencies, such as bitcoin, 图币
    virtual_balance = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    remark = models.TextField()


# Basically we are hooking the create_user_profile and save_user_profile methods to the User model, whenever a save event occurs. This kind of signal is called post_save.
# Reference: https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html#onetoone

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
