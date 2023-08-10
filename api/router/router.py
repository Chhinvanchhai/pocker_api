"""
 * @Author: Vanchhai
 * @Date: 2020-08-11 11:00:00
 * @Desciption: mapping route with plask and router
"""  

from api import app
import os
from flask import Flask, jsonify, request
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from api.controller.AuthController import AuthController
from api.controller.UserController import UserController
from api.services.UserSerivce import UserService

userService  = UserService()
userController = UserController(userService)
authController = AuthController()

# user routing
@app.route('/', methods = ['POST', 'GET'])
def welcome():   
  print("in=====welcome")
  print("process==env=", os.getenv("DOMAIN"))
  return "wellcome"

# user routing
@app.route('/users', methods = ['POST', 'GET'])
def users():   
  return  userController.users()

@app.route('/users/<int:id>', methods = ['GET'])
def get(id):
  return userController.get(id)

@app.route('/users/<int:id>/update', methods = ['POST'])
def update(id):
  return userController.update(id)

@app.route('/users/<int:id>', methods = ['DELETE'])
def delete(id):
  return userController.delete(id)

# auth routing
@app.route('/login', methods=['POST'])
def login():
  return authController.login()

@app.route("/protected", methods=["GET"])
@jwt_required()
def protected():
   get_jwt_identity()
   return authController.protected()
