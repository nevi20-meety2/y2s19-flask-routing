from databases import *
from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route('/')
def home():
	return render_template('home.html')
    # return "home page" 

@app.route('/student/<int:number>')
def display_student(number):
	query_by_id(number)
	return render_template("student.html", id_number=number, student=query_by_id(number))
	# return render_template('student.html', id_number = number)



if __name__ == '__main__':
	app.run(debug=True)
