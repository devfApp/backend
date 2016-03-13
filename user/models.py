from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

# Create your models here.
class MyUser(models.Model):

    class Meta:
        verbose_name = "MyUser"
        verbose_name_plural = "MyUser"

    #Relations
    user = models.OneToOneField(User, related_name='user')

    #Attributes
    date_added = models.DateTimeField(auto_now_add=True)
    profile_pic = models.ImageField(upload_to='profile_pic/', blank=True)
    is_validated = models.BooleanField(blank=True, default=False)
    description = models.TextField(blank=True, max_length=140)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{10,15}$', message="Phone number must be entered in the format: '55-5555-5555'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], blank=True, max_length=13) # validators should be a list

    def __str__(self):
    	return (self.user.username)
    