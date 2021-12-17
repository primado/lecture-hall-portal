from django.contrib.auth import logout
from django.urls import path

from department import views


urlpatterns = [
    path('', views.loginPage, name="login"),
    path('lecture-halls-list/', views.classRooms, name="classRooms"),
    path('all-lecture-list/', views.classRoomsList, name="allClassList"),
    path('student-info/<str:pk>/', views.detailClassRoom, name="student-info"),
    
    
    path('logout/', views.logoutUser, name="logout"),
    path('bookhall/', views.bookHall, name="bookHall"),
    path('updatehall/<str:pk>/', views.updateBookHall, name="updateHall"),
    path('register/', views.registerPage, name="register-student"),
    
]


