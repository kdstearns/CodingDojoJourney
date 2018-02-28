from django.shortcuts import render, HttpResponse, redirect

def index(request):
	return render(request, 'amadon_app/amadon.html')

def receipt(request):
	product_id = int(request.POST['product_id'])
	quantity = int(request.POST['quantity'])
	if 'total' not in request.session:
		request.session['total'] = 0
		request.session['grandTotal'] = 0
		request.session['quantTotal'] = 0

	if product_id == 100:
		price = 19.99
		total = price * quantity

	if product_id == 101:
		price = 29.99
		total = price * quantity

	if product_id == 102: 
		price = 4.99
		total = price * quantity

	if product_id == 103:
		price = 49.99
		total = price * quantity

	request.session['total'] = total
	request.session['grandTotal'] += total 
	request.session['quantTotal'] += quantity
	# print request.session['total']
	# print request.session['grandTotal']
	# print request.session['quantTotal']

	return redirect('/amadon/checkout')

def checkout(request):
	return render(request, 'amadon_app/amadonReceipt.html')

def purchase(request):
	return redirect('/amadon')