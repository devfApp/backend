from django.db import models
from user.models import *

# Create your models here.

class Challenge(models.Model):

    class Meta:
        verbose_name = "Challenge"
        verbose_name_plural = "Challenges"

    #Relations
    sensei = models.ForeignKey(MyUser, related_name='sensei')
    batch = models.ForeignKey(Batch)
    # completed_user = models.ManyToManyField(MyUser, related_name='users')

    #Attributes
    title = models.CharField(max_length=20, blank=False)
    description = models.TextField(max_length=140, blank=True)
    demo_link = models.URLField(blank=True)

    def __str__(self):
        return self.title
    
class Answer(models.Model):

    class Meta:
        verbose_name = "Answer"
        verbose_name_plural = "Answers"
    #Relations
    user=models.ForeignKey(MyUser)
    challenge=models.ForeignKey(Challenge, related_name='answers')

    #Attributes
    file_link=models.URLField(blank=False)
    date_added=models.DateField(auto_now_add=True)

    def __str__(self):
        return 'Answer ' + self.challenge.title
        
