from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from user.models import MyUser

# Create your models here.
class Notification(models.Model):

    class Meta:
        verbose_name = "Notification"
        verbose_name_plural = "Notifications"

    title = models.CharField(max_length=256)
    message = models.TextField()
    viewed = models.BooleanField(default=False)
    my_user = models.ForeignKey(MyUser)

    def __str__(self):
    	return self.title
        
@receiver(post_save, sender=MyUser)
def create_welcome_message(sender, **kwargs):
	if kwargs.get('created', False):
		Notification.objects.create(user=kwargs.get('instance'),
									title='Welcome to our django site',
									message='Thanks for signing up!')
    