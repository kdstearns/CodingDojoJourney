from __future__ import unicode_literals
from django.db import models

import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile(r'^[a-zA-Z]+$')

class UserManager(models.Manager):
	def basic_validator(self, postData):
		errors = {}

		if len(postData['first']) < 1 or len(postData['last']) < 1 or len(postData['email']) < 1 :
			errors['blank'] = "All fields must be completed!"
			
		if not NAME_REGEX.match(postData['first']) or not NAME_REGEX.match(postData['last']):
			errors['name'] = "Your name cannot contain numbers."
			
		if not EMAIL_REGEX.match(postData['email']):
			errors['email'] = "Please enter a valid e-mail address!"

		emailVal = User.objects.filter(email = postData['email'])
		if len(emailVal) != 0:
			errors['userEmail'] = "Your email is already in our database, if you would like to change it, please go to our Update page."

		return errors


class User(models.Model):
	first_name = models.CharField(max_length = 255)
	last_name = models.CharField(max_length = 255)
	email = models.CharField(max_length = 255)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	objects = UserManager()