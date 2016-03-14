from django.db import models
from user.models import *

# Create your models here.
class Event(models.Model):

    class Meta:
        verbose_name = "Event"
        verbose_name_plural = "Events"

    #Relations
    added_by = models.ForeignKey(MyUser, blank=False)
    skill = models.ManyToManyField(Skill, blank=True, related_name='skills')

    #Attributes
    title = models.CharField(max_length=20, blank=False)
    description = models.TextField(max_length=140, blank=False)
    place = models.CharField(max_length=50)
    date_added = models.DateField(auto_now_add=True, blank=False)
    event_date = models.DateTimeField(blank=False)
    event_link = models.URLField(blank=False)

    def __str__(self):
    	return self.title
    