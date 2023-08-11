from datetime import datetime
from flask import Flask, Request
from flask_jwt_extended import JWTManager
import logging
from logging import Formatter, FileHandler

app  = Flask("api")
app.config["JWT_SECRET_KEY"] = "super-secret"  # Change this!
jwt = JWTManager(app)

# for login file
log_name = './api/logs/'+str(datetime.now().strftime("%Y-%m-%d"))+".log"
file_handler = FileHandler(log_name)
file_handler.setLevel(logging.DEBUG)
app.logger.addHandler(file_handler)
app.logger.setLevel(logging.INFO)

# middleware
from api.router.router import *

