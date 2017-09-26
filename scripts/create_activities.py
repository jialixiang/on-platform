#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Script to create On! activities
#

import dateutil.parser
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "on.settings")
django.setup()

from on.base import Activity

activities = [
    {
        'name': u'在线阅读',
        'start_time': '2017-05-01 00:00:00',
        'end_time': '2017-07-31 00:00:00',
        'status': 'complete',
        'coefficient': 10.5,
        'active_participants': 0,
        'max_participants': 500,
        'logoimgurl': 'http://m1.ablwang.com/uploadfile/2015/0507/20150507093857753.jpg',
        'description': u'要么读书，要么旅行，身体和灵魂总有一个在路上',
    },
    {
        'name': u'跑步',
        'start_time': '2017-08-01 00:00:00',
        'end_time': None,
        'status': 'active',
        'coefficient': 30,
        'active_participants': 100,
        'max_participants': 500,
        'logoimgurl': 'https://greatist.com/sites/default/files/styles/list_left_deck/public/JoelRunyon1.jpg?itok=siSQJJ5S',
        'description': u'自由模式-在目标天数内完成自己所设置的距离',
    },
    {
        'name': u'作息',
        'start_time': '2017-10-01 00:00:00',
        'end_time': None,
        'status': 'pending',
        'coefficient': 20,
        'active_participants': 0,
        'max_participants': 500,
        'logoimgurl': 'https://i2.kknews.cc/large/11140000ded9b4d94975',
        'description': u'早睡早起有易于身体健康',
    },
]

if __name__ == '__main__':

    for activity_data in activities:

        print('Creating activity - %s, %s' % (activity_data['name'], activity_data['start_time']))

        # Parse datetime string to Django DateTimeField
        for time_field in ['start_time', 'end_time']:
            if activity_data[time_field]:
                activity_data[time_field] = dateutil.parser.parse(activity_data[time_field])

        # Check if activity already exists
        if Activity.objects.filter(
            name = activity_data['name'],
            start_time = activity_data['start_time']
        ).exists():
            print('\tActivity existing, skipped...')
            continue

        a = Activity(**activity_data)
        a.save()
