from django.http import Http404
from django.shortcuts import render

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Activity, Task, TaskRecord
from .serializers import ActivitySerializer, TaskSerializer, TaskRecordSerializer


class ActivityList(APIView):
    """ List all activities, or create a new activity """
    def get(self, request, format=None):
        activities = Activity.objects.all()
        serializer = ActivitySerializer(activities, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        # TODO: need to set admin permission only
        serializer = ActivitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ActivityDetail(APIView):
    """ Retrieve, update or delete a activity instance """
    def get_object(self, activity_id):
        try:
            return Activity.objects.get(activity_id=activity_id)
        except Activity.DoesNotExist:
            raise Http404

    def get(self, request, activity_id, format=None):
        activity = self.get_object(activity_id)
        serializer = ActivitySerializer(activity)
        return Response(serializer.data)

    def put(self, request, activity_id, format=None):
        activity = self.get_object(activity_id)
        serializer = ActivitySerializer(activity, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, activity_id, format=None):
        activity = self.get_object(activity_id)
        activity.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


def show_activities(request):
    activities = Activity.objects.all().order_by('start_time')
    return render(request, 'on/index.html', {
        'activities': activities
    })
