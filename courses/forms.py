from typing import Coroutine
from django.forms import ModelForm

from .models import Course


class CourseForm(ModelForm):
    
    class Meta:
        model = Course
        fields = ['name', 'code',]