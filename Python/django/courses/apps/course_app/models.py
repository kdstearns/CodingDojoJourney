from __future__ import unicode_literals
from django.db import models

class CourseManager(models.Manager):
	def basic_validator(self, postData):
		errors = {}
		# print postData

		if len(postData['courseName']) < 1 or len(postData['desc']) < 1 :
			errors['blank'] = "All fields must be completed!"

		if len(postData['courseName']) < 5:
			errors['nameShort'] = "Name must be more than 5 characters."

		if len(postData['desc']) < 15:
			errors['descShort'] = "Name must be more than 15 characters."
			
		nameVal = Course.objects.filter(courseName = postData['courseName'])
		if len(nameVal) != 0:
			errors['nameShort'] = "This course is already in our database."

		return errors

class Course(models.Model):
	courseName = models.CharField(max_length = 255)
	desc = models.CharField(max_length = 255)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	objects = CourseManager()