from django.shortcuts import render, HttpResponse, redirect
from time import strftime

def index(request):
	return render(request, 'session_app/sessionWords.html')

def add(request):

	if 'content' not in request.session:
		request.session['content'] = []

	if request.method == 'POST':
		content = {
			'word': request.POST['word'], 
			'datetime': " - "+strftime('%r, %b %e %Y'),
			'color': request.POST['color'],
			'big': request.POST['big']
		}
		request.session['content'].append(content)
		request.session['content'] = request.session['content']
		
		# print content
		# print request.session['content']

	return redirect('/')

def clear(request):
	del request.session['content']
	return redirect('/')