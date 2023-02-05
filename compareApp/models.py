from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    homeLong = models.FloatField()
    homeLat = models.FloatField()
    profilePicture = models.ImageField(upload_to='profile_pics/', blank=True)

