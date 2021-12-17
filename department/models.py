from django.db import models

# Create your models here.

class Department(models.Model):
    name = models.CharField(max_length=60)
    hod = models.CharField(max_length=60, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.name
    