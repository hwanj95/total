from django.conf import settings
from django.db import models
from django.utils import timezone

class First(models.Model):
    title = models.CharField(max_length=100)

