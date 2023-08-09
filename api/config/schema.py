
from app import db
import datetime

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