from django.db import models
from user.models import *

# Create your models here.
class File(models.Model):

    class Meta:
        verbose_name = "File"
        verbose_name_plural = "Files"

    #Relations
    added_by = models.ForeignKey(MyUser, related_name='shared_files')
    skill = models.ManyToManyField(Skill, related_name='shared_files')

    #Attributes
    title = models.CharField(max_length=50, blank=False)
    description = models.TextField(max_length=400, blank=True)
    file_link = models.URLField(blank=False)
    date = models.DateField(auto_now_add=True)



    def __str__(self):
    	return (self.title)
       
    