from django.contrib import admin
from django.conf.urls import url, include

from rest_framework.urlpatterns import format_suffix_patterns

from on import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^home/$', views.show_activities, name='home'),
    url(r'^login/$', views.login, name='login'),

    url(r'^users/$', views.UserList.as_view(), name='user_list'),
    url(r'^users/(?P<pk>\d+)/$', views.UserDetail.as_view(), name='user_detail'),

    url(r'^activities/$', views.ActivityList.as_view(), name='activity_list'),
    url(r'^activities/(?P<pk>[0-9a-f-]+)/$', views.ActivityDetail.as_view(), name='activity_detail'),

]

urlpatterns = format_suffix_patterns(urlpatterns)
