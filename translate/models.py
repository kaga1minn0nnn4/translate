from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.

class Sentence(models.Model):
    ja_str = models.TextField()
    en_str = models.TextField()
    en_count = models.BigIntegerField()
