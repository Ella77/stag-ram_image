from django.conf.urls import include, url

from . import views



urlpatterns= [
    url(r'^(?P<username>[\w.@+-]+)/$', views.profile, name= 'profile'),


]