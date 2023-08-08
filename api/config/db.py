
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from api import app


db = SQLAlchemy()
# create the app
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
# initialize the app with the extension
db.init_app(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String)

with app.app_context():
    db.create_all()
    

# class SqlConnection:
#     connection = ""
#     # def __init__(self):
#     def db(): 
#         connection = SQLAlchemy()
#         connection.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
#         connection.init_app(app)
#         connection.create_all()
#         return connection