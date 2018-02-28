from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello():
	return "<h1>No ninjas here!</h1>"

@app.route('/ninja/')
def team():
	return render_template('teamNinja.html') 

@app.route('/ninja/<color>')
def ninja(color):
	if color == "orange":
		source = 'dnIMGS/michelangelo.jpg'
	elif color == "red":
		source = 'dnIMGS/raphael.jpg'
	elif color == "purple":
		source = 'dnIMGS/donatello.jpg'
	elif color == "blue":
		source = 'dnIMGS/leonardo.jpg'
	else:
		source = 'dnIMGS/notapril.jpg'
	
	return render_template('color.html', source=source)

app.run(debug = True)