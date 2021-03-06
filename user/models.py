from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
    
# Create your models here.
class Cinta(models.Model):

    class Meta:
        verbose_name = "Cinta"
        verbose_name_plural = "Cintas"

    #Relations

    #Attributes
    is_active=models.BooleanField(blank=False)
    name=models.CharField(max_length=50, blank=False)

    def __str__(self):
        return self.name
    

class Skill(models.Model):

    class Meta:
        verbose_name = "Skill"
        verbose_name_plural = "Skills"

    #Attributes
    skill = models.CharField(max_length=20)

    def __str__(self):
    	return self.skill
    
class Batch(models.Model):

    class Meta:
        verbose_name = "Batch"
        verbose_name_plural = "Batchs"

    #Attributes
    batch = models.CharField(max_length=10)

    def __str__(self):
    	return self.batch
    

class MyUser(User):

    class Meta:
        verbose_name = "MyUser"
        verbose_name_plural = "MyUser"

    #Relations
    # user = models.OneToOneField(User, related_name='user')
    batch = models.ManyToManyField(Batch, related_name='my_users')
    cinta = models.ManyToManyField(Cinta, related_name='my_users')
    skill = models.ManyToManyField(Skill, blank=True, related_name='my_users')

    #Attributes
    date_added = models.DateTimeField(auto_now_add=True)
    profile_pic = models.ImageField(upload_to='profile_pic/', blank=True)
    is_validated = models.BooleanField(blank=True, default=False)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{10,15}$', message="Phone number must be entered in the format: '55-5555-5555'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], blank=True, max_length=13) # validators should be a list
    job = models.CharField(max_length=50, blank=True)
    description = models.TextField(blank=True, max_length=140)
    user_type = models.CharField(max_length=50, choices=[('alumni' ,'alumni'),('sensei', 'sensei'), ('admin', 'admin')])

    def __str__(self):
    	return (self.username)
