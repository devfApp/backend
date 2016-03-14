from django.conf.urls import url, include
from . import views as api_view
from rest_framework.authtoken import views as token_view

urlpatterns = [
	#Events
	url(r'event/', api_view.EventView.as_view()),

	#User
	url(r'user/', api_view.UserView.as_view()),
]