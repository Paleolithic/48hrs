from django.conf.urls import patterns, url
from user_prof import views

urlpatterns = patterns('',
		url(r'^user/(?P<user_name>\w+)/$'. views.userPage, name='user page'),
		)
