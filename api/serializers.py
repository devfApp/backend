# -*- encoding:utf-8 -*-
from rest_framework import serializers
from django.contrib.auth.models import User
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
		model = User
		fields = ['id', 'username', 'first_name', 'last_name', 'email']

class DefaultMyUserSerializer(serializers.ModelSerializer):
	user = DefaultUserSerializer(many=False, read_only=True)

	user_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=User.objects.all())

	class Meta:
		model = MyUser
		fields = ['id', 'user', 'user_id', 'date_added', 'profile_pic', 'is_validated', 'phone_number', 
			'job', 'description',]
		read_only_fields=['user',]
		write_only_fields=['user_id',]

class DefaultBatchSerializer(serializers.ModelSerializer):
	class Meta:
		model=Batch
		fields=['id', 'batch']

class DefaultSkillSerializer(serializers.ModelSerializer):
	class Meta:
		model=Skill
		fields=['id', 'skill']

#Event Serializer
class EventSerializer(serializers.ModelSerializer):
	class 