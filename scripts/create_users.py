#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Script to create On! test users
#

import django
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "on.settings")
django.setup()

from on.user import Profile
from django.contrib.auth.models import User

profiles = [
    {
        'openid': 'o6_bmjrPTlm6_2sgVt7hMZOPfL2M',
        'nickname': 'test',
        'subscribe': True,
        'subscribe_time': 1382694957,
        'sex': 2,
        'city': 'Hongkong',
        'province': 'Hongkong',
        'country': 'China',
        'language': 'zh_CN',
        'headimgurl': 'http://wx.qlogo.cn/mmopen/g3MonUZtNHkdmzicIlibx6iaFqAc56vxLSUfpb6n5WKSYVY0ChQKkiaJSgQ1dZuTOgvLLrhJbERQQ4eMsv84eavHiaiceqxibJxCfHe/0',
        'deposit': 200,
        'points': 0,
        'balance': 200,
        'virtual_balance': 0,
        'remark': 'Test user',
    },
    {
        'openid': 'i9_bmudhakfq_fSFdf9fdZOPfKLI',
        'nickname': 'test2',
        'subscribe': True,
        'subscribe_time': 1382678906,
        'sex': 1,
        'city': 'Wuhu',
        'province': 'Anhui',
        'country': 'China',
        'language': 'zh_CN',
        'headimgurl': 'http://wx.qlogo.cn/mmopen/g3MonUZtNHkdmzicIlibx6iaFqAc56vxLSUfpb6n5WKSYVY0ChQKkiaJSgQ1dZuTOgvLLrhJbERQQ4eMsv84eavHiaiceqxibJxCfHe/0',
        'deposit': 1000,
        'points': 320,
        'balance': 500,
        'virtual_balance': 150,
        'remark': 'Test user2',
    },
]


if __name__ == '__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "on.settings")

    for profile_data in profiles:
        # Skip if no openid
        if not profile_data['openid']:
            continue

        print('Cresting user - %s' % profile_data['openid'])
        # Check if user already exists
        if User.objects.filter(profile__openid=profile_data['openid']).exists():
            print('\tUser existing, skipped...')
            continue

        user = User(username = profile_data['openid'])
        user.save()
        user.profile.__dict__.update(**profile_data)
        user.save()
