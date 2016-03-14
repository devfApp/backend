# -*- encoding:utf-8 -*-
from rest_framework import serializers
from user.models import *
from community_event.models import *

#Default Serializers
class DefaultEventSerializer(serializers.ModelSerializer):
	class Meta:
		model = Event
		fields = ['id', 'title', 'description', 'place', 'date_added', 'event_date', 'event_link',]