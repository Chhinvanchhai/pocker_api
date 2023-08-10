from flask import Flask
from flask_jwt_extended import JWTManager

app  = Flask("api")
app.config["JWT_SECRET_KEY"] = "super-secret"  # Change this!
jwt = JWTManager(app)
from api.router.router import *

