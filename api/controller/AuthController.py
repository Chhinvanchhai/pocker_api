from flask import abort, jsonify, request, url_for
from flask_jwt_extended import create_access_token, get_jwt_identity
from api import app
from api.config.db import User
class AuthController: 
   
    def login(selt):
        username = request.json.get("username", None)
        password = request.json.get("password", None)
        if username != "test" or password != "test":
            return jsonify({"msg": "Bad username or password"}), 401
        
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token)

    def register(self):
        return "register"
    
    def logout(self):
        return "logout"
    
    def is_authenticated(self):
        return True
    
    def me(self):
        return "me"
    
    def validate_email(self, email):
        if User.query.filter_by(email=email.data).first():
            raise "error"

    def validate_uname(self, username):
        if User.query.filter_by(username=username.data).first():
             raise "error"
    def protected(self):
        return jsonify(logged_in_as="home"), 200