from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^radar/', views.radar, name='radar'),
	url(r'^credits/', views.about, name='credits'),
]
