from django.db import models

class Members(models.Model):
    username = models.CharField(max_length=30)
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    
    
    def __str__(self):
        return self.name
    