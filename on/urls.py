from django.contrib import admin
from django.conf.urls import url, include

from rest_framework.urlpatterns import format_suffix_patterns

from on import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^$', views.show_activities, name='Home'),

    url(r'^users/$', views.OnUserList.as_view(), name='activity_list'),

    url(r'^activities/$', views.ActivityList.as_view(), name='activity_list'),
    url(r'^activities/(?P<pk>[0-9a-f-]+)/$', views.ActivityDetail.as_view(), name='activity_detail'),

]

urlpatterns = format_suffix_patterns(urlpatterns)
