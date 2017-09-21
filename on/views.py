from django.http import Http404
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from rest_framework import status
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Activity, Task, TaskRecord
from .serializers import UserSerializer, ActivitySerializer
from .serializers import RunningTaskSerializer, RunningTaskRecordSerializer


class UserList(generics.ListCreateAPIView):
    """ List all users, or create a new user"""
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    """ Retrieve, update or delete a user """
    # TODO: need to set admin permission only for PUT/DELETE
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ActivityList(generics.ListCreateAPIView):
    """ List all activities, or create a new activity """
    # TODO: need to set admin permission only for POST
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer


class ActivityDetail(generics.RetrieveUpdateDestroyAPIView):
    """ Retrieve, update or delete a activity instance """
    # TODO: need to set admin permission only for PUT/DELETE
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer


##############################################################


def login(request):
    print request
    return redirect('home')


def show_activities(request):
    activities = Activity.objects.all().order_by('start_time')
    return render(request, 'on/index.html', {
        'activities': activities
    })
