#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from flask import Flask,make_response,request,abort,render_template,flash
from flask_wtf import Form
from wtforms import StringField, SubmitField, TextAreaField,FileField,PasswordField
from wtforms.validators import DataRequired, Length, Email, Optional
from flask.ext.bootstrap import Bootstrap
app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config.from_object('config') 
class LoginForm(Form):
    user = StringField('user',validators=[DataRequired()])
    password = PasswordField('password',validators=[DataRequired()])
    file = FileField('file',validators=[DataRequired()])
    submit = SubmitField('Submit')

@app.route('/user/<name>') 
def user(name):
    #return '<h1>Hello %s</h1>' % name
    return render_template('user.html',name=name)

@app.route('/', methods = ['GET','POST'])
def index():
	name = ""
	password = ""
	form = LoginForm()
	if form.validate_on_submit():
		user = form.user.data
		password = form.password.data
		form.name.data = ''
		form.password.data = ''
		if user != 'admin':
			flash("not admin")
			pass
	return render_template('index.html',form=form, user=name, password = password)
	#return render_template('index.html')


@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'), 404 

@app.errorhandler(500)
def page_not_found(e):
	return render_template('500.html'), 404
		

if __name__ == '__main__':
    app.run(host="localhost",port=8888,debug=True)
