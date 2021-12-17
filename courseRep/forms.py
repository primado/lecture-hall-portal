from django.db.models import fields
from django.forms import ModelForm

from .models import BookLectureHall


class BookHallForm(ModelForm):
    
    
    class Meta:
        model = BookLectureHall
        fields = '__all__'
        ordering = ['-created_at']







