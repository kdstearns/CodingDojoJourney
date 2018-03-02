from __future__ import unicode_literals
from django.db import models
import bcrypt
from datetime import date, datetime
from time import time
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

class QuoteManager(models.Manager):
	def quote_validator(self, postData):
		quote = {}

		if len(postData['quoted_by']) < 1 or len(postData['quote']) < 1:
			quote['blank'] = "All fields must be completed."
		
		if len(postData['quoted_by']) < 3:
			quote['short'] = "Name should be more than 3 characters."

		if len(postData['quote']) < 10:
			quote['shorter'] = "Quote should be more than 10 characters."

		return quote

class User(models.Model):
	name = models.CharField(max_length = 255)
	alias = models.CharField(max_length = 255)
	email = models.CharField(max_length = 255)
	password = models.CharField(max_length = 255)
	birthday = models.DateField()
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	objects = UserManager()

class Quote(models.Model):
	quoted_by = models.CharField(max_length = 255)
	quote = models.CharField(max_length = 255)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	posted_by = models.ForeignKey(User, related_name = "posted_quotes")
	fave_users = models.ManyToManyField(User, related_name = "fave_quotes")
	objects = QuoteManager()