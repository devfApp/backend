from django.conf.urls import url, include
from . import views as api_view
from rest_framework.authtoken import views as token_view

urlpatterns = [
	#Events urls
	url(r'event/$', api_view.EventView.as_view()),
	url(r'event/(?P<pk>[0-9]+)/$', api_view.EventDetailView.as_view(), name='event_api_detail'),

	#Batch urls
	url(r'batch/$', api_view.BatchView.as_view()),

	#Skill urls
	url(r'skill/$', api_view.SkillView.as_view()),

	#MyUser urls
	url(r'user/$', api_view.MyUserView.as_view()),
	url(r'user/(?P<pk>[0-9]+)/$', api_view.MyUserDetailView.as_view(), name='user_api_detail'),

]