from flask import Flask, render_template, request, redirect, session, flash
import re 
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile(r'^[a-zA-Z]+$')
PW_REGEX = re.compile(r'^.*(?=.{8,15})(?=.*\d)(?=.*[a-zA-Z]).*$')
app = Flask(__name__)
app.secret_key = "GuessMySecret"

@app.route('/')
def load():
	return render_template('regForm.html')

@app.route('/process', methods = ['POST'])
def form():

	if len(request.form['email']) < 1:
		flash("You must enter your email address.")
		return redirect('/')
	elif not EMAIL_REGEX.match(request.form['email']):
		flash("Please enter a valid email address.")

	if len(request.form['first']) < 1:
		flash("You must enter your first name.")
	elif not NAME_REGEX.match(request.form['first']):
		flash("Your first name cannot contain numbers.")

	if len(request.form['last']) < 1:
		flash("You must enter your last name.")
	elif not NAME_REGEX.match(request.form['last']):
		flash("Your last name cannot contain numbers.")

	if len(request.form['password']) < 1:
		flash("You must enter your password.")
	elif not PW_REGEX.match(request.form['password']):
		flash("Your password must contain 1 uppercase letter and 1 digit")

	if len(request.form['confirm']) < 1:
		flash("You must confirm your password.")
	elif not request.form['confirm'] == request.form['password']:
		flash("Your passwords must match.")

	else: 
		flash("Thank you for submitting your information.")
	
	return redirect('/')

app.run(debug=True)