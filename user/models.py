from django.core import validators
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.core.validators import RegexValidator
    
# Create your models here.

USER_TYPE = [('alumni' ,'alumni'),('sensei', 'sensei'), ('admin', 'admin')]

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
    

class MyUser(AbstractBaseUser, PermissionsMixin):

    class Meta:
        verbose_name = "MyUser"
        verbose_name_plural = "MyUser"

    #Relations
    # user = models.OneToOneField(User, related_name='user')
    batch = models.ManyToManyField(Batch, related_name='my_users')
    cinta = models.ManyToManyField(Cinta, related_name='my_users')
    skill = models.ManyToManyField(Skill, blank=True, related_name='my_users')

    #USER ATTRIBUTES
    username = models.CharField(
        'username',
        max_length=30,
        unique=True,
        help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.',
        validators=[
            validators.RegexValidator(
                r'^[\w.@+-]+$',
                ('Enter a valid username. This value may contain only '
                  'letters, numbers ' 'and @/./+/-/_ characters.')
            ),
        ],
        error_messages={
            'unique': "A user with that username already exists.",
        },
    )
    first_name = models.CharField('first name', max_length=30, blank=True)
    last_name = models.CharField('last name', max_length=30, blank=True)
    email = models.EmailField('email address', blank=True)
    profile_pic = models.ImageField(upload_to='/profile_pic', blank=True)
    is_staff = models.BooleanField(
        'staff status',
        default=False,
        help_text='Designates whether the user can log into this admin site.',
    )
    is_active = models.BooleanField(
        'active',
        default=True,
        help_text='Designates whether this user should be treated as active. ' 'Unselect this instead of deleting accounts.',
    )

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', ]
    date_added = models.DateTimeField(auto_now_add=True)

    #Attributes
    is_validated = models.BooleanField(blank=True, default=False)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{10,15}$', message="Phone number must be entered in the format: '55-5555-5555'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], blank=True, max_length=13) # validators should be a list
    job = models.CharField(max_length=50, blank=True)
    description = models.TextField(blank=True, max_length=140)
    user_type = models.CharField(blank=True ,max_length=50, choices=USER_TYPE)

    def __str__(self):
        return self.username


    def get_full_name(self):
        pass


    def get_short_name(self):
        pass
