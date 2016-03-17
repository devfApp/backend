# -*- encoding: utf-8 -*-
import django_filters
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, status, filters, permissions
from django.http import Http404
from .serializers import *
from django.contrib.auth.models import User

# Create your views here.

def get_current_user():
	current_user = getattr(_thread_locals, USER_ATTR_NAME, None)

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

#MyUser Views
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

# File views
class FileView(generics.ListCreateAPIView):
	"""
	FILE object list and create object
	"""

	# def get_queryset(self):
	# 	"""
	# 	This view should return only the user login.
	# 	"""
	# 	user = self.request.user
	# 	return File.objects.filter(id=user.id)

	queryset=File.objects.all()
	serializer_class=FileSerializer
	filter_backends=(filters.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
	filter_fields=['title', 'added_by_id', 'date']
	search_fields=['title', 'added_by__user__username', 'date', 'skill__skill']
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
	queryset=Challenge.objects.all()
	serializer_class=ChallengeSerializer

class ChallengeDetailView(generics.RetrieveUpdateDestroyAPIView):
	queryset=Challenge.objects.all()
	serializer_class=ChallengeSerializer

#Answer views
class AnswerView(generics.ListCreateAPIView):
	queryset=Answer.objects.all()
	serializer_class=AnswerSerializer