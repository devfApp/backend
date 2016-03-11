from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class MyUser(models.Model):

    class Meta:
        verbose_name = "MyUser"
        verbose_name_plural = "MyUsers"

    #Relations

    #Attributes

    def __str__(self):
        pass
    