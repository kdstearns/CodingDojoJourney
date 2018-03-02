from __future__ import unicode_literals
from django.db import models
import bcrypt
import datetime
from time import time, strftime
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile(r'^[a-zA-Z ]+$')

class UserManager(models.Manager):
	def basic_validator(self, postData):
		errors = {}

		if len(postData['name']) < 1 or len(postData['email']) < 1 or len(postData['password']) < 1 or len(postData['confirm']) < 1 or len(postData['birthday']) < 1 :
			errors['blank'] = "All fields must be completed."

		if not NAME_REGEX.match(postData['name']):
			errors['name'] = "Your name cannot contain numbers."

		if not EMAIL_REGEX.match(postData['email']):
			errors['address'] = "Please enter a valid e-mail address!"

		emailVal = User.objects.filter(email = postData['email'])
		if len(emailVal) != 0:
			errors['userEmail'] = "Your email is already in our database, please login."

		if len(postData['password']) < 8:
			errors['length'] = "Your password must be at least 8 characters."

		if postData['confirm'] != postData['password']:
			errors['match'] = "Your passwords must match."

		return errors

	def login_validator(self, postData):
		match = {}
		user = User.objects.filter(email = postData['email'])
		# print user
		# print user[0].password
		if len(user) == 0:
			match['username'] = "This username does not exist, please register."
			return match

		if not bcrypt.checkpw(postData['password'].encode(), user[0].password.encode()):
			match['pw'] = "Login invalid."
			return match

class AppointmentManager(models.Manager):
	def appt_validator(self, postData):
		appt = {}

		if len(postData['task']) < 1 or len(postData['date']) < 1 or len(postData['time']) < 1:
			appt['blank'] = "All fields must be completed."

		todayDate = datetime.datetime.today().strftime('%Y-%m-%d')
		# print todayDate
		# print inputDate
		if postData['date'] < todayDate:
			appt['date'] = "Your appointment date cannot be prior to today."

		return appt

class User(models.Model):
	name = models.CharField(max_length = 255)
	email = models.CharField(max_length = 255)
	password = models.CharField(max_length = 255)
	birthday = models.DateField()
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	objects = UserManager()

class Appointment(models.Model):
	date = models.DateField()
	time = models.TimeField()
	task = models.CharField(max_length = 255)
	status = models.CharField(max_length = 255, default = "Pending")
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	user = models.ForeignKey(User, related_name = "appointments")
	objects = AppointmentManager()