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

	#DOCS
	url(r'docs/', include('rest_framework_swagger.urls'))
]