# -*- encoding:utf-8 -*-
from rest_framework import serializers
from django.contrib.auth.models import User
from user.models import *
from community_event.models import *
from user.models import *
from shared_files.models import *

#Default Serializers
"""
Default se refiere a los serializers que solo van a regresar los ATRIBUTOS de los 
modelos para poder reutilizarlos
"""
class DefaultEventSerializer(serializers.ModelSerializer):
	"""Default list for EVENTS without its relations"""

	class Meta:
		model = Event
		fields = ['id', 'title', 'description', 'place', 'date_added', 'event_date',
			'event_link',]

class DefaultUserSerializer(serializers.ModelSerializer):
	"""Default list for USER without its relations"""
	class Meta:
		model = User
		fields = ['id', 'username', 'first_name', 'last_name', 'email']

class DefaultMyUserSerializer(serializers.ModelSerializer):
	"""Default list for MYUSER without its relations"""
	user = DefaultUserSerializer(many=False)

	class Meta:
		model = MyUser
		fields = ['id', 'user', 'date_added', 'profile_pic', 'is_validated',
			 'phone_number', 'job', 'description',]

class DefaultBatchSerializer(serializers.ModelSerializer):
	"""Default list for BATCH without its relations"""

	class Meta:
		model=Batch
		fields=['id', 'batch']

class DefaultSkillSerializer(serializers.ModelSerializer):
	"""Default list for SKILL without its relations"""

	class Meta:
		model=Skill
		fields=['id', 'skill']

class DefaultFileSerializer(serializers.ModelSerializer):
	class Meta:
		model=File
		fields=['id', 'title', 'description', 'file_link', 'date']

"""
Aquí comienzan los seriealizers con ATRIBUTOS y RELACIONES
"""

#MyUser Serializer
class MyUserSerializer(serializers.ModelSerializer):
	"""MYUSER object list and create object with relations"""

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

#Event Serializer
class EventSerializer(serializers.ModelSerializer):
	"""EVENT object list and create object with relations"""

	added_by=DefaultMyUserSerializer(many=False, read_only=True)
	skill=DefaultSkillSerializer(many=True)

	added_by_id=serializers.PrimaryKeyRelatedField(write_only=True, 
		queryset=MyUser.objects.all(), source='added_by')

	class Meta:
		model = Event
		fields = ['id', 'title', 'description', 'place', 'date_added', 'event_date', 
			'event_link', 'added_by', 'added_by_id', 'skill']
		read_only_fields=['added_by',]
		write_only_fields=['added_by_id',]

#Skill Serializers
class SkillSerializer(serializers.ModelSerializer):
	"""SKILL object list and create object with relations"""

	events=DefaultEventSerializer(many=True)
	my_users=DefaultMyUserSerializer(many=True)

	class Meta:
		model=Skill
		fields=['id', 'skill', 'events', 'my_users']

#Batch Serializers
class BatchSerializer(serializers.ModelSerializer):
	"""BATCH object list and create object with relations"""

	my_users = DefaultMyUserSerializer(many=True)

	class Meta:
		model=Batch
		fields=['id', 'batch', 'my_users']

#File Serializer
class FileSerializer(serializers.ModelSerializer):
	"""FILE object list and create object with relations"""

	added_by=DefaultMyUserSerializer(many=False)
	skill=DefaultSkillSerializer(many=True)

	class Meta:
		model=File
		fields=['id', 'title', 'description', 'file_link', 'date', 'added_by', 'skill']