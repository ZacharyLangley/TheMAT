from django.conf.urls import url
from django.conf import settings
from django.views.static import serve
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^profiles/$', views.profileList, name='profiles'),
    url(r'^profiles/(?P<venue_id>[0-9]+)$', views.profile, name="profile"),
    url(r'^event/(?P<event_id>[0-9]+)$', views.event_page, name="event page"),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^register/$', views.register, name='register'),
    url(r'^add_event/$', views.add_event, name='add_event'),
    url(r'^add_venue/$', views.profileList, name='add_venue'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^userprofile/$', views.userprofile, name='userprofile'),
]
