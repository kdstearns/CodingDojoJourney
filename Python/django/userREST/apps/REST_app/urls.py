from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.main),
	url(r'^users$', views.index),
	url(r'^users/new$', views.new),
	url(r'^users/(?P<num>\d+)/edit$', views.edit),
	url(r'^users/(?P<num>\d+)$', views.show),
	url(r'^users/create$', views.create),
	url(r'^users/(?P<num>\d+)/update$', views.update),
	url(r'^users/(?P<num>\d+)/destroy$', views.destroy)
]