from flask import Flask

app  = Flask("api")
app.secret_key = '123456'
from api.router.router import *