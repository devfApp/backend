# -*- encoding: utf-8 -*-
import django_filters
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
	FILTERS --> added_by_id, event_date
	SEARCH --> title, place, event_date, skill__skill
	DEFAULT ORDER --> Descending event_date
	"""

	queryset = Event.objects.all()
	serializer_class = EventSerializer
	#Filter
	filter_backends=[filters.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
	filter_fields=['added_by_id', 'event_date']
	search_fields=['title', 'place', 'event_date', 'skill__skill']
	ordering=['-event_date']

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

#MyUser Views
class MyUserView(generics.ListCreateAPIView):
	"""
	MYUSER object list and create object
	"""

	queryset = User.objects.all()
	serializer_class = MyUserSerializer

class MyUserDetailView(generics.RetrieveUpdateDestroyAPIView):
	"""
	MYUSER object view and edit
	"""

	queryset = User.objects.all()
	serializer_class = MyUserSerializer

#User views
class UserRegisterView(generics.CreateAPIView):
	"""
	USER object list and create object
	"""

	queryset=User.objects.all()
	serializer_class=UserRegisterSerializer
	permission_classes = [permissions.AllowAny]

# File views
class FileView(generics.ListCreateAPIView):
	"""
	FILE object list and create object
	FILTERS --> title, added_by_id, date
	SEARCH --> added_by__username, date, skill__skill
	DEFAULT ORDER --> Descending date
	"""

	# def get_queryset(self):
	# 	"""
	# 	This view should return only the user login.
	# 	"""
	# 	user = self.request.user
	# 	return File.objects.filter(id=user.id)
	queryset=File.objects.all()
	serializer_class=FileSerializer
	#Filters
	filter_backends=(filters.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
	filter_fields=['title', 'added_by_id', 'date']
	search_fields=['title', 'added_by__username', 'date', 'skill__skill']
	ordering=['-date']

class FileDetailView(generics.RetrieveUpdateDestroyAPIView):
	"""
	FILE object view and edit
	"""

	queryset=File.objects.all()
	serializer_class=FileSerializer

# class FileDetailView(APIView):
# 	def get_object(self, pk):
# 		try:
# 			return File.objects.get(pk=pk)
# 		except File.DoesNotExist:
# 			raise Http404


# 	def get(self, request, pk, format=None):
# 		file = self.get_object(pk)
# 		serializer = FileSerializer(file, many=False)
# 		return Response(serializer.data, status.HTTP_200_OK)

# 	def put(self, request, pk):
# 		file = self.get_object(pk)
# 		serializer=FileSerializer(file, data=request.data)
# 		if serializer.is_valid():
# 			serializer.save()
# 			return Response(serializer.data)
# 		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#Challenge views
class ChallengeView(generics.ListCreateAPIView):
	"""
	CHALLENGE object list and create object
	FILTERS --> sensei_id, title, batch_id
	SEARCH --> title, date
	DEFAULT ORDER --> Descending date
	"""

	queryset=Challenge.objects.all()
	serializer_class=ChallengeSerializer
	#Filters
	filter_backends=[filters.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
	filter_fields=['sensei_id', 'title', 'batch_id']
	search_fields=['title', 'date', ]
	ordering=['-date']	

class ChallengeDetailView(generics.RetrieveUpdateDestroyAPIView):
	"""
	CHALLENGE object view and edit
	"""

	queryset=Challenge.objects.all()
	serializer_class=ChallengeSerializer

#Answer views
class AnswerView(generics.ListCreateAPIView):
	"""
	ANSWER object list and create object
	FILTERS --> user_id, challenge_id
	SEARCH --> date_added, user__username
	DEFAULT ORDER --> Descending date_added
	"""

	queryset=Answer.objects.all()
	serializer_class=AnswerSerializer
	#Filters
	filter_backends=[filters.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
	filter_fields=['user_id', 'challenge_id']
	search_fields=['date_added', 'user__username']
	ordering=['-date_added']

class AnswerDetailView(generics.RetrieveUpdateDestroyAPIView):
	"""
	ANSWER object view and edit
	"""

	queryset=Answer.objects.all()
	serializer_class=AnswerSerializer

class CintaView(generics.ListCreateAPIView):
	"""
	CINTA object list and create object
	"""

	queryset=Belt.objects.all()
	serializer_class=CintaSerializer

class CintaDetailView(generics.RetrieveUpdateDestroyAPIView):
	"""
	CINTA object view and edit
	"""

	queryset=Belt.objects.all()
	serializer_class=CintaSerializer