# -*- coding: utf-8 -*-
"""
Created on Fri May  3 22:12:42 2019

@author: DELL
"""
from flask import render_template,url_for,flash,redirect
from flaskblog.models import User,Post
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog import app,db,bcrypt

    
posts=[
       {
          'author':'Anjali Chachra',
          'title':'C Programming',
          'content':'First post',
          'date_posted':'May 24, 2019'

        },
        {
        'author':'Leena Sahu',
        'title':'Java Programming',
        'content':'Second post',
        'date_posted':'May 28, 2019'
                }]

@app.route('/')
@app.route('/home')
def hello_world():
    return render_template('home.html',posts=posts)

@app.route('/about')
def about():
    return render_template('about.html',title='About')

@app.route('/register',methods=['GET','POST'])
def register():
    form=RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(format('Account created! you are now able to log in.'),'success')
        return redirect(url_for('login'))
    return render_template('register.html',title='Register',form=form)

@app.route('/login',methods=['GET','POST'])
def login():
    form=LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'anjali.chachra@somaiya.edu' and form.password.data=='password':
            flash('You have been logged in successfully','success')
            return redirect(url_for('hello_world'))
        else:
            flash('Log in Unsuccsesfull. Please check Username and Password','danger')
    return render_template('login.html',title='Login',form=form)
