# -*- coding: utf-8 -*-
"""
Created on Fri May  3 21:30:53 2019

@author: DELL
"""

from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_bcrypt import Bcrypt


app = Flask(__name__)

app.config['SECRET_KEY']='6c63274225d399af50f4fbff9821ad79'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'

db=SQLAlchemy(app)
bcrypt=Bcrypt(app)

from flaskblog import routes