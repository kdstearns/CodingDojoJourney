from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index),
	url(r'^register$', views.register),
	url(r'^login$', views.login),
	url(r'^success$', views.success),
	url(r'^addquote$', views.addquote),
	url(r'^addlist/(?P<id>\d+)$', views.addlist),
	url(r'^removelist/(?P<id>\d+)$', views.removelist),
	url(r'^userposts/(?P<id>\d+)$', views.userposts),
	url(r'^logout$', views.logout),
]