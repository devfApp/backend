# -*- encoding: utf-8 -*-
# import django_filters
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, status, filters, permissions
from django.http import Http404
from .serializers import *

# Create your views here.
#Event Views
class EventView(generics.ListCreateAPIView):
	"""
	EVENT object list and create object
	"""

	queryset = Event.objects.all()
	serializer_class = EventSerializer

class EventDetailView(generics.RetrieveUpdateDestroyAPIView):
	"""
	EVENT object view and edit
	"""

	queryset = Event.objects.all()
	serializer_class = EventSerializer

#Batch Views
class BatchView(generics.ListCreateAPIView):
	"""
	BATCH object list and create object
	"""

	queryset=Batch.objects.all()
	serializer_class=BatchSerializer

class BatchDetailView(generics.RetrieveUpdateDestroyAPIView):
	"""
	BATCH object view and edit
	"""

	queryset=Batch.objects.all()
	serializer_class=BatchSerializer

#Skill Views
class SkillView(generics.ListCreateAPIView):
	"""
	SKILL object list and create object
	"""

	queryset=Skill.objects.all()
	serializer_class=SkillSerializer

class SkillDetailView(generics.RetrieveUpdateDestroyAPIView):
	"""
	SKILL object view and edit
	"""

	queryset=Skill.objects.all()
	serializer_class=SkillSerializer

#MyUse Views
class MyUserView(generics.ListCreateAPIView):
	"""
	MYUSER object list and create object
	"""

	queryset = MyUser.objects.all()
	serializer_class = MyUserSerializer

class MyUserDetailView(generics.RetrieveUpdateDestroyAPIView):
	"""
	MYUSER object view and edit
	"""

	queryset = MyUser.objects.all()
	serializer_class = MyUserSerializer
