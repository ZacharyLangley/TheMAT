from django.conf.urls import url
from django.conf import settings
from django.views.static import serve
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^venues/$', views.venue_list, name='venues list'),
    url(r'^venue/(?P<venue_id>[0-9]+)$', views.venue_detail, name="venue detail"),
    url(r'^event/(?P<event_id>[0-9]+)$', views.event_detail, name="event detail"),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^register/$', views.register, name='register'),
    url(r'^add_event/$', views.add_event, name='add_event'),
    url(r'^add_venue/$', views.venue_list, name='add_venue'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^userprofile/$', views.userprofile, name='userprofile'),
]
