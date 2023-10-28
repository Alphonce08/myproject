from django.db import models

class Members(models.Model):
    username = models.CharField(max_length=30, blank=True, null=True)
    phonenumber = models.CharField(max_length=30, blank=True, null=True)
    email = models.CharField(max_length=30, blank=True, null=True)
    password = models.CharField(max_length=30, blank=True, null=True)
    
    
    def __str__(self):
        return self.name
    