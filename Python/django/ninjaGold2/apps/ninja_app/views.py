from django.shortcuts import render, HttpResponse, redirect
import random
from datetime import datetime
from time import strftime

def index(request):
	
	if not 'goldMoney' in request.session:
		request.session['goldMoney'] = 0
	if not 'msg' in request.session:
		request.session['msg']= ''
	return render(request, 'ninja_app/ninjaGold2.html')

def process(request):  

	if request.POST['building'] == "farm":
		gain = random.randrange(10,21)
		# print gain
		request.session['goldMoney'] += gain
		request.session['msg'] += "You earned "+str(gain)+" gold from the farm! "+datetime.now().strftime('%m-%d-%Y %I:%M %p')+"\n"
		request.session['split'] = request.session['msg'].split('\n')
	
	if request.POST['building'] == "cave":
		gain = random.randrange(5,11)
		# print gain
		request.session['goldMoney'] += gain
		request.session['msg'] += "You earned "+str(gain)+" gold from the cave! "+datetime.now().strftime('%m-%d-%Y %I:%M %p')+"\n"
		request.session['split'] = request.session['msg'].split('\n')

	if request.POST['building'] == "house":
		gain = random.randrange(2,6)
		# print gain
		request.session['goldMoney'] += gain
		request.session['msg'] += "You earned "+str(gain)+" gold from the house! "+datetime.now().strftime('%m-%d-%Y %I:%M %p')+"\n"
		request.session['split'] = request.session['msg'].split('\n')

	if request.POST['building'] == "casino":
		gainLoss = random.randrange(-50,51)
		# print gainLoss
		request.session['goldMoney'] += gainLoss
		if gainLoss == 0:
			request.session['msg'] += "You got "+str(gainLoss)+" gold from the casino! "+datetime.now().strftime('%m-%d-%Y %I:%M %p')+"\n"
			request.session['split'] = request.session['msg'].split('\n')
		elif gainLoss > 0:
			request.session['msg'] += "You won "+str(gainLoss)+" gold at the casino! "+datetime.now().strftime('%m-%d-%Y %I:%M %p')+"\n"
			request.session['split'] = request.session['msg'].split('\n')
		else:
			request.session['msg'] += "The casino took "+str(abs(gainLoss))+" gold from you, dude! "+datetime.now().strftime('%m-%d-%Y %I:%M %p')+"\n"
			request.session['split'] = request.session['msg'].split('\n')

	return redirect('/')

def reset(request):

	del request.session['goldMoney']
	del request.session['msg']
	del request.session['split']
	# print 'Start Over'
	return redirect('/')