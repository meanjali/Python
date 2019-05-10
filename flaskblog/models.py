# -*- coding: utf-8 -*-
"""
Created on Fri May  3 14:31:59 2019

@author: DELL
"""
from datetime import datetime
from flaskblog import db,login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        #return format(User('{self.username}', '{self.email}', '{self.image_file}'))
        #return f"User('{self.username}', '{self.email}', '{self.image_file}')"
        return 'Username is {} and email is {}  and image is {} .'.format(self.username, self.email,self.image_file)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return 'Title is {} and Date Posted is {} and content is {} .'.format(self.title, self.date_posted,self.content)
