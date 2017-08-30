from django.conf.urls import url
from django.contrib import admin

from on.views import show_activities

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^$', show_activities, name='Home')
]
