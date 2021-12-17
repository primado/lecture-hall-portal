from django.db import models
from django.contrib.auth.models import User

from department.models import Department
from courses.models import Course
# Create your models here.


class ClassRooms(models.Model):
    name = models.CharField("Lecture Hall Name", max_length=20)
    
    def __str__(self):
        return self.name


class BookLectureHall(models.Model):
    Male = 'Male'
    Female = 'Female'
    GENDER = [
        (Male, 'Male'),
        (Female, 'Female')
    ]
    
    first_name = models.CharField('First Name', max_length=60)
    last_name = models.CharField('Last Name', max_length=60, blank=True, null=True)
    student_id = models.CharField('Student ID', max_length=15, blank=True, null=True)
    level = models.CharField('Level', max_length=5, blank=True, null=True)
    gender = models.CharField(max_length=10, choices=GENDER)
    created_at = models.DateTimeField(auto_now=True)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    class_rooms = models.ForeignKey( ClassRooms, verbose_name="Lecture Halls", on_delete=models.SET_NULL, null=True)
    complete = models.BooleanField("Confirm", default=False) 
    
    
    class Meta:
        ordering = ['-created_at']
        
    def __str__(self):
        return f"{self.first_name}, {self.last_name}"
    


    














