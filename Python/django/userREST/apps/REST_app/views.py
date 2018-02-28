from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from models import *

def main(request):
	response = "Hello! Please head over to localhost:8000/users to see the fun things you can do with users!"
	return HttpResponse(response)

def index(request):
	all_users = User.objects.all()
	context = {
		'all': all_users
	}
	return render(request, 'REST_app/usersRest.html', context)

def new(request):
	return render(request, 'REST_app/usersAdd.html')

def edit(request, num):
	editUser = User.objects.get(id = num)
	context = {
		'edit': editUser
	}
	return render(request, 'REST_app/usersEdit.html', context)

def show(request, num):
	showUser = User.objects.get(id = num)
	context = {
		'show': showUser
	}
	return render(request, 'REST_app/usersShow.html', context)

def create(request):
	errors = User.objects.basic_validator(request.POST)
	if len(errors):
		for tag, error in errors.iteritems():
			messages.error(request, error, extra_tags = tag)
		return redirect('/users/new')
	else:
		newUser = User.objects.create(first_name = request.POST['first'], last_name = request.POST['last'], email = request.POST['email'])
		return redirect('/users')

def update(request, num):
	if request.method == 'POST':
		errors = User.objects.basic_validator(request.POST)
		if len(errors):
			for tag, error in errors.iteritems():
				messages.error(request, error, extra_tags = tag)
			return redirect('/users/'+str(num)+'/edit')

		else:
			# print num
			updateUser = User.objects.get(id = num)
			updateUser.first_name = request.POST['first']
			updateUser.last_name = request.POST['last']
			updateUser.email = request.POST['email']
			# print request.POST['first']
			# print request.POST['last']
			# print request.POST['email']
			updateUser.save()
			return redirect('/users')

def destroy(request, num):
	deleteUser = User.objects.get(id = num)
	deleteUser.delete()
	return redirect('/users')
