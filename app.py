

from api import app
from api.config.db import db
from flask_sqlalchemy import SQLAlchemy
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
    
if __name__ == '__main__':
    app.run(host="localhost", port=8000, debug=True)