from django.conf.urls import url
from django.conf import settings
from django.views.static import serve
from django.conf.urls.static import static
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^venues/$', views.venue_list, name='venues list'),
    url(r'^venue/(?P<venue_id>[0-9]+)$', views.venue_detail, name="venue detail"),
    url(r'^event/(?P<event_id>[0-9]+)$', views.event_detail, name="event detail"),
    url(r'^editevent/$', views.event_detail, name="edit event"),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^register/$', views.register, name='register'),
    url(r'^add_event/$', views.add_event, name='add_event'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^profile/$', views.userprofile, name='userprofile'),
]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
