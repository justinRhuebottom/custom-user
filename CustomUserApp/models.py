from django.db import models
from django.contrib.auth.models import AbstractUser

class MyUser(AbstractUser):
    display_name = models.CharField(max_length=20, blank=True, null=True)
    homepage = models.URLField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    
    REQUIRED_FIELDS = ['age']

    def __str__(self):
        return self.username