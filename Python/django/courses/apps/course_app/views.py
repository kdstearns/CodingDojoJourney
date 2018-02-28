from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from models import *

def index(request):
	context = {
		'all': Course.objects.all()
	}
	return render(request, 'course_app/courses.html', context)

def destroy(request, num):
	context = {
		'delete': Course.objects.get(id = num)
	}
	return render(request, 'course_app/coursesAlert.html', context)

def add(request):
	errors = Course.objects.basic_validator(request.POST)
	if len(errors):
		for tag, error in errors.iteritems():
			messages.error(request, error, extra_tags = tag)
		return redirect('/')
	else:
		Course.objects.create(courseName = request.POST['courseName'], desc = request.POST['desc'])
		return redirect('/')

def remove(request, num):	
	removeCourse = Course.objects.get(id = num)
	removeCourse.delete()
	return redirect('/')