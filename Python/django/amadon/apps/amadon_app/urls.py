from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^amadon$', views.index),
	url(r'^amadon/receipt$', views.receipt),
	url(r'^amadon/checkout$', views.checkout),
	url(r'^amadon/purchase$', views.purchase),
]