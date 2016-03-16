from django.db import models
from user.models import *

# Create your models here.
class Challenge(models.Model):

    class Meta:
        verbose_name = "Challenge"
        verbose_name_plural = "Challenges"

    #Relations
    sensei = models.ForeignKey(MyUser)
    batch = models.ForeignKey(Batch)

    #Attributes
    title = models.CharField(max_length=20, blank=False)
    description = models.TextField(max_length=140, blank=True)
    demo_link = models.URLField(blank=True)
    # completed_user = models.ManyToManyField(MyUser)

    def __str__(self):
        return self.title
    