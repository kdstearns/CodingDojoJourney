from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from models import *
import bcrypt
from time import time

def index(request):
	return render(request, 'review_app/loginReg.html')

def success(request):
	showUser = User.objects.get(id = request.session['id'])
	# print showUser
	descending = Review.objects.order_by("-created_at")
	recent = []
	title = []
	i = 1	
	for element in descending:

		if i < 4:
			recent.append(element)
			title.append(element.book_reviewed.title)
			i += 1
			# print recent
			# print title

	otherBooks = []
	allBooks = Review.objects.all()
	for element in allBooks:
		if element.book_reviewed.title not in title:
			otherBooks.append(element.book_reviewed)
			# print otherBooks
	
	context = {
		'show': showUser,
		'recent': recent,
		'title': title,
		'other': otherBooks
	}

	return render(request, 'review_app/dashboard.html', context)

def add(request):
	allAuthors = Author.objects.all()
	context = {
		'author': allAuthors
	}
	return render(request, 'review_app/addBook.html', context)

def user_reviews(request, id):
	thisUser = User.objects.get(id = id)
	userReviews = Review.objects.filter(reviewed_by = id)
	count = userReviews.count()
	# print userReviews
	# print count
	
	context = {
		'show': thisUser,
		'review': userReviews,
		'count': count
	}
	return render(request, 'review_app/user.html', context)

def book_reviews(request, id):
	thisBook = Book.objects.get(id = id)
	bookReviews = Review.objects.filter(book_reviewed = thisBook)
	bookAuthor = Author.objects.filter(books_written = thisBook)
	# print thisBook
	# print bookReviews
	# print bookAuthor

	context = {
		'book': thisBook,
		'review': bookReviews,
		'author': bookAuthor
	}
	return render(request, 'review_app/book.html', context)

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
			user = User.objects.create(name = request.POST['name'], alias = request.POST['alias'], email = request.POST['email'], password = hash1)
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

def add_book(request):
	if request.method == 'POST':
		book = Book.objects.book_validator(request.POST)
		# print book
		if len(book):
			for tag, error in book.iteritems():
				messages.error(request, error, extra_tags = tag)
			return redirect('/books/add')
		else:
			if len(request.POST['add_author']) > 0:
				author = request.POST['add_author']
				# print author
				newBook = Book.objects.create(title = request.POST['title'])
				newAuthor = Author.objects.create(name = author, books_written = newBook)
				userReview = User.objects.get(id = request.session['id'])
				newReview = Review.objects.create(review = request.POST['review'], rating = request.POST['rating'], book_reviewed = newBook, reviewed_by = userReview)

				return redirect('/success')
			else: 
				author = Author.objects.get(name = request.POST['author'])
				# print author
				newBook = Book.objects.create(title = request.POST['title'])
				userReview = User.objects.get(id = request.session['id'])
				Review.objects.create(review = request.POST['review'], rating = request.POST['rating'], book_reviewed = newBook, reviewed_by = userReview)
				
				return redirect('/success')
			

def add_review(request, id):
	if request.method == 'POST':
		thisBook = Book.objects.get(id=id)
		# print thisBook
		thisUser = User.objects.get(id = request.session['id'])
		# print thisUser
		newReview = Review.objects.create(review = request.POST['review'], rating = request.POST['rating'], book_reviewed = thisBook, reviewed_by = thisUser)
		return redirect('/books/'+str(id))

def delete_review(request, id, book_id):
	thisReview = Review.objects.get(id = id)
	# print thisReview
	thisReview.delete()
	return redirect('/books/'+str(book_id))

def logout(request):
	request.session.pop('id')
	return redirect('/')
