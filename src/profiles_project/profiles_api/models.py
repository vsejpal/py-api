from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin

# Create your models here.

class UserProfile(AbstractBaseUser, PermissionsMixin):
    """"Represents a 'user profile' in our system"""

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']


    def get_full_name(self):
        """"Used to get a user's full name"""

        return self.name

    def get_short_name(self):
        """"Used to get user's short name"""

        return self.name

    def str(self):
        """" so django knows how to print an object of this class"""

        return self.email
