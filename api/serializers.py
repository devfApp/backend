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
		fields = ['id', 'title', 'description', 'place', 'date_added', 'event_date',
			'event_link',]

class DefaultUserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ['id', 'username', 'first_name', 'last_name', 'email']

class DefaultMyUserSerializer(serializers.ModelSerializer):
	class Meta:
		model = MyUser
		fields = ['id', 'date_added', 'profile_pic', 'is_validated',
			 'phone_number', 'job', 'description',]


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

	added_by=DefaultMyUserSerializer(many=False, read_only=True)
	# skill=DefaultSkillSerializer(many=True)

	added_by_id=serializers.PrimaryKeyRelatedField(write_only=True, 
		queryset=MyUser.objects.all(), source='added_by')

	class Meta:
		model = Event
		fields = ['id', 'title', 'description', 'place', 'date_added', 'event_date', 
			'event_link', 'added_by', 'added_by_id', 'skill']
		read_only_fields=['added_by',]
		write_only_fields=['added_by_id',]

class MyUserSerializer(serializers.ModelSerializer):
	user=DefaultUserSerializer(many=False, read_only=True)
	skill=DefaultSkillSerializer(many=True)
	batch=DefaultBatchSerializer(many=True)

	user_id=serializers.PrimaryKeyRelatedField(write_only=True, queryset=User.objects.all(),
		source='user')


	class Meta:
		model=MyUser
		fields = ['id', 'user', 'user_id', 'date_added', 'profile_pic', 'is_validated',
			 'phone_number', 'job', 'description', 'skill', 'batch']
		read_only_fields=['user',]
		write_only_fields=['user_id']

class SkillSerializer(serializers.ModelSerializer):

	events=serializers.StringRelatedField(many=True)

	class Meta:
		model=Skill
		fields=['id', 'skill', 'events']

class BatchSerializer(serializers.ModelSerializer):

	my_users = MyUserSerializer(many=True)

	class Meta:
		model=Batch
		fields=['id', 'batch', 'my_users']