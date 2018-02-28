from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from models import *
import bcrypt
import datetime
from time import time, strftime
today = datetime.datetime.today().strftime('%m-%d-%Y')

def index(request):
	return render(request, 'appt_app/loginReg.html')

def success(request):
	# print today
	showUser = User.objects.get(id = request.session['id'])
	userAppts = showUser.appointments.all().order_by('date')
	context = {
		'show': showUser,
		'appt': userAppts
	}
	return render(request, 'appt_app/dashboard.html', context)

def edit(request, id):
	showAppt = Appointment.objects.get(id = id)
	# userAppts = showAppt.appointments.all()
	context = {
		'edit': showAppt,
		# 'appt': userAppts
	}
	return render(request, 'appt_app/update.html', context)

def register(request):
	if request.method == 'POST':
		errors = User.objects.basic_validator(request.POST)
		if len(errors):
			for tag, error in errors.iteritems():
				messages.error(request, error, extra_tags = tag)
			return redirect('/')
		else:
			hash1 = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
			# print hash1
			# print request.POST['name']
			# print request.POST['email']
			# print request.POST['birthday']
			user = User.objects.create(name = request.POST['name'], email = request.POST['email'], password = hash1, birthday = request.POST['birthday'])
			# print user.id
			request.session['id'] = user.id
			return redirect('/success')

def login(request):
	if request.method == 'POST':
		match = User.objects.login_validator(request.POST)
		# print match
		if len(match):
			for tag, error in match.iteritems():
				messages.error(request, error, extra_tags = tag)
			return redirect('/')
		else:
			user = User.objects.get(email = request.POST['email'])
			# print user
			request.session['id'] = user.id
			# keeps user logged in
			# print user
			return redirect('/success')

def appt(request):
	if request.method == 'POST':
		appt = Appointment.objects.appt_validator(request.POST)
		if len(appt):
			for tag, error in appt.iteritems():
				messages.error(request, error, extra_tags = tag)
			return redirect('/success')
		currentUser = User.objects.get(id = request.session['id'])
		allAppts = currentUser.appointments.all()
		# print allAppts
		for element in allAppts:
			if request.POST['time'] and request.POST['date']:
				appt['dup'] = "You already have an appointment for that time."
				if len(appt):
					for tag, error in appt.iteritems():
						messages.error(request, error, extra_tags = tag)
				return redirect('/success')
		else:
			# print request.session
			userAppt = User.objects.get(id = request.session['id'])
			appointment = Appointment.objects.create(user = userAppt, task = request.POST['task'], date = request.POST['date'], time = request.POST['time'])
			request.session['appt_id'] = appointment.id
			return redirect('/success')

def update(request, id):
	if request.method == 'POST':
		appt = Appointment.objects.appt_validator(request.POST)
		if len(appt):
			for tag, error in appt.iteritems():
				messages.error(request, error, extra_tags = tag)
			return redirect('/success')
		currentUser = User.objects.get(id = request.session['id'])
		allAppts = currentUser.appointments.all()
		# print allAppts
		for element in allAppts:
			if request.POST['time'] and request.POST['date']:
				appt['dup'] = "You already have an appointment for that time."
				if len(appt):
					for tag, error in appt.iteritems():
						messages.error(request, error, extra_tags = tag)
				return redirect('/edit/'+str(id))
		else:
			updateAppt = Appointment.objects.get(id = id)
			# print updateAppt
			updateAppt.task = request.POST['task']
			updateAppt.status = request.POST['status']
			updateAppt.date = request.POST['date']
			updateAppt.time = request.POST['time']
			updateAppt.save()
			return redirect('/success')


def delete(request, id):
	removeAppt = Appointment.objects.get(id = id)
	# print removeAppt
	removeAppt.delete()
	return redirect('/success')

def logout(request):
	request.session.pop('id')
	return redirect('/')
