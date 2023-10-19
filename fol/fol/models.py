from django.db import models
from django.contrib.auth.models import User


class TimeStamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    
    class Meta:
        abstract = True
       
       
class Register(models.Model):
    username = models.CharField(max_length=15, blank=True, null=True)
    email = models.CharField(max_length=30, blank=True, null=True)
    number = models.IntegerField(max_length=10, blank=True, null=True)
    
    class Meta:
        abstract = True