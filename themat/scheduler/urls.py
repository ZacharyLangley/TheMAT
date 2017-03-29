from django.conf.urls import url
from django.conf import settings
from django.views.static import serve
from . import views


urlpatterns = [
    #Index
    url(r'^$', views.index, name='index'),
    url(r'^profile/$', views.profile, name='profile'),
]
