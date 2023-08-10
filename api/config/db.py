
import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from api import app
import pymysql


# create the app
# configure the SQLite database, relative to the app instance folder

# ========
# userpass = 'mysql+pymysql://root:@'
# basedir  = '127.0.0.1'
# dbname   = '/pocker'
# socket   = '?unix_socket=/Applications/XAMPP/xamppfiles/var/mysql/mysql.sock'
# dbname   = dbname + socket
# app.config['SQLALCHEMY_DATABASE_URI'] = userpass + basedir + dbname
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# ========
db = SQLAlchemy()
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
db.init_app(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(225), unique=True, nullable=False)
    password = db.Column(db.String(225), nullable=False)
    email = db.Column(db.String(225))
    lastName = db.Column(db.String(225))
    firstName = db.Column(db.String(225))
    status = db.Column(db.String(225))
    createdAt = db.Column(db.DateTime, default=datetime.date.today())

class Roles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(225), unique=True, nullable=False)
    type = db.Column(db.String(225))
    permissions = db.Column(db.String(225))
    createdAt = db.Column(db.DateTime, default=datetime.date.today())

with app.app_context():
    db.create_all()
