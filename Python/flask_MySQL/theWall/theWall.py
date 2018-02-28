from flask import Flask, render_template, request, redirect, session, flash
from mysqlconnection import MySQLConnector
import re
import md5 
import os, binascii
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile(r'^[a-zA-Z]+$')
PW_REGEX = re.compile(r'^.*(?=.{8,15})(?=.*\d)(?=.*[a-zA-Z0-9]).*$')
app = Flask(__name__)
app.secret_key = "SecretsAreForKeeping"
mysql = MySQLConnector(app, 'wall')

@app.route('/')
def index():
	query = "SELECT * FROM users"
	users = mysql.query_db(query)
	# print users
	return render_template('theWall.html', all_users=users)

@app.route('/register', methods=['POST'])
def register():
	
	if len(request.form['first_name']) < 1 or len(request.form['last_name']) < 1 or len(request.form['email']) < 1 or len(request.form['password']) < 1 or len(request.form['confirm']) < 1:
		flash("All fields must be completed!")
		return redirect('/')
	if not NAME_REGEX.match(request.form['first_name']) or not NAME_REGEX.match(request.form['last_name']):
		flash("Your name cannot contain numbers.")
		return redirect('/')
	if not EMAIL_REGEX.match(request.form['email']):
		flash("Please enter a valid e-mail address!")
		return redirect('/')
	user_query = "SELECT * FROM users WHERE users.email = :email"
	query_data = {
			'email': request.form['email'],
		}
	user = mysql.query_db(user_query, query_data)
	# print user
	if len(user) != 0:
		flash("Your email is already in our database, please login.")
		return redirect('/')
	if not PW_REGEX.match(request.form['password']):
		flash("Your password must be at least 8 characters long.")
		return redirect('/')
	if request.form['confirm'] != request.form['password']:
		flash("Your passwords must match.")
		return redirect('/')
	else:
		flash("Thank you for registering!")
		salt = binascii.b2a_hex(os.urandom(15))
		hashed_password = md5.new(request.form['password'] + salt).hexdigest()
		insert_query = "INSERT INTO users (first_name, last_name, email, password, salt, created_at, updated_at) VALUES (:first_name, :last_name, :email, :hashed_password, :salt, NOW(), NOW())"
		query_data = {
				'first_name': request.form['first_name'],
				'last_name': request.form['last_name'],
				'email': request.form['email'],
				'hashed_password': hashed_password,
				'salt': salt
			}
		users_row = mysql.query_db(insert_query, query_data)
		session['email'] = request.form['email']
		session['name'] = request.form['first_name']
		# print users_row
		return redirect('/success')

@app.route('/success')
def success():
	query = "SELECT * FROM users"
	users = mysql.query_db(query)
	return render_template('theWallSuccess.html')

@app.route('/home', methods=['POST'])
def home():
	return redirect('/')

@app.route('/login', methods=['POST'])
def login():
	email = request.form['email']
	password = request.form['password']
	user_query = "SELECT * FROM users WHERE users.email = :email LIMIT 1"
	query_data = {
			'email': email,
		}
	user = mysql.query_db(user_query, query_data)
	session['email'] = request.form['email']
	if len(user) != 0:
		hashed_pw2 = md5.new(password + user[0]['salt']).hexdigest()
		if user[0]['password'] == hashed_pw2:
			session['id'] = user[0]['id']
			session['name'] = user[0]['first_name']
		return redirect('/message')
	else:
		flash("Email or password invalid.")
		return redirect('/')

@app.route('/message')
def message():
	msgquery = "SELECT CONCAT(users.first_name, ' ', users.last_name) as full_name, messages.id AS msg_id, messages.user_id, messages.message, DATE_FORMAT(messages.created_at, '%b %D %Y %r') AS created, messages.updated_at FROM messages JOIN users ON users.id = messages.user_id"
	msg = mysql.query_db(msgquery)
	cmtquery = "SELECT CONCAT(users.first_name, ' ', users.last_name) as full_name, messages.id AS msg_id, comments.user_id, comments.comment, DATE_FORMAT(comments.created_at, '%b %D %Y %r') AS created, comments.updated_at FROM comments JOIN users ON users.id = comments.user_id JOIN messages ON messages.id = comments.message_id"
	cmt = mysql.query_db(cmtquery)
	return render_template('theWallPost.html', all_msgs=msg, all_comments=cmt)

@app.route('/post1', methods=['POST'])
def post1():
	insert_query = "INSERT INTO messages (user_id, message, created_at, updated_at) VALUES (:user_id, :message, NOW(), NOW())"
	query_data = {
			'user_id': session['id'],
			'message': request.form['message']
		}
	user_msg = mysql.query_db(insert_query, query_data)
	# print user_msg
	return redirect('/message')

@app.route('/post2/<message_id>', methods=['POST'])
def post2(message_id):
	# print message_id
	insert_query = "INSERT INTO comments (user_id, message_id, comment, created_at, updated_at) VALUES (:user_id, :message_id, :comment, NOW(), NOW())"
	query_data = {
			'user_id': session['id'],
			'comment': request.form['comment'],
			'message_id': int(message_id)
		}
	user_comment = mysql.query_db(insert_query, query_data)
	# print user_comment
	return redirect('/message')

@app.route('/logout')
def logout():
	session['id'] = None
	session['name'] = None
	return redirect('/')

app.run(debug=True)