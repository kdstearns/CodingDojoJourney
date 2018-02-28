from flask import Flask, render_template, request, redirect, session
import random
from datetime import datetime
app = Flask(__name__)
app.secret_key='toomanysecrets'

@app.route('/')
def load():
	if not 'goldMoney' in session:
		session['goldMoney'] = 0
	if not 'msg' in session:
		session['msg']= ''
	return render_template('ninjaGold.html')

@app.route('/process_money', methods=['POST'])
def process():  

	if request.form['building'] == "farm":
		gain = random.randrange(10,21)
		# print gain
		session['goldMoney'] += gain
		session['msg'] += "You earned "+str(gain)+" gold from the farm! "+datetime.now().strftime('%m-%d-%Y %I:%M %p')+"\n"
		session['split'] = session['msg'].split('\n')
	
	if request.form['building'] == "cave":
		gain = random.randrange(5,11)
		# print gain
		session['goldMoney'] += gain
		session['msg'] += "You earned "+str(gain)+" gold from the cave! "+datetime.now().strftime('%m-%d-%Y %I:%M %p')+"\n"
		session['split'] = session['msg'].split('\n')

	if request.form['building'] == "house":
		gain = random.randrange(2,6)
		# print gain
		session['goldMoney'] += gain
		session['msg'] += "You earned "+str(gain)+" gold from the house! "+datetime.now().strftime('%m-%d-%Y %I:%M %p')+"\n"
		session['split'] = session['msg'].split('\n')

	if request.form['building'] == "casino":
		gainLoss = random.randrange(-50,51)
		# print gainLoss
		session['goldMoney'] += gainLoss
		if gainLoss == 0:
			session['msg'] += "You got "+str(gainLoss)+" gold from the casino! "+datetime.now().strftime('%m-%d-%Y %I:%M %p')+"\n"
			session['split'] = session['msg'].split('\n')
		elif gainLoss > 0:
			session['msg'] += "You won "+str(gainLoss)+" gold at the casino! "+datetime.now().strftime('%m-%d-%Y %I:%M %p')+"\n"
			session['split'] = session['msg'].split('\n')
		else:
			session['msg'] += "The casino took "+str(abs(gainLoss))+" gold from you, dude! "+datetime.now().strftime('%m-%d-%Y %I:%M %p')+"\n"
			session['split'] = session['msg'].split('\n')

	return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():

	session.pop('goldMoney')
	session.pop('msg')
	session.pop('split')
	# print 'Start Over'
	return redirect('/')

app.run(debug=True)