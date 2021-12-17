from django.db import models

from department.models import Department
# Create your models here.

class Course(models.Model):
    name = models.CharField('Couses Name', max_length=200)
    code = models.CharField('Course Code', max_length=10, null=True, blank=True)
    # department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return self.name