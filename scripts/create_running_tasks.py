#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Script to create On! running tasks
#

import dateutil.parser

import django
django.setup()

from django.contrib.auth.models import User
from on.models import Activity, RunningTask, RunningTaskRecord

task_records = [
    {
        'record_time': '2017-09-01 22:00:00',
        'bonus': 5,
        'distance': 7,
        'voucher': None,
    },
    {
        'record_time': '2017-09-02 23:15:00',
        'bonus': -3,
        'distance': 3,
        'voucher': None,
    },
]


if __name__ == '__main__':

    user = User.objects.get(profile__openid='o6_bmjrPTlm6_2sgVt7hMZOPfL2M')
    activity = Activity.objects.get(activity_id='8a171008-c03d-4eb3-81e6-89790363f08b')

    task_data = {
        'start_time': '2017-09-01 00:00:00',
        'end_time': None,
        'status': 'active',
        'mode': u'普通',
        'guaranty': 150,
        'down_payment': 50,
        'coefficient': 30,
        'balance': 200,
        'description': u'测试数据',
        'duration_days': 21,
        'distance': 6,
    }

    # Parse datetime string to Django DateTimeField
    for time_field in ['start_time', 'end_time']:
        if task_data[time_field]:
            task_data[time_field] = dateutil.parser.parse(task_data[time_field])

    try:
        task = RunningTask.objects.get(
            user = user,
            activity = activity,
            start_time = task_data['start_time'],
        )
    except RunningTask.DoesNotExist, e:
        print('Creating task - %s, %s, %s' % (user, activity, task_data['start_time']))
        task = RunningTask(
            user = user,
            activity = activity,
            **task_data
        )
        task.save()
        
    for record_data in task_records:
        print('Creating task record - %s %s' % (task, record_data['record_time']))
        # Parse datetime string to Django DateTimeField
        record_data['record_time'] = dateutil.parser.parse(record_data['record_time'])
        if task.records.filter(record_time=record_data['record_time']).exists():
            print('\tRecord existing, skipped...')
            continue
        record = RunningTaskRecord(
            task=task,
            **record_data
        )
        record.save()
