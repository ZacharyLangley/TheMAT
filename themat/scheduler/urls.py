from django.conf.urls import url
from django.conf import settings
from django.views.static import serve
from . import views


urlpatterns = [
    #Index
    url(r'^$', views.index, name='index'),
    url(r'^profiles/$', views.profileList, name='profiles'),
    url(r'^profiles/(?P<venue_id>[0-9]+)$', views.profile, name="profile"),

]
