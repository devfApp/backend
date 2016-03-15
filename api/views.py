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
	queryset = Event.objects.all()
	serializer_class = EventSerializer

class EventDetailView(generics.RetrieveUpdateDestroyAPIView):
	queryset = Event.objects.all()
	serializer_class = EventSerializer

#Batch Views
class BatchView(generics.ListCreateAPIView):
	queryset=Batch.objects.all()
	serializer_class=BatchSerializer

#Skill Views
class SkillView(generics.ListCreateAPIView):
	queryset=Skill.objects.all()
	serializer_class=SkillSerializer

class SkillDetailView(generics.RetrieveUpdateDestroyAPIView):
	queryset=Skill.objects.all()
	serializer_class=SkillSerializer

#MyUse Views
class MyUserView(generics.ListCreateAPIView):
	queryset = MyUser.objects.all()
	serializer_class = MyUserSerializer

class MyUserDetailView(generics.RetrieveUpdateDestroyAPIView):
	queryset = MyUser.objects.all()
	serializer_class = MyUserSerializer
