from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index),
	url(r'^register$', views.register),
	url(r'^login$', views.login),
	url(r'^success$', views.success),
	url(r'^books/add$', views.add),
	url(r'^addbook$', views.add_book),
	url(r'^books/(?P<id>\d+)$', views.book_reviews),
	url(r'^addreview/(?P<id>\d+)$', views.add_review),
	url(r'^users/(?P<id>\d+)$', views.user_reviews),
	url(r'^delete/(?P<id>\d+)/(?P<book_id>\d+)$', views.delete_review),
	url(r'^logout$', views.logout),
]