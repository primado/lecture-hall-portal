from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.utils import timezone
from datetime import datetime, timedelta

from department.models import Department
from courses.models import Course
from courseRep.models import BookLectureHall, ClassRooms

from courses.forms import CourseForm
from courseRep.forms import BookHallForm


 

# Create your views here.
def loginPage(request):
    page = 'login'
    
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')
        
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist, try again.')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('classRooms')
        else:
            messages.error(request, 'Username or password does not exist.')
        
    context = {'page': page}
    return render(request, 'courseRep/register_student.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')        
        
def registerPage(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
           messages.error(request, 'An error occured during registration.') 
    
    context = {
        'form': form,
    }
    return render(request, 'courseRep/register_student.html', context)

def departmentHome(request):
    departments = Department.objects.all()
    context = {
        'departments': departments,
    }
    return render(request, 'department/department_list.html', context)


def courseHome(request):
    courses = Course.objects.all()
    context = {'courses': courses}
    return render(request, 'courses/course_list.html', context)

def createCourse(request):
    courses = Course.objects.all()
    form = CourseForm()
    
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {
        'courses': courses,
        'form': form,
    }
    return render(request, 'courses/add_course.html', context)
            
    
def updateCourse(request, pk):
    courses = Course.objects.get(id=pk)
    form = CourseForm(instance=courses)
    if request.method == 'POST':
        form = CourseForm(request.POST, instance=courses)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {
        'courses': courses,
        'form': form,
    }
    return render(request, 'courses/add_course.html', context)


def deleteCourse(request, pk):
    courses = Course.objects.get(id=pk)
    if request.method == 'POST':
        courses.delete()
        return redirect('home')
    context = {'courses': courses}
    return render(request, 'courses/courses_delete.html', context)    
    

def bookHall(request):
    books = BookLectureHall.objects.all()
    form = BookHallForm()
    
    if request.method == 'POST':
        form = BookHallForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('classRooms')
    context = {
        'books': books,
        'form': form,
    }
    return render(request, 'courseRep/bookHall.html', context)


def updateBookHall(request, pk):
    lecture = BookLectureHall.objects.get(id=pk)
    
    form = BookHallForm(instance=lecture)
    if request.method == 'POST':
        form = BookHallForm(request.POST, instance=lecture)
        if form.is_valid():
            form.save() 
            return redirect('classRooms') 
        
    context = {
        'books': lecture, 
        'form': form,
    }
    return render(request, 'courseRep/bookHall.html', context)


def classRooms(request):
    # rooms = BookLectureHall.objects.all()
    rooms = BookHallForm.objects.filter(created_at__lte=datetime.now() - timedelta(seconds=60*60*24))   # booking period is 24hrs ( 1st 60 in minutes, 2nd 60 in hrs, 24 is 24hrs)
    roomCount = rooms.filter(complete=True).count() 
    
    unstrike = timezone.now()
        
     
    context = {
        'rooms': rooms,
        'roomCount': roomCount,
        'unstrike': unstrike,
    }

    return render(request, 'courseRep/lecture_halls_list.html', context)

def classRoomsList(request):
    class_rooms = ClassRooms.objects.all() 
    context = {
        'class_rooms': class_rooms,
    }
    return render(request, 'courseRep/class_rooms_list.html', context)


def detailClassRoom(request, pk):
    students = BookLectureHall.objects.get(id=pk)
     
    context = {'students': students}
    
    return render(request, 'courseRep/student_booked.html', context)
    


