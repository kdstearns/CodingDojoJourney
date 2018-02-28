from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from models import *
import bcrypt
from datetime import date, datetime
from time import time

def index(request):
	return render(request, 'quote_app/loginReg.html')

def success(request):
	showUser = User.objects.get(id = request.session['id'])
	# print showUser
	faveQuotes = showUser.fave_quotes.all()
	# print faveQuotes

	allQuotes = Quote.objects.all()
	# print allQuotes
	# for objects in allQuotes:
	# 	print objects.quoted_by
	# 	print objects.quote
	otherQuotes = Quote.objects.exclude(fave_users = showUser)
	# print otherQuotes
	# for objects in otherQuotes:
	# 	print objects.quoted_by
	# 	print objects.quote
	
	context = {
		'show': showUser,
		'faveQuote': faveQuotes,
		'allQuote': otherQuotes
	}
	return render(request, 'quote_app/dashboard.html', context)

def userposts(request, id):
	thisUser = User.objects.get(id = id)
	count = thisUser.posted_quotes.count()
	userQuotes = thisUser.posted_quotes.all()
	# print userQuotes
	# count = 0
	# for objects in userQuotes:
	# 	count += 1
	# print count
	# 	print objects.quoted_by
	# 	print objects.quote
	context = {
		'show': thisUser,
		'postQuote': userQuotes,
		'count': count
	}
	return render(request, 'quote_app/update.html', context)

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
			user = User.objects.create(name = request.POST['name'], alias = request.POST['alias'], email = request.POST['email'], password = hash1, birthday = request.POST['birthday'])
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

def addquote(request):
	if request.method == 'POST':
		quote = Quote.objects.quote_validator(request.POST)
		if len(quote):
			for tag, error in quote.iteritems():
				messages.error(request, error, extra_tags = tag)
			return redirect('/success')
		else:
			userQuote = User.objects.get(id = request.session['id'])
			newQuote = Quote.objects.create(posted_by = userQuote, quoted_by = request.POST['quoted_by'], quote = request.POST['quote'])
			
			return redirect('/success')

def addlist(request, id):
	if request.method == 'POST':
		thisQuote = Quote.objects.get(id=id)
		# print thisQuote
		thisUser = User.objects.get(id = request.session['id'])
		# print thisUser
		thisQuote.fave_users.add(thisUser)
		return redirect('/success')

def removelist(request, id):
	if request.method == 'POST':
		thisQuote = Quote.objects.get(id = id)
		thisUser = User.objects.get(id = request.session['id'])
		thisQuote.fave_users.remove(thisUser)
		return redirect('/success')

def logout(request):
	request.session.pop('id')
	return redirect('/')
