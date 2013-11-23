from django.conf.urls import patterns, url
from user_prof import views

urlpatterns = patterns('',
		url(r'^$', views.register, name='index'),
		url(r'^$/index.html', views.register, name='index'),
		url(r'^user/(?P<user_name>\w+)/$', views.userPage, name='user page'),
		)
