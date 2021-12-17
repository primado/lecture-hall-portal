from django.contrib import admin

from .models import *
# Register your models here.


@admin.register(Department)
class Department(admin.ModelAdmin):
    list_display = ("name", "description")
