# -*- encoding: utf-8 -*-
# import django_filters
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, status, filters, permissions
from django.http import Http404
from .serializers import *

# Create your views here.
class EventView(generics.ListCreateAPIView):
	queryset = Event.objects.all()
	serializer_class = DefaultEventSerializer