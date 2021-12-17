from django import urls
from django.urls import path

from courses import views

from department import views


urlpatterns = [
    path('', views.courseHome, name='home'),
    path('add-course', views.createCourse, name="add-course"),
    path('update-course/<str:pk>/', views.updateCourse, name="update-course"),
    path('delete-course/<str:pk>/', views.deleteCourse, name='delete-course'),
]
