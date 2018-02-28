from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index),
	url(r'^add$', views.add),
	url(r'^courses/destroy/(?P<num>\d+)$', views.destroy),
	url(r'^remove/(?P<num>\d+)$', views.remove)
]