from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key='secrets'

@app.route('/')
def load():
	if 'random' not in session:
		randNumber = random.randrange(1,101)
		session['random'] = randNumber
	print session['random']
	return render_template('numberGame.html')

@app.route('/guess', methods=['POST'])
def guess():
	print request.form['number']
	number = int(request.form['number'])
	session['input'] = number

	if session['input'] == session['random']:
		session['msg'] = str(number) + ' was the number!'
		session.pop('random')
		session.pop('input')

	elif session['input'] < session['random']:
		session['msg'] = "Too low! Try again!"

	elif session['input'] > session['random']:
		session['msg'] = "Too high! Try again!"

	return redirect('/')

app.run(debug=True)