from django.conf.urls import patterns, url
from user_prof import views
from project_prof import views as pviews

urlpatterns = patterns('',
		url(r'^$', views.register, name='index'),
		url(r'^$/index.html', views.register, name='index'),
		url(r'^login/$', views.user_login, name='login'),
		(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
		url(r'^user/(?P<user_number>\w+)/$', views.profile_page, name='user page'),
		url(r'^project/(?P<project_number>\w+)/$', pviews.project_page, name='projects'),
		url(r'^start/$', pviews.start_project, name='start project')
		#url(r'^project/(\d)/$', views.project_page, name='project page'),
		)
