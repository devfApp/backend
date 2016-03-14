# -*- encoding:utf-8 -*-
from rest_framework import serializers
from user.models import *
from community_event.models import *
from user.models import *

#Default Serializers
class DefaultEventSerializer(serializers.ModelSerializer):
	class Meta:
		model = Event
		fields = ['id', 'title', 'description', 'place', 'date_added', 'event_date', 'event_link',]

class DefaultUserSerializer(serializers.ModelSerializer):
	class Meta:
		model = MyUser
		fields = ['id', 'user', 'date_added', 'profile_pic', 'is_validated', 'phone_number', 
			'job', 'description', 'batch', 'skills']
