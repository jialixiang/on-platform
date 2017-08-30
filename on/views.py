from django.shortcuts import render

from .models import Activity


def show_activities(request):
    activities = Activity.objects.all().order_by('start_time')
    return render(request, 'on/index.html', {
        'activities': activities
    })
