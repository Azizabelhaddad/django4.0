from distutils.command.upload import upload
from django.db import models

from django.contrib.auth.models import User

from uuid import uuid4

# Create your models here.


class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    name = models.TextField(max_length=30, null=True)
    email = models.EmailField(max_length=100, null=True)
    description = models.TextField(max_length=50, null=True , blank=True)
    image = models.ImageField(null= True, upload_to = 'profile/')
    url = models.URLField(null=True, blank=True)
    id = models.UUIDField(primary_key=True, unique=True, default=uuid4, editable=False )

    def __str__(self):
        return f"{self.user.username}"
