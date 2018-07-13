#!/usr/bin/python3

from flask import Flask,render_template
from loll import hello

app=Flask(__name__)

@app.route('/')
def try1():
	return render_template('lol.html')	


@app.route('/file')
def second():
	hello()
	return '<h1><center>THANK YOU</center></h1>'

if __name__ == '__main__':
	app.run(debug = True)
