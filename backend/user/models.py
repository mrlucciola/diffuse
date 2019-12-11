# djongo
from djongo import models

# django imports
from django.contrib.auth.models import AbstractUser

class UserManager(models.Manager):
    def get_by_natural_key(self, username):
        return self.get(username=username)
# start user class
class CustomUser(AbstractUser):
    objects = UserManager()
    
    # default fields are username, password, email, firstname, lastname
    # username and password are not optional
    dob = models.DateField(name='dob', blank=True, null=True)
    phone = models.CharField(max_length=15, name='phone', blank=True, null=True)
    profile_picture = models.ImageField(verbose_name='profile_picture', name='profile_picture', width_field=300, null=True, blank=True)

    def natural_key(self):
        return self.username
    def __str__(self):
        return f'{self.username}'