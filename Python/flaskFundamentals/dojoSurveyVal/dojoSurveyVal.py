from flask import Flask, render_template, request, redirect, session, flash
app = Flask(__name__)
app.secret_key = "ThisIsSecret!"

@app.route('/')
def survey():
	return render_template('dojoSurveyVal.html')

@app.route('/process', methods=['GET','POST'])
def form():
	name = request.form['name']
	location = request.form['location']
	language = request.form['language']
	comment = request.form['comment']
	# print name
	# print location
	# print language
	# print comment
	if len(request.form['name']) < 1:
		flash("Please enter a name!")
		return redirect('/')
	elif len(request.form['comment']) < 1:
		flash("Please enter a comment so we can know more about you.")
		return redirect('/')
	elif len(request.form['comment']) > 120:
		flash("Please shorten your comments to less than 120 characters.")
		return redirect('/')
	else:
		flash("Thank you for your information!")
		return render_template('resultsVal.html',name=request.form['name'],location=request.form['location'],language=request.form['language'],comment=request.form['comment'])

app.run(debug = True)