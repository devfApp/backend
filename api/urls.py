from django.conf.urls import url, include
from . import views as api_view
from rest_framework.authtoken import views as token_view

urlpatterns = [
	#Events urls
	url(r'event/$', api_view.EventView.as_view(), name='event_api'),
	url(r'event/(?P<pk>[0-9]+)/$', api_view.EventDetailView.as_view(), name='event_api_detail'),

	#Batch urls
	url(r'batch/$', api_view.BatchView.as_view(), name='batch_api'),
	url(r'batch/(?P<pk>[0-9]+)/$', api_view.BatchDetailView.as_view(), name='batch_api_detail'),

	#Skill urls
	url(r'skill/$', api_view.SkillView.as_view(), name='skill_api'),
	url(r'skill/(?P<pk>[0-9]+)/$', api_view.SkillDetailView.as_view(), name='skill_api_detail'),

	#MyUser urls
	url(r'user/$', api_view.MyUserView.as_view(), name='user_api'),
	url(r'user/(?P<pk>[0-9]+)/$', api_view.MyUserDetailView.as_view(), name='user_api_detail'),

	#Files urls
	url(r'file/$', api_view.FileView.as_view(), name='file_api'),
	url(r'file/(?P<pk>[0-9]+)/$', api_view.FileDetailView.as_view(), name='file_api_detail'),

	#Challenge urls
	url(r'challenge/$', api_view.ChallengeView.as_view(), name='challenge_api'),
	url(r'challenge/(?P<pk>[0-9]+)/$', api_view.ChallengeDetailView.as_view(), name='challenge_api_detail'),

	url(r'answer/$', api_view.AnswerView.as_view(), name='answer_api'),

	#DOCS
	url(r'docs/', include('rest_framework_swagger.urls')),
]