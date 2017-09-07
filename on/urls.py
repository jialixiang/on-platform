from django.contrib import admin
from django.conf.urls import url, include

from rest_framework.urlpatterns import format_suffix_patterns

from on import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^$', views.show_activities, name='Home'),
    url(r'^activities/$', views.ActivityList.as_view(), name='ActivityList'),
    url(r'^activities/(?P<activity_id>[0-9a-f-]+)/$', views.ActivityDetail.as_view(), name='ActivityDetail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
