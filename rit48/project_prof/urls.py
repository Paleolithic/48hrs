from django.conf.urls import patterns, url
from project_prof import views

urlpatterns = patterns('',
		#url(r'^projects/$', views.projects, name='projects'),
		url(r'^project/(?P<project_number>)/$', views.project_page, name='project page'),
		)
