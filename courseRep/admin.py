from django.contrib import admin

from .models import BookLectureHall, ClassRooms

# Register your models here.

@admin.register(BookLectureHall)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "student_id", "class_rooms",)
    search_fields = ("first_name__icontains", "last_name__icontains")

@admin.register(ClassRooms)
class classRoomsAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name__icontains",)



