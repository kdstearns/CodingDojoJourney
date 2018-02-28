from __future__ import unicode_literals
from django.db import models
import bcrypt
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile(r'^[a-zA-Z .]+$')

class UserManager(models.Manager):
	def basic_validator(self, postData):
		errors = {}

		if len(postData['name']) < 1 or len(postData['email']) < 1 or len(postData['password']) < 1 or len(postData['confirm']) < 1 :
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
		if not bcrypt.checkpw(postData['password'].encode(), user[0].password.encode()):
			match['pw'] = "Your password is incorrect."

		if len(user) == 0:
			match['address'] = "Your email is not in our database."

		return match

class BookManager(models.Manager):
	def book_validator(self, postData):
		book = {}

		if len(postData['title']) < 1 or len(postData['review']) < 1 or len(postData['rating']) < 1 :
			book['blank'] = "All fields must be completed."

		if not NAME_REGEX.match(postData['add_author']):
			book['name'] = "Author name cannot contain numbers."
		
		bookVal = Book.objects.filter(title = postData['title'])
		if len(bookVal) != 0:
			book['dup'] = "This book title has already been reviewed, please add your review from the home page."

		if len(postData['author']) < 1 and len(postData['add_author']) < 1:
			book['author'] = "You must either choose an author or add a new one."

		if len(postData['author']) > 1 and len(postData['add_author']) > 1:
			book['author'] = "You must either choose an author or add a new one."

		authorVal = Author.objects.filter(name = postData['add_author'])
		if len(authorVal) != 0:
			book['author_dup'] = "This author is already in our database, please choose from the list."
			
		return book

class User(models.Model):
	name = models.CharField(max_length = 255)
	alias = models.CharField(max_length = 255)
	email = models.CharField(max_length = 255)
	password = models.CharField(max_length = 255)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	objects = UserManager()

class Book(models.Model):
	title = models.CharField(max_length = 255)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	objects = BookManager()

class Author(models.Model):
	name = models.CharField(max_length = 255)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	books_written = models.ForeignKey(Book, related_name = "written_by")
	objects = BookManager()

class Review(models.Model):
	review = models.TextField()
	rating = models.IntegerField()
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	reviewed_by = models.ForeignKey(User, related_name = "reviewed_books")
	book_reviewed = models.ForeignKey(Book, related_name = "have_reviews")
	objects = BookManager()