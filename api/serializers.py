# -*- encoding:utf-8 -*-
from rest_framework import serializers
from django.contrib.auth.models import User
from user.models import *
from community_event.models import *
from user.models import *
from shared_files.models import *
from sensei_stuff.models import *

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

	class Meta:
		model = MyUser
		fields = ['id', 'username', 'first_name', 'last_name', 'email', 'date_added', 
		'profile_pic', 'is_validated', 'phone_number', 'job', 'description', 'user_type']

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

class DefaultChallengeSerializer(serializers.ModelSerializer):
	class Meta:
		model=Challenge
		fields=['id', 'title', 'description', 'demo_link', 'date']

class DefaultAnswerSerializer(serializers.ModelSerializer):
	class Meta:
		model=Answer
		fields=['id', 'file_link']

class DefaultCintaSerializer(serializers.ModelSerializer):
	class Meta:
		model=Cinta
		fields=['id', 'is_active', 'name']

"""
Aquí comienzan los seriealizers con ATRIBUTOS y RELACIONES
"""

class UserRegisterSerializer(serializers.ModelSerializer):
	class Meta:
		model = MyUser
		fields = ['id', 'username', 'first_name', 'last_name', 'email', 'password']
		write_only_fields=['password']

	def create(self, validate_data):
		my_user = MyUser.objects.create(
				username = validate_data['username'],
				email = validate_data['email'],
				first_name = validate_data['first_name'],
				last_name = validate_data['last_name'])
		my_user.set_password(validate_data['password'])
		my_user.save()
		return my_user


#MyUser Serializer
class MyUserSerializer(serializers.ModelSerializer):
	"""MYUSER object list and create object with relations"""

	skill=DefaultSkillSerializer(many=True)
	batch=DefaultBatchSerializer(many=True)
	cinta=DefaultCintaSerializer(many=True)

	class Meta:
		model=MyUser
		fields = ['id', 'username', 'first_name', 'last_name', 'email', 'date_added', 
		'profile_pic', 'is_validated','phone_number', 'job', 'description', 'skill', 
		'batch', 'cinta', 'user_type']

#Event Serializer
class EventSerializer(serializers.ModelSerializer):
	"""EVENT object list and create object with relations"""

	added_by=DefaultMyUserSerializer(many=False, read_only=True)
	skill=DefaultSkillSerializer(many=True, read_only=True)

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

	events=DefaultEventSerializer(many=True, read_only=True)
	my_users=DefaultMyUserSerializer(many=True, read_only=True)
	shared_files=DefaultFileSerializer(many=True, read_only=True)

	class Meta:
		model=Skill
		fields=['id', 'skill', 'events', 'my_users', 'shared_files']
		read_only_fields=['events', 'my_users']

#Batch Serializers
class BatchSerializer(serializers.ModelSerializer):
	"""BATCH object list and create object with relations"""

	my_users = DefaultMyUserSerializer(many=True, read_only=True)

	class Meta:
		model=Batch
		fields=['id', 'batch', 'my_users']
		read_only_fields=['my_users']

#File Serializer
class FileSerializer(serializers.ModelSerializer):
	"""FILE object list and create object with relations"""

	added_by=DefaultMyUserSerializer(many=False, read_only=True)
	skill=DefaultSkillSerializer(many=True, read_only=True)

	added_by_id=serializers.PrimaryKeyRelatedField(write_only=True, queryset=MyUser.objects.all(), 
		source='added_by')

	class Meta:
		model=File
		fields=['id', 'title', 'description', 'file_link', 'date', 'added_by', 'added_by_id',
			'skill']
		read_only_fields=['added_by']
		write_only_fields=['added_by_id']

#Answer Serializer
class AnswerSerializer(serializers.ModelSerializer):

	my_user = DefaultMyUserSerializer(many=False, read_only=True)
	challenge = DefaultChallengeSerializer(many=False, read_only=True)

	my_user_id=serializers.PrimaryKeyRelatedField(write_only=True, queryset=MyUser.objects.all(),
		source='user')
	challenge_id=serializers.PrimaryKeyRelatedField(write_only=True, 
		queryset=Challenge.objects.all(), source='challenge')

	class Meta:
		model=Answer
		fields=['id', 'file_link', 'date_added', 'my_user', 'my_user_id', 'challenge', 'challenge_id']
		read_only_fields=['my_user', 'challenge']
		write_only_fields=['my_user_id', 'challenge_id']

#Challenge Serializer
class ChallengeSerializer(serializers.ModelSerializer):
	sensei = DefaultMyUserSerializer(many=False, read_only=True)
	answers = DefaultAnswerSerializer(many=True, read_only=True)
	batch = DefaultBatchSerializer(many=False, read_only=True)

	sensei_id=serializers.PrimaryKeyRelatedField(write_only=True, queryset=MyUser.objects.all(), 
		source='sensei')
	batch_id=serializers.PrimaryKeyRelatedField(write_only=True, queryset=Batch.objects.all(),
		source='batch')

	class Meta:
		model=Challenge
		fields=['id', 'title', 'description', 'demo_link', 'date', 'sensei', 'sensei_id', 'batch', 
			'batch_id', 'answers']
		read_only_fields=['answers', 'sensei', 'batch']
		write_only_fields=['sensei_id', 'batch_id']

class CintaSerializer(serializers.ModelSerializer):
	my_users = DefaultMyUserSerializer(many=True, read_only=True)

	class Meta:
		model=Cinta
		fields=['id', 'is_active', 'name', 'my_users']

def jwt_response_payload_handler(token, my_user=None, request=None):
    return {
        'token': token,
        'my_user': DefaultUserSerializer(my_user).data
    }